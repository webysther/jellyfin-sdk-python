"""
Module `items` - High-level interface for ItemsApi.
"""

import copy
from pydantic import BaseModel
from typing_extensions import Self
from typing import List, Any, Callable
from .base import Model, Collection, Pagination
from .generated import (
    BaseItemKind,
    ItemsApi
)

class Item(Model):
    pass

class ItemCollection(Collection):
    _factory: Callable = Item

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

    def __init__(self, items_api):
        self.items_api = items_api
        self._params = {}
        self._page_size = 0

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
    
    def add(self, key: str, value: Any) -> Self:
        """ Add multiple filters at once using 'search.add(attr=value, ...)' 
        
        Args:
            key (str): The name of the attribute to add.
            value (Any): The value to set the attribute to.

        Returns:
            ItemSearch: The current ItemSearch instance (for chaining).
        """
        self._params[key] = value
        return self
    
    def remove(self, key: str) -> Self:
        """ Remove multiple filters at once using 'search.remove(attr, ...)' 
        
        Args:
            key (str): The name of the attribute to remove.

        Returns:
            ItemSearch: The current ItemSearch instance (for chaining).
        """
        if key in self._params:
            del self._params[key]
        return self
    
    def next_page(self) -> ItemCollection:
        """
        Move to the next page of results based on the current pagination settings.

        Returns:
            ItemCollection: A collection of items for the next page.
        """
        self._params['start_index'] += self._page_size
        self._params['limit'] = self._page_size

        return self.all

    def paginate(self, size: int = 100) -> Self:
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
    def all(self) -> ItemCollection:
        """
        Execute the search and return all results as an ItemCollection 
        
        Returns:
            ItemCollection: A collection of items matching the search criteria.
        """
        return ItemCollection(
            Model(self.items_api.get_items(**self._params)), 
            self if self._page_size > 0 else None
        )
    
    def recursive(self, flag: bool = True) -> Self:
        """ Shortcut to enable recursive search """
        self._params["recursive"] = flag
        return self
    
    def name_starts_with(self, prefix: str) -> Self:
        """ Shortcut to filter by name prefix """
        self._params["name_starts_with"] = prefix
        return self

    def only_library(self) -> Self:
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
        Returns all items as an ItemCollection.

        Returns:
            ItemCollection: A collection of all items.
        """
        return self.search.recursive().paginate().all

    @property
    def search(self) -> ItemSearch:
        """
        Returns an ItemSearch instance for building search queries.

        Returns:
            ItemSearch: An instance of ItemSearch for building search queries.
        """
        return ItemSearch(self.items_api)
