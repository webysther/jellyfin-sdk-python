from enum import Enum
import importlib
from .system import System
from .items import Items
from .user import User

class Version(Enum):
    V10_10 = "10.10"
    V10_11 = "10.11"

class Inject():
    @staticmethod
    def get(version: Version):
        module_target = version.value.replace('.', '_')
        module_name = f"jellyfin.generated.api_{module_target}"
        return importlib.import_module(module_name)

class Api:
    _system = None
    _items = None
    _user = None

    def __init__(self, url, api_key, version: Version = Version.V10_10):
        try:
            version = Version(version)
        except ValueError:
            versions = [v.value for v in Version]
            raise ValueError(f"Unsupported version: {version}. Supported versions are: {versions}")

        self.url = url
        self.api_key = api_key
        self.version = version
        self._module = Inject.get(self.version)

        self.client = self._module.ApiClient(
            self._module.Configuration(host=self.url), 
            header_name='X-Emby-Token', 
            header_value=self.api_key
        )
    
    @property
    def system(self):
        if self._system is None:
            self._system = System(self._module.SystemApi(self.client))
        return self._system

    @property
    def items(self):
        if self._items is None:
            self._items = Items(self._module.ItemsApi(self.client))
        return self._items
    
    @property
    def user(self):
        if self._user is None:
            self._user = User(self._module.UserViewsApi(self.client))
        return self._user