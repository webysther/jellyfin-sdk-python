"""
Module `api` - High-level interface for ApiClient and Configuration.
"""

from enum import Enum
import importlib
from .system import System
from .items import Items
from .user import User

class Version(Enum):
    """Enumeration of supported Jellyfin API versions."""
    V10_10 = "10.10"
    V10_11 = "10.11"

class Inject():
    @staticmethod
    def get(version: Version):
        """ Dynamically imports the appropriate API module based on the specified version.
        
        Args:
            version (Version): The API version to import.
            
        Returns:
            module: The imported module corresponding to the specified version.
        """
        module_target = version.value.replace('.', '_')
        module_name = f"jellyfin.generated.api_{module_target}"
        return importlib.import_module(module_name)

class Api:
    _system: System = None
    _items: Items = None
    _user: User = None

    def __init__(self, url: str, api_key: str, version: Version = Version.V10_10):
        """Initializes the Jellyfin API client.
    
        Args:
            url (str): The base URL of the Jellyfin server.
            api_key (str): The API key for authentication.
            version (Version): The API version to use (default is Version.V10_10).

        Raises:
            ValueError: If an unsupported version is provided.
        
        Returns:
            Api: An instance of the Api class.
        """
        try:
            version = Version(version)
        except ValueError:
            versions = [v.value for v in Version]
            raise ValueError(f"Unsupported version: {version}. Supported versions are: {versions}")

        self.url = url
        self.api_key = api_key
        self.version = version
        self._module = Inject.get(self.version)
        
        self.configuration = self._module.Configuration(
            host=self.url,
            api_key={'CustomAuthentication': f'Token="{self.api_key}"'}, 
            api_key_prefix={'CustomAuthentication': 'MediaBrowser'}
        )

        self.client = self._module.ApiClient(self.configuration)
    
    @property
    def system(self) -> System:
        """
        Lazy load the System API.
        
        Returns:
            System: An instance of the System API wrapper.
        """
        if self._system is None:
            self._system = System(self._module.SystemApi(self.client))
        return self._system

    @property
    def items(self) -> Items:
        """
        Lazy load the Items API.
        
        Returns:
            Items: An instance of the Items API wrapper.
        """
        if self._items is None:
            self._items = Items(self._module.ItemsApi(self.client))
        return self._items
    
    @property
    def user(self) -> User:
        """
        Lazy load the User API.
        
        Returns:
            User: An instance of the User API wrapper.
        """
        if self._user is None:
            self._user = User(
                self._module.UserApi(self.client),
                self._module.UserViewsApi(self.client)
            )
        return self._user