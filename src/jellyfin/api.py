"""
Module `api` - High-level interface for ApiClient and Configuration.
"""

from enum import Enum
from uuid import UUID
import importlib, socket, platform, uuid, distro
from typing_extensions import Self

from jellyfin.items import ItemCollection
from jellyfin.users import User
from jellyfin.generated import (
    Version,
    Proxy,
    ApiClient,
    Configuration
)

class Api:

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
    def user(self) -> User | None:
        """Returns the user context for the API requests."""
        if hasattr(self, '_user') is False:
            return None
        return self._user

    @user.setter
    def user(self, value: str | uuid.UUID):
        """
        Sets the user context for the API requests.
        
        Args:
            value (str | uuid.UUID): The user to set, either as a username or UUID.
        """
        if isinstance(value, (str, UUID)):
            self._user = self.users.of(value)

    @property
    def configuration(self) -> Configuration:
        """Returns the Configuration instance."""
        if hasattr(self, '_configuration') is False:
            self._configuration = self.generated.Configuration(
                host=self.url,
                api_key={'CustomAuthentication': self._auth},
                api_key_prefix={'CustomAuthentication': 'MediaBrowser'}
            )
        return self._configuration
    
    @property
    def client(self) -> ApiClient:
        """Returns the ApiClient instance."""
        if hasattr(self, '_client') is False:
            self._client = self.generated.ApiClient(self.configuration)
            self.generated.ApiClient.set_default(self._client)
        return self._client

    def register_client(
            self, 
            client_name: str = None, 
            device_name: str = None, 
            device_id: str = None, 
            device_version: str = None
        ) -> Self:
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

        if hasattr(self, '_configuration'):
            del self._configuration
        if hasattr(self, '_client'):
            del self._client

        return self
    
    @property
    def libraries(self) -> ItemCollection:
        """
        Alias for items of type COLLECTIONFOLDER.
        
        Returns:
            ItemCollection: A collection of all libraries.
        """
        return self.items.search.only_library().all
    
    def __getattr__(self, name):
        try:
            private_name = f"_{name}"
            if not hasattr(self, private_name):
                cls = getattr(__import__(__name__), name.capitalize(), None)
                if cls is None:
                    raise AttributeError(f"No class named '{name.capitalize()}' found")
                self.__setattr__(private_name, cls(self))
            return getattr(self, private_name)
        except Exception as e:
            raise AttributeError(f"'Api' object has no attribute '{name}': {e}")