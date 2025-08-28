# jellyfin.generated.api_10_11.ItemRefreshApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**refresh_item**](ItemRefreshApi.md#refresh_item) | **POST** /Items/{itemId}/Refresh | Refreshes metadata for an item.


# **refresh_item**
> refresh_item(item_id, metadata_refresh_mode=metadata_refresh_mode, image_refresh_mode=image_refresh_mode, replace_all_metadata=replace_all_metadata, replace_all_images=replace_all_images, regenerate_trickplay=regenerate_trickplay)

Refreshes metadata for an item.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jellyfin.generated.api_10_11.Configuration(
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
with jellyfin.generated.api_10_11.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jellyfin.generated.api_10_11.ItemRefreshApi(api_client)
    item_id = 'item_id_example' # str | Item id.
    metadata_refresh_mode = None # MetadataRefreshMode | (Optional) Specifies the metadata refresh mode. (optional) (default to None)
    image_refresh_mode = None # MetadataRefreshMode | (Optional) Specifies the image refresh mode. (optional) (default to None)
    replace_all_metadata = False # bool | (Optional) Determines if metadata should be replaced. Only applicable if mode is FullRefresh. (optional) (default to False)
    replace_all_images = False # bool | (Optional) Determines if images should be replaced. Only applicable if mode is FullRefresh. (optional) (default to False)
    regenerate_trickplay = False # bool | (Optional) Determines if trickplay images should be replaced. Only applicable if mode is FullRefresh. (optional) (default to False)

    try:
        # Refreshes metadata for an item.
        api_instance.refresh_item(item_id, metadata_refresh_mode=metadata_refresh_mode, image_refresh_mode=image_refresh_mode, replace_all_metadata=replace_all_metadata, replace_all_images=replace_all_images, regenerate_trickplay=regenerate_trickplay)
    except Exception as e:
        print("Exception when calling ItemRefreshApi->refresh_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item id. | 
 **metadata_refresh_mode** | **MetadataRefreshMode**| (Optional) Specifies the metadata refresh mode. | [optional] [default to None]
 **image_refresh_mode** | **MetadataRefreshMode**| (Optional) Specifies the image refresh mode. | [optional] [default to None]
 **replace_all_metadata** | **bool**| (Optional) Determines if metadata should be replaced. Only applicable if mode is FullRefresh. | [optional] [default to False]
 **replace_all_images** | **bool**| (Optional) Determines if images should be replaced. Only applicable if mode is FullRefresh. | [optional] [default to False]
 **regenerate_trickplay** | **bool**| (Optional) Determines if trickplay images should be replaced. Only applicable if mode is FullRefresh. | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Item metadata refresh queued. |  -  |
**404** | Item to refresh not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

