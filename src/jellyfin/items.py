"""
Module `items` - High-level interface for ItemsApi, BaseItemDto and BaseItemDtoQueryResult.
"""

import copy, warnings
from pydantic import BaseModel
from typing import List, Union, Any, Dict, Protocol
from enum import Enum
from .base import Model, Single, CollectionPagination
from .generated import (
    BaseItemKind,
    BaseItemDtoQueryResult, 
    BaseItemDto, 
    ItemsApi
)

class Item(Single):
    _naming: str = "Item"

class ItemCollection(Model):
    _data: BaseItemDtoQueryResult = None
    _pagination: CollectionPagination = None

    def __init__(self, collection: BaseItemDtoQueryResult, pagination: CollectionPagination = None):
        """
        Initializes the ItemCollection class.
        
        Args:
            collection (BaseItemDtoQueryResult): The collection of items.
            pagination (CollectionPagination, optional): An optional pagination handler. Defaults to None.
        """
        self._data = collection
        self._iterator = None
        self._current = None
        self._pagination = pagination
        
    def to_dict(self) -> Dict[str, Any]:
        """ Signature method for generated models"""
        return super().to_dict()['Items']
        
    @property
    def items(self) -> List[Item]:
        """
        Returns the list of items in the collection.
        
        Returns:
            List[Item]: A list of Item objects.
        """
        if self._data is None:
            return []
        
        for item in self._data.items:
            yield Item(item)

    def __iter__(self):
        """
        Returns an iterator for the collection.

        Usage:
            collection = ItemCollection(...)
            for item in collection:
                print(collection.current)  # Always shows the current item
        """
        current = self.items
        while True:
            self._iterator = iter(current)
            self._current = None
            for item in current:
                yield item
                
            if self._pagination is None:
                break

            collection = self._pagination.next_page()
            if collection.current is None:
                break

            current = collection.items
            
        return self

    def __next__(self):
        """
        Returns the next item in the iteration.
        """
        self._current = next(self._iterator)
        return self._current
    
    def __len__(self):
        """
        Returns the number of items in the collection.
        """
        return self.total

    @property
    def current(self):
        """
        Returns the current item in the iteration, or None if not started.
        """
        if len(self._data.items) == 0:
            return None

        if len(self._data.items) > 0:
            return next(self.items)
        
        return self._current

    @property
    def all(self) -> List[Item]:
        """
        Returns all items in the collection as a list.

        Returns:
            List[Item]: A list of all Item objects.
        """
        return list(self.items)

    @property
    def total(self) -> int:
        """
        Returns the total number of records in the collection.

        Returns:
            int: The total number of records.
        """
        if self._data is None:
            return 0
        
        if self._data.total_record_count is None:
            return len(self._data.items)
        
        return self._data.total_record_count
    
    @property
    def index(self) -> int:
        """
        Returns the start index of the collection.
        
        Returns:
            int: The start index.
        """
        if self._data is None:
            return 0
        
        if self._data.start_index is None:
            return 0
        
        return self._data.start_index

    def by_name(self, name: str) -> 'ItemCollection':
        """
        Returns all items that match the specified name.

        Args:
            name (str): The name to search for.
        """
        return self.filter({"name": name})
    
    def first(self, attr: str, value: Any) -> Item | None:
        """
        Returns the first item that matches the specified attribute and value.
        
        Args:
            attr (str): The attribute to search by.
            value (Any): The value to match.
        """
        for item in self.filter({attr: value}, limit=1).items:
            return item
        return None

    def filter(self, criteria: dict, limit: int = None) -> 'ItemCollection':
        """
        Returns a list of items that match the specified criteria.
        
        Args:
            criteria (dict): A dictionary of attribute-value pairs to filter by.
            limit (int, optional): The maximum number of items to return. Defaults to None (no limit).
            
        Returns:
            list: A list of Item objects that match the criteria.
        """
        if self._data is None or not hasattr(self._data, "items"):
            return []

        result = []
        for item in self._data.items:
            match = True
            for key, value in criteria.items():
                if getattr(item, key, None) != value:
                    match = False
                    break
            if match:
                result.append(item)
                if limit is not None and len(result) >= limit:
                    break
                
        dto = copy.deepcopy(self._data)
        dto.items = result
        dto.total_record_count = len(result)
        return ItemCollection(dto)

    def __repr__(self) -> str:
        if len(self._data.items) == 0:
            return "<ItemCollection (no items)>"
        
        items = list(getattr(self._data, "items", []))
        items_repr = ""
        
        for item in items[:10]:
            attrs = repr(Item(item)).split(',\n')
            items_repr += ",\n".join(attrs[:10])

            if len(attrs) > 10:
                items_repr += ", ...\n"

        if len(items) > 10:
            items_repr += "  ..."
        return (
            f"<ItemCollection total={self.total} start_index={self.index} items=[\n  {items_repr}\n]>"
        )

