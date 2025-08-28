import uuid

class User:
    _user_uuid = None

    def __init__(self, user_api, user_views_api):
        self.user_api = user_api
        self.user_views_api = user_views_api
        
    def of(self, user_uuid:str|uuid.UUID):
        """Set user context"""
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
    
    def by_id(self, user_id):
        """Get user by ID"""
        return self.user_api.get_user_by_id(user_id=user_id)

    def by_name(self, user_name, sensitive=False):
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
    def users(self):
        """Get all users. Alias for all"""
        return self.user_api.get_users
    
    @property
    def all(self):
        """Get all users"""
        return self.users()

    @property
    def libraries(self):
        """Get libraries. Alias for views"""
        return self.views

    @property
    def views(self):
        if self._user_uuid is None:
            raise ValueError("User ID is not set. Use the 'of(user_id)' method to set the user context.")
        
        return self.user_views_api.get_user_views(user_id=self._user_uuid)
    
    def __getattr__(self, name):
        if hasattr(self.user_api, name):
            return getattr(self.user_api, name)
        if hasattr(self.user_views_api, name):
            return getattr(self.user_views_api, name)
        if self._user_uuid is not None:
            user = self.by_id(uuid.UUID(self._user_uuid))
            if hasattr(user, name):
                return getattr(user, name)
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")