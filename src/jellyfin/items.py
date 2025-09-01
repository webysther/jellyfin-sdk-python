"""
Module `items` - High-level interface for ItemsApi.
"""

from typing import List

class Items:
    def __init__(self, items_api: object):
        """
        Initializes the Items API wrapper.
        
        Args:
            items_api (ItemsApi): An instance of the generated ItemsApi class.
        """
        self.items_api = items_api
        
    @property
    def all(self) -> object:
        """
        Returns all items.
        
        Returns:
            BaseItemDtoQueryResult: A list of all items.
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