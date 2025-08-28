# jellyfin.generated.api_10_10.TrickplayApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_trickplay_hls_playlist**](TrickplayApi.md#get_trickplay_hls_playlist) | **GET** /Videos/{itemId}/Trickplay/{width}/tiles.m3u8 | Gets an image tiles playlist for trickplay.
[**get_trickplay_tile_image**](TrickplayApi.md#get_trickplay_tile_image) | **GET** /Videos/{itemId}/Trickplay/{width}/{index}.jpg | Gets a trickplay tile image.


# **get_trickplay_hls_playlist**
> bytearray get_trickplay_hls_playlist(item_id, width, media_source_id=media_source_id)

Gets an image tiles playlist for trickplay.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jellyfin.generated.api_10_10.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: CustomAuthentication
configuration.api_key['CustomAuthentication'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CustomAuthentication'] = 'Bearer'

# Enter a context with an instance of the API client
with jellyfin.generated.api_10_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jellyfin.generated.api_10_10.TrickplayApi(api_client)
    item_id = 'item_id_example' # str | The item id.
    width = 56 # int | The width of a single tile.
    media_source_id = 'media_source_id_example' # str | The media version id, if using an alternate version. (optional)

    try:
        # Gets an image tiles playlist for trickplay.
        api_response = api_instance.get_trickplay_hls_playlist(item_id, width, media_source_id=media_source_id)
        print("The response of TrickplayApi->get_trickplay_hls_playlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrickplayApi->get_trickplay_hls_playlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **width** | **int**| The width of a single tile. | 
 **media_source_id** | **str**| The media version id, if using an alternate version. | [optional] 

### Return type

**bytearray**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-mpegURL, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tiles playlist returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trickplay_tile_image**
> bytearray get_trickplay_tile_image(item_id, width, index, media_source_id=media_source_id)

Gets a trickplay tile image.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jellyfin.generated.api_10_10.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: CustomAuthentication
configuration.api_key['CustomAuthentication'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CustomAuthentication'] = 'Bearer'

# Enter a context with an instance of the API client
with jellyfin.generated.api_10_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jellyfin.generated.api_10_10.TrickplayApi(api_client)
    item_id = 'item_id_example' # str | The item id.
    width = 56 # int | The width of a single tile.
    index = 56 # int | The index of the desired tile.
    media_source_id = 'media_source_id_example' # str | The media version id, if using an alternate version. (optional)

    try:
        # Gets a trickplay tile image.
        api_response = api_instance.get_trickplay_tile_image(item_id, width, index, media_source_id=media_source_id)
        print("The response of TrickplayApi->get_trickplay_tile_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrickplayApi->get_trickplay_tile_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **width** | **int**| The width of a single tile. | 
 **index** | **int**| The index of the desired tile. | 
 **media_source_id** | **str**| The media version id, if using an alternate version. | [optional] 

### Return type

**bytearray**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tile image not found at specified index. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

