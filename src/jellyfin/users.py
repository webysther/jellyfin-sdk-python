"""
Module `user` - High-level interface for UserApi and UserViewsApi.
"""
from __future__ import annotations

from typing import Callable
from typing_extensions import Self

import uuid

from jellyfin.base import Model, Collection
from jellyfin.items import ItemCollection, Item
from jellyfin.generated import (
    BaseItemKind,
    UserApi, 
    UserViewsApi
)

class User(Model):
    pass

class UserCollection(Collection):
    _factory: Callable = User

class Users():
    _user = None

    def __init__(self, api: Api):
        """Initializes the User API wrapper.

        Args:
            api (Api): An instance of the Api class.
        """
        self._user_api = api.generated.UserApi(api.client)
        self._user_views_api = api.generated.UserViewsApi(api.client)

    def of(self, user_name_or_uuid: str | uuid.UUID) -> Self:
        """Set user context
        
        Args:
            user_name_or_uuid (str | uuid.UUID): The UUID or name of the user.

        Raises:
            ValueError: If the provided user_name_or_uuid is not a valid UUID or name.

        Returns:
            User: The current User instance with the user context set.
        """
        try:
            if isinstance(user_name_or_uuid, uuid.UUID):
                self._user = self.by_id(user_name_or_uuid)
                return self
        except ValueError:
            raise ValueError(f"Not found UUID: {user_name_or_uuid}")
        try:
            self._user = self.by_name(user_name_or_uuid)
            return self

            self._user = self.by_id(uuid.UUID(user_name_or_uuid))
            warnings.warn("User UUID need to be a UUID object.")
        except Exception:
            raise ValueError(f"Not found user: {user_name_or_uuid}")

        return self
    
    def by_id(self, user_id: uuid.UUID) -> User:
        """Get user by ID
        
        Args:
            user_id (uuid.UUID): The UUID of the user.
        
        Returns:
            User: The user object if found.
        """
        return User(self._user_api.get_user_by_id(user_id=user_id))

    def by_name(self, user_name: str) -> User | None:
        """Get user by name
        
        Args:
            user_name (str): The name of the user.
            
        Returns:
            User | None: The user object if found, otherwise None.
        """
        for user in self.all:
            if user.model.name == user_name:
                return user
        return None
    
    @property
    def all(self) -> UserCollection:
        """Get all users.
        
        Returns:
            UserCollection: A list of all users.
        """
        return UserCollection(self._user_api.get_users())

    @property
    def libraries(self) -> ItemCollection:
        """Get libraries for the current user context.
        
        Returns:
            ItemCollection: A list of libraries.
        """
        views = self.views
        filtered_items = [
            item for item in views.data
            if item.type in [BaseItemKind.COLLECTIONFOLDER.value]
        ]
        return ItemCollection(filtered_items)

    @property
    def views(self) -> ItemCollection:
        """Get views for the current user context.
        
        Raises:
            ValueError: If user ID is not set.

        Returns:
            ItemCollection: A list of libraries.
        """
        if self._user is None:
            raise ValueError("User ID is not set. Use the 'of(user_id)' method to set the user context.")

        user_views = self._user_views_api.get_user_views(
            user_id=self._user.id
        )
        return ItemCollection(Item(user_views))
    
    def __repr__(self):
        """String representation of the Users instance."""
        if self._user is None:
            return f"<{self.__class__.__name__} (no user context)>"

        return self._user.__repr__()

    def __getattr__(self, name):
        """Delegate attribute access to user_api, user_views_api, or the current user object."""
        if hasattr(self._user_api, name):
            return getattr(self._user_api, name)
        if hasattr(self._user_views_api, name):
            return getattr(self._user_views_api, name)
        if self._user is not None:
            if hasattr(self._user, name):
                return getattr(self._user, name)
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")