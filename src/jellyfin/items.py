"""
Module `items` - High-level interface for ItemsApi, BaseItemDto and BaseItemDtoQueryResult.
"""

from pydantic import BaseModel
from typing import List, Union, Any, Dict
from .typing import BaseItemQueryResult, BaseItem
from .base import Model

class Item(Model):
    _data: BaseItem = None

    def __init__(self, item: BaseItem):
        """
        Initializes the Item class.

        Args:
            item (BaseItem): The item data.
        """
        self._data = item
        
    def __repr__(self) -> str:
        """Returns a string representation of the Item object."""
        return (
            f"<Item id={self._data.id} type={self._data.type}"
            f" name={self._data.name}>"
        )

class ItemCollection(Model):
    _data: BaseItemQueryResult = None

    def __init__(self, collection: BaseItemQueryResult):
        """
        Initializes the ItemCollection class.
        
        Args:
            collection (BaseItemQueryResult): The collection of items.
        """
        self._data = collection
        
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
    
    @property
    def total(self) -> int:
        """
        Returns the total number of records in the collection.

        Returns:
            int: The total number of records.
        """
        if self._data is None:
            return 0
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
        return self._data.start_index

    def first(self, attr: str, value: Any) -> Item | None:
        """
        Returns the first item that matches the specified attribute and value.
        
        Args:
            attr (str): The attribute to search by.
            value (Any): The value to match.
        """
        if self._data is None:
            return None
        
        for item in self._data.items:            
            if getattr(item, attr, None) == value:
                return Item(item)
            
        return None
    
    def __repr__(self) -> str:
        return (f"<ItemCollection total={self.total} start_index={self.index}>")

class Items():
    def __init__(self, items_api: object):
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
        return self.filter()

    @property
    def filter(self) -> object:
        """
        Returns a filtered list of items.

        Returns:
            ItemsApi.get_items: A filtered list of items.
        """
        return self.items_api.get_items