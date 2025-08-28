# jellyfin.generated.api_10_10.FilterApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_query_filters**](FilterApi.md#get_query_filters) | **GET** /Items/Filters2 | Gets query filters.
[**get_query_filters_legacy**](FilterApi.md#get_query_filters_legacy) | **GET** /Items/Filters | Gets legacy query filters.


# **get_query_filters**
> QueryFilters get_query_filters(user_id=user_id, parent_id=parent_id, include_item_types=include_item_types, is_airing=is_airing, is_movie=is_movie, is_sports=is_sports, is_kids=is_kids, is_news=is_news, is_series=is_series, recursive=recursive)

Gets query filters.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.base_item_kind import BaseItemKind
from jellyfin.generated.api_10_10.models.query_filters import QueryFilters
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
    api_instance = jellyfin.generated.api_10_10.FilterApi(api_client)
    user_id = 'user_id_example' # str | Optional. User id. (optional)
    parent_id = 'parent_id_example' # str | Optional. Specify this to localize the search to a specific item or folder. Omit to use the root. (optional)
    include_item_types = [jellyfin.generated.api_10_10.BaseItemKind()] # List[BaseItemKind] | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited. (optional)
    is_airing = True # bool | Optional. Is item airing. (optional)
    is_movie = True # bool | Optional. Is item movie. (optional)
    is_sports = True # bool | Optional. Is item sports. (optional)
    is_kids = True # bool | Optional. Is item kids. (optional)
    is_news = True # bool | Optional. Is item news. (optional)
    is_series = True # bool | Optional. Is item series. (optional)
    recursive = True # bool | Optional. Search recursive. (optional)

    try:
        # Gets query filters.
        api_response = api_instance.get_query_filters(user_id=user_id, parent_id=parent_id, include_item_types=include_item_types, is_airing=is_airing, is_movie=is_movie, is_sports=is_sports, is_kids=is_kids, is_news=is_news, is_series=is_series, recursive=recursive)
        print("The response of FilterApi->get_query_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilterApi->get_query_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Optional. User id. | [optional] 
 **parent_id** | **str**| Optional. Specify this to localize the search to a specific item or folder. Omit to use the root. | [optional] 
 **include_item_types** | [**List[BaseItemKind]**](BaseItemKind.md)| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited. | [optional] 
 **is_airing** | **bool**| Optional. Is item airing. | [optional] 
 **is_movie** | **bool**| Optional. Is item movie. | [optional] 
 **is_sports** | **bool**| Optional. Is item sports. | [optional] 
 **is_kids** | **bool**| Optional. Is item kids. | [optional] 
 **is_news** | **bool**| Optional. Is item news. | [optional] 
 **is_series** | **bool**| Optional. Is item series. | [optional] 
 **recursive** | **bool**| Optional. Search recursive. | [optional] 

### Return type

[**QueryFilters**](QueryFilters.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Filters retrieved. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_query_filters_legacy**
> QueryFiltersLegacy get_query_filters_legacy(user_id=user_id, parent_id=parent_id, include_item_types=include_item_types, media_types=media_types)

Gets legacy query filters.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.base_item_kind import BaseItemKind
from jellyfin.generated.api_10_10.models.media_type import MediaType
from jellyfin.generated.api_10_10.models.query_filters_legacy import QueryFiltersLegacy
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
    api_instance = jellyfin.generated.api_10_10.FilterApi(api_client)
    user_id = 'user_id_example' # str | Optional. User id. (optional)
    parent_id = 'parent_id_example' # str | Optional. Parent id. (optional)
    include_item_types = [jellyfin.generated.api_10_10.BaseItemKind()] # List[BaseItemKind] | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited. (optional)
    media_types = [jellyfin.generated.api_10_10.MediaType()] # List[MediaType] | Optional. Filter by MediaType. Allows multiple, comma delimited. (optional)

    try:
        # Gets legacy query filters.
        api_response = api_instance.get_query_filters_legacy(user_id=user_id, parent_id=parent_id, include_item_types=include_item_types, media_types=media_types)
        print("The response of FilterApi->get_query_filters_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilterApi->get_query_filters_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Optional. User id. | [optional] 
 **parent_id** | **str**| Optional. Parent id. | [optional] 
 **include_item_types** | [**List[BaseItemKind]**](BaseItemKind.md)| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited. | [optional] 
 **media_types** | [**List[MediaType]**](MediaType.md)| Optional. Filter by MediaType. Allows multiple, comma delimited. | [optional] 

### Return type

[**QueryFiltersLegacy**](QueryFiltersLegacy.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Legacy filters retrieved. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

