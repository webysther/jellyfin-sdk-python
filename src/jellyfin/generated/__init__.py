import importlib
from enum import Enum

class Version(Enum):
    """Enumeration of supported Jellyfin API versions."""
    V10_10 = "10.10"
    V10_11 = "10.11"

class Proxy:
    _VERSION = Version.V10_10

    @property
    def current(self) -> Version:
        return self._VERSION

    @classmethod
    @current.setter
    def current(cls, version: Version):
        """Set the default API version for dynamic imports."""
        cls._VERSION = version

    @classmethod
    @property
    def default(cls):
        """Dynamically imports the appropriate API module based on the specified version."""
        return cls.module(cls._VERSION)

    @classmethod
    def module(cls, version: Version):
        """Dynamically imports and returns the appropriate API module based on the specified version."""
        module_target = version.value.replace('.', '_')
        module_name = f"jellyfin.generated.api_{module_target}"
        return importlib.import_module(module_name)
    
    @classmethod
    def factory(cls, name, version: Version):
        """Factory method to get a class or function from the specified version module."""
        return getattr(cls.module(version), name)

def __getattr__(name):
    """Dynamically fetch attributes from the default API version module."""
    try:
        return getattr(Proxy.default, name)
    except AttributeError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# auto-completion support
def __dir__():
    return list(globals().keys()) + dir(Proxy.default)