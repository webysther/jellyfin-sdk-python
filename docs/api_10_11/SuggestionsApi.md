# jellyfin.generated.api_10_11.SuggestionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_suggestions**](SuggestionsApi.md#get_suggestions) | **GET** /Items/Suggestions | Gets suggestions.


# **get_suggestions**
> BaseItemDtoQueryResult get_suggestions(user_id=user_id, media_type=media_type, type=type, start_index=start_index, limit=limit, enable_total_record_count=enable_total_record_count)

Gets suggestions.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.base_item_dto_query_result import BaseItemDtoQueryResult
from jellyfin.generated.api_10_11.models.base_item_kind import BaseItemKind
from jellyfin.generated.api_10_11.models.media_type import MediaType
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
    api_instance = jellyfin.generated.api_10_11.SuggestionsApi(api_client)
    user_id = 'user_id_example' # str | The user id. (optional)
    media_type = [jellyfin.generated.api_10_11.MediaType()] # List[MediaType] | The media types. (optional)
    type = [jellyfin.generated.api_10_11.BaseItemKind()] # List[BaseItemKind] | The type. (optional)
    start_index = 56 # int | Optional. The start index. (optional)
    limit = 56 # int | Optional. The limit. (optional)
    enable_total_record_count = False # bool | Whether to enable the total record count. (optional) (default to False)

    try:
        # Gets suggestions.
        api_response = api_instance.get_suggestions(user_id=user_id, media_type=media_type, type=type, start_index=start_index, limit=limit, enable_total_record_count=enable_total_record_count)
        print("The response of SuggestionsApi->get_suggestions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuggestionsApi->get_suggestions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user id. | [optional] 
 **media_type** | [**List[MediaType]**](MediaType.md)| The media types. | [optional] 
 **type** | [**List[BaseItemKind]**](BaseItemKind.md)| The type. | [optional] 
 **start_index** | **int**| Optional. The start index. | [optional] 
 **limit** | **int**| Optional. The limit. | [optional] 
 **enable_total_record_count** | **bool**| Whether to enable the total record count. | [optional] [default to False]

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Suggestions returned. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

