import importlib
from enum import Enum

class ServerVersion(Enum):
    """Enumeration of supported Jellyfin API versions."""
    V10_10 = "10.10"
    V10_11 = "10.11"

class ProxyVersion:
    _VERSION = ServerVersion.V10_10

    def __repr__(self):
        return f"<ProxyVersion current='{self._VERSION.value}'>"
    
    def __str__(self):
        return self._VERSION.value

    @property
    def current(self) -> ServerVersion:
        return self._VERSION

    @classmethod
    @current.setter
    def current(cls, version: ServerVersion):
        """Set the default API version for dynamic imports."""
        cls._VERSION = version

    @classmethod
    @property
    def module(cls):
        """Dynamically imports the appropriate API module based on the specified version."""
        module_target = cls._VERSION.value.replace('.', '_')
        module_name = f"jellyfin.generated.api_{module_target}"
        return importlib.import_module(module_name)

def __getattr__(name):
    """Dynamically fetch attributes from the default API version module."""
    try:
        return getattr(ProxyVersion.module, name)
    except AttributeError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# auto-completion support
def __dir__():
    return list(globals().keys()) + dir(ProxyVersion.module)