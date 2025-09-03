"""
Entrypoint module for the Jellyfin SDK.
"""

from .api import Api
from .items import Items
from .system import System
from .user import User
from .generated import Version

__all__ = ['Api', 'Items', 'System', 'User', 'Version']

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