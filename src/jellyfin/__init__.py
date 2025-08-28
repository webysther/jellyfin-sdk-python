from .api import Api, Version

def api(url, api_key, version=Version.V10_10) -> Api:
    """
    Create an instance of the Jellyfin API client.
    
    :param url: The base URL of the Jellyfin server.
    :param api_key: The API key for authentication.
    :param version: The API version to use (default is Version.V10_10).
    :return: An instance of the Api class.
    """
    return Api(url, api_key, version)