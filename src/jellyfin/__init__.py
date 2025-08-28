from .api import Api

def api(url, api_key) -> Api:
    return Api(url, api_key)