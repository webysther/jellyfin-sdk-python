from enum import Enum
import importlib
from .system import System

class ApiVersion(Enum):
    V10_10 = "api_10_10"
    V10_11 = "api_10_11"
    
class ApiModule():
    @staticmethod
    def get(version: ApiVersion):
        module_name = f"jellyfin.generated.{version.value}"
        return importlib.import_module(module_name)

class Api:
    _system = None
    
    def __init__(self, url, api_key, version: ApiVersion = ApiVersion.V10_10):
        self.url = url
        self.api_key = api_key
        self.version = version
        self._module = ApiModule.get(self.version)

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