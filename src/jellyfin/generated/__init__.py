import importlib
from enum import Enum

class Version(Enum):
    """Enumeration of supported Jellyfin API versions."""
    V10_10 = "10.10"
    V10_11 = "10.11"

class Proxy:
    current = Version.V10_10
    modules = {}

    @classmethod
    @property
    def default(cls):
        """Dynamically imports the appropriate API module based on the specified version."""
        return cls.module(cls.current)

    @classmethod
    def name(cls, version: Version) -> str:
        """Returns the API module name for the specified version."""
        module_target = version.value.replace('.', '_')
        return f"jellyfin.generated.api_{module_target}"

    @classmethod
    def module(cls, version: Version):
        """Dynamically imports and returns the appropriate API module based on the specified version."""
        return importlib.import_module(cls.name(version))
    
    @classmethod
    def factory(cls, name, version: Version):
        """Factory method to get a class or function from the specified version module."""
        if cls.name(version) not in cls.modules:
            cls.modules[cls.name(version)] = cls.module(version)

        return getattr(cls.modules[cls.name(version)], name)

def __getattr__(name):
    """Dynamically fetch attributes from the default API version module."""
    try:
        return Proxy.factory(name, Proxy.current)
    except AttributeError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# auto-completion support
def __dir__():
    return list(globals().keys()) + dir(Proxy.default)