class ItemSearch():
    """ Based on DataFrame Builder pattern
    
    Usage:
        search = api.items.search
        search.is_movie = False
        search.user_id = "abc"
        result = search.all()
        
        api.items.search.add(is_movie=False).all()
        api.items.search.filter({
            "is_movie": False, 
            "user_id": "abc"
        }).all()
    """
    _page_size: int = 0

    def __init__(self, items_api):
        self.items_api = items_api
        self._params = {}

    def __setattr__(self, name, value):
        """ Set a filter using 'search.attr = value'
        
        Args:
            name (str): The name of the attribute to set.
            value (Any): The value to set the attribute to.
        """
        if name in ("items_api", "_params", "_page_size"):
            super().__setattr__(name, value)
        else:
            self._params[name] = value

    def __getattr__(self, name):
        """ Get a filter using 'search.attr' 
        
        Args:
            name (str): The name of the attribute to retrieve.
            
        Returns:
            Any: The value of the specified attribute, or None if not found.
        """
        if name in self._params:
            return self._params[name]
    
    def __delattr__(self, name):
        """ Remove a filter using 'del search.attr'
        
        Args:
            name (str): The name of the attribute to remove.
        """
        if name in self._params:
            del self._params[name]
    
    def __repr__(self) -> str:
        if not self._params:
            return "<ItemSearch (no filters set)>"
        filtros = ",\n  ".join(f"{k}={v!r}" for k, v in self._params.items())
        return f"<ItemSearch filters={{\n  {filtros}\n}}>"
    
    def add(self, key: str, value: Any) -> 'ItemSearch':
        """ Add multiple filters at once using 'search.add(attr=value, ...)' 
        
        Args:
            key (str): The name of the attribute to add.
            value (Any): The value to set the attribute to.

        Returns:
            ItemSearch: The current ItemSearch instance (for chaining).
        """
        self._params[key] = value
        return self
    
    def remove(self, key: str) -> 'ItemSearch':
        """ Remove multiple filters at once using 'search.remove(attr, ...)' 
        
        Args:
            key (str): The name of the attribute to remove.

        Returns:
            ItemSearch: The current ItemSearch instance (for chaining).
        """
        if key in self._params:
            del self._params[key]
        return self

    def filter(self, criteria: dict) -> 'ItemSearch':
        """ Add multiple filters at once using 'search.filter({attr: value, ...})' 
        
        Args:
            criteria (dict): A dictionary of attribute-value pairs to filter by.

        Returns:
            ItemSearch: The current ItemSearch instance (for chaining).
        """
        for key, value in criteria.items():
            self._params[key] = value
        return self

    def copy(self) -> 'ItemSearch':
        """
        Returns an independent copy of the search object (similar to pandas).
        
        Returns:
            ItemSearch: A new instance of ItemSearch with the same filters.
        """
        new_search = ItemSearch(self.items_api)
        new_search._params = copy.deepcopy(self._params)
        return new_search
    
    def next_page(self) -> 'ItemCollection':
        """
        Move to the next page of results based on the current pagination settings.

        Returns:
            ItemSearch: The current ItemSearch instance (for chaining).
        """
        self._params['start_index'] += self._page_size
        self._params['limit'] = self._page_size

        return self.all

    def paginate(self, size: int = 100) -> 'ItemSearch':
        """
        Enable pagination.
        
        Args:
            size (int): The maximum number of results to return per page. Defaults to 100. Zero turns off pagination.

        Returns:
            ItemSearch: The current ItemSearch instance (for chaining).
        """
        if size < 0:
            raise ValueError("Page size must be a non-negative integer.")
        
        self._page_size = size
        self._params['start_index'] = 0
        self._params['limit'] = size
        self._params['enable_total_record_count'] = bool(size > 0)
        return self

    @property
    def all(self) -> 'ItemCollection':
        """
        Execute the search and return all results as an ItemCollection 
        
        Returns:
            ItemCollection: A collection of items matching the search criteria.
        """
        pagination = self if self._page_size > 0 else None
        collection = self.items_api.get_items(**self._params)
        
        return ItemCollection(collection, pagination)

    def only_library(self) -> 'ItemSearch':
        """ Shortcut to filter only libraries (collections) """
        self._params["include_item_types"] = [BaseItemKind.COLLECTIONFOLDER.value]
        self._params["recursive"] = True
        return self

class Items():
    def __init__(self, items_api: ItemsApi):
        """
        Initializes the Items API wrapper.
        
        Args:
            items_api (ItemsApi): An instance of the generated ItemsApi class.
        """
        self.items_api = items_api
        
    @property
    def all(self) -> ItemCollection:
        """
        Returns all items.
        
        Returns:
            ItemCollection: A list of all items.
        """
        return ItemCollection(self.filter())

    @property
    def filter(self) -> ItemsApi.get_items:
        """
        Returns a filtered list of items.

        Returns:
            ItemsApi.get_items: A filtered list of items.
        """
        return self.items_api.get_items
    
    @property
    def search(self) -> ItemSearch:
        """
        Returns an ItemSearch instance for building search queries.

        Returns:
            ItemSearch: An instance of ItemSearch for building search queries.
        """
        return ItemSearch(self.items_api)
