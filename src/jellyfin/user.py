"""
Module `user` - High-level interface for UserAPI and UserViewsAPI.
"""

import uuid

class User:
    _user_uuid = None

    def __init__(self, user_api: object, user_views_api: object):
        """Initializes the User API wrapper.

        Args:
            user_api (object): An instance of the generated UserApi class.
            user_views_api (object): An instance of the generated UserViewsApi class.
        """
        self.user_api = user_api
        self.user_views_api = user_views_api

    def of(self, user_uuid: str | uuid.UUID) -> 'User':
        """Set user context
        
        Args:
            user_uuid (str | uuid.UUID): The UUID or name of the user.
        
        Raises:
            ValueError: If the provided user_uuid is not a valid UUID or name.
            
        Returns:
            User: The current User instance with the user context set.
        """
        if isinstance(user_uuid, uuid.UUID):
            user_uuid = user_uuid.hex
        self._user_uuid = user_uuid
        
        user = self.by_name(user_uuid)
        if user is not None:
            self._user_uuid = user.id.hex
            return self

        try:
            user = self.by_id(uuid.UUID(user_uuid))
        except ValueError:
            raise ValueError(f"Invalid or Not found UUID/Name for user: {user_uuid}")
            
        if user is not None:
            self._user_uuid = user.id.hex
            return self

        return self
    
    def by_id(self, user_id: uuid.UUID) -> object:
        """Get user by ID
        
        Args:
            user_id (uuid.UUID): The UUID of the user.
        
        Returns:
            UserDto: The user object if found.
        """
        return self.user_api.get_user_by_id(user_id=user_id)

    def by_name(self, user_name: str, sensitive: bool = False):
        """Get user by name"""
        if sensitive is False:
            user_name = user_name.lower()
        
        for user in self.all:
            current_name = user.name
            if sensitive is False:
                current_name = current_name.lower()
            if current_name == user_name:
                return user
        return None

    @property
    def users(self) -> object:
        """Get all users.
        
        Returns:
            UserApi.get_users: A list of all users.
        """
        return self.user_api.get_users
    
    @property
    def all(self) -> object:
        """Get all users. Alias for users
        
        Returns:
            UserApi.get_users: A list of all users.
        """
        return self.users()

    @property
    def libraries(self) -> object:
        """Get libraries. Alias for views
        
        Returns:
            BaseItemDtoQueryResult: A list of libraries.
        """
        return self.views

    @property
    def views(self) -> object:
        """Get libraries for the current user context.
        
        Raises:
            ValueError: If user ID is not set.

        Returns:
            BaseItemDtoQueryResult: A list of libraries.
        """
        if self._user_uuid is None:
            raise ValueError("User ID is not set. Use the 'of(user_id)' method to set the user context.")
        
        return self.user_views_api.get_user_views(user_id=self._user_uuid)
    
    def get_libraries(user_id: str | uuid.UUID) -> object:
        """Get libraries for a specific user.
        
        Args:
            user_id (str | uuid.UUID): The UUID of the user.
        
        Returns:
            BaseItemDtoQueryResult: A list of libraries.
        """
        return self.of(user_id).libraries
    
    def __getattr__(self, name):
        """Delegate attribute access to user_api, user_views_api, or the current user object."""
        if hasattr(self.user_api, name):
            return getattr(self.user_api, name)
        if hasattr(self.user_views_api, name):
            return getattr(self.user_views_api, name)
        if self._user_uuid is not None:
            user = self.by_id(uuid.UUID(self._user_uuid))
            if hasattr(user, name):
                return getattr(user, name)
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")