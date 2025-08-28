
class User:
    _user_id = None
    
    def __init__(self, user_views_api):
        self.user_views_api = user_views_api
        
    def of(self, user_id):
        """Set user context"""
        self._user_id = user_id
        return self

    @property
    def libraries(self):
        """Get libraries. Alias for views"""
        return self.views

    @property
    def views(self):
        if self._user_id is None:
            raise ValueError("User ID is not set. Use the 'of(user_id)' method to set the user context.")
        
        return self.user_views_api.get_user_views(user_id=self._user_id)