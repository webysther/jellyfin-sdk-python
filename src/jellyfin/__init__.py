"""
Entrypoint module for the Jellyfin SDK.
"""

from jellyfin.api import Api
from jellyfin.items import Items
from jellyfin.image import Image
from jellyfin.system import System
from jellyfin.users import Users
from jellyfin.generated import Version, Proxy

def api(url: str, api_key: str, version: Version = Version.V10_10) -> Api:
    """
    Create an instance of the Jellyfin API client.

    Args:
        url (str): The base URL of the Jellyfin server.
        api_key (str): The API key for authentication.
        version (Version): The API version to use (default is Version.V10_10).

    Returns:
        Api: An instance of the Api class.
    """
    return Api(url, api_key, version)

version = Version

__all__ = [
    'api',
    'version', 
    'Api', 
    'Items', 
    'Image', 
    'System', 
    'Users', 
    'Version', 
    'Proxy'
]