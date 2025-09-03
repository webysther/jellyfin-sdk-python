"""
Module `user` - High-level interface for UserApi and UserViewsApi.
"""
from typing import Callable, List
from enum import Enum

from pydantic import BaseModel

import uuid

from .base import Model, Single
from .items import ItemCollection
from .generated import (
    BaseItemKind,
    UserApi, 
    UserViewsApi, 
    UserDto
)

class User(Single):
    _naming: str = "User"

class UserCollection(Model):
    _naming: str = "UserCollection"
    _single: Callable = User
        
    @property
    def items(self) -> List[User]:
        return super().items
    
    @property
    def all(self) -> List[User]:
        return super().all
    
    def first(self, attr: str, value: Any) -> User | None:
        return super().first(attr, value)
    
    def filter(self, criteria: dict, limit: int = None) -> 'UserCollection':
        return super().filter(criteria, limit)

class Users(Model):
    _user = None

    def __init__(self, user_api: UserApi, user_views_api: UserViewsApi):
        """Initializes the User API wrapper.

        Args:
            user_api (UserApi): An instance of the generated UserApi class.
            user_views_api (UserViewsApi): An instance of the generated UserViewsApi class.
        """
        self._user_api = user_api
        self._user_views_api = user_views_api

    def of(self, user_name_or_uuid: str | uuid.UUID) -> 'User':
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
            if user.name == user_name:
                return User(user)
        return None

    @property
    def users(self) -> UserApi.get_users:
        """Get all users.
        
        Returns:
            UserApi.get_users: A list of all users.
        """
        return self._user_api.get_users
    
    @property
    def all(self) -> UserApi.get_users:
        """Get all users. Alias for users
        
        Returns:
            UserApi.get_users: A list of all users.
        """
        return self.users()

    @property
    def libraries(self) -> ItemCollection:
        """Get libraries for the current user context.
        
        Returns:
            ItemCollection: A list of libraries.
        """
        views = self.views
        filtered_items = [
            item for item in views._data.items
            if item.type in [BaseItemKind.COLLECTIONFOLDER.value]
        ]
        views._data.items = filtered_items
        views._data.total_record_count = len(filtered_items)
        return views

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
        return ItemCollection(user_views)
    
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