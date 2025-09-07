"""
Module `api` - High-level interface for ApiClient and Configuration.
"""

from enum import Enum
import importlib, socket, platform, uuid, distro
from typing_extensions import Self

from .system import System
from .items import Items, ItemCollection
from .users import Users
from .generated import (
    Version,
    Proxy,
    ApiClient,
    Configuration
)

class Api:
    _system: System = None
    _items: Items = None
    _users: Users = None
    _client = None
    _configuration = None

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
        self.generated = Proxy.module(version)
        self._auth = f'Token="{self.api_key}"'
        
    def __repr__(self):
        """ Official string representation of the Api instance. """
        auth_parts = self._auth.replace(self.api_key, "***").split(", ")
        
        if len(auth_parts) > 1:
            auth = ",\n       ".join(auth_parts)
        else:
            auth = auth_parts[0]
            
        return f"<Api\n url='{self.url}',\n version='{self.version.value}',\n auth='{auth}'\n>"

    def __str__(self):
        """ String representation of the Api instance. """
        return self.__repr__()

    @property
    def configuration(self) -> Configuration:
        """Returns the Configuration instance."""
        if self._configuration is None:
            self._configuration = self.generated.Configuration(
                host=self.url,
                api_key={'CustomAuthentication': self._auth},
                api_key_prefix={'CustomAuthentication': 'MediaBrowser'}
            )
        return self._configuration
    
    @property
    def client(self) -> ApiClient:
        """Returns the ApiClient instance."""
        if self._client is None:
            self._client = self.generated.ApiClient(self.configuration)
            self.generated.ApiClient.set_default(self._client)
        return self._client

    def register_client(self, client_name: str = None, device_name: str = None, device_id: str = None, device_version: str = None) -> Self:
        """Just register this as a client with the server.
        
        Args:
            client_name (str, optional): The name of the client application. Defaults to the hostname if not provided.
            device_name (str, optional): The name of the device. Defaults to the OS name if not provided.
            device_id (str, optional): The unique identifier for the device. Defaults to the MAC address if not provided.
            device_version (str, optional): The version of the client application. Defaults to the OS version if not provided.
            
        Returns:
            Api: The current instance of the Api class.
        """
        hostname = socket.gethostname()
        os_name = platform.system()
        os_version = platform.release()
        
        if platform.system() == "Linux":
            os_name = f"{os_name} {distro.name(pretty=True)} ({distro.codename()})"
            os_version = distro.version(best=True)

        if client_name is None:
            client_name = hostname
        
        if device_name is None:
            device_name = os_name
            
        if device_id is None:
            mac = uuid.getnode()
            device_id = '-'.join(['{:02x}'.format((mac >> ele) & 0xff) for ele in range(40, -1, -8)])
            
        if device_version is None:
            device_version = os_version

        self._auth = f'Token="{self.api_key}", Client="{client_name}", Device="{device_name}"'
        self._auth += f', DeviceId="{device_id}", Version="{device_version}"'
        self._configuration = None
        self._client = None
        
        return self

    @property
    def system(self) -> System:
        """
        Lazy load the System API.
        
        Returns:
            System: An instance of the System API wrapper.
        """
        if self._system is None:
            self._system = System(self.generated.SystemApi(self.client))
        return self._system

    @property
    def items(self) -> Items:
        """
        Lazy load the Items API.
        
        Returns:
            Items: An instance of the Items API wrapper.
        """
        if self._items is None:
            self._items = Items(self.generated.ItemsApi(self.client))
        return self._items
    
    @property
    def libraries(self) -> Items:
        """
        Alias for items of type COLLECTIONFOLDER.
        
        Returns:
            ItemCollection: A collection of all libraries.
        """
        return self.items.search.only_library().all

    @property
    def users(self) -> Users:
        """
        Lazy load the User API.
        
        Returns:
            Users: An instance of the User API wrapper.
        """
        if self._users is None:
            self._users = Users(
                self.generated.UserApi(self.client),
                self.generated.UserViewsApi(self.client)
            )
        return self._users