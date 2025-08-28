# jellyfin.generated.api_10_11.UserViewsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_grouping_options**](UserViewsApi.md#get_grouping_options) | **GET** /UserViews/GroupingOptions | Get user view grouping options.
[**get_user_views**](UserViewsApi.md#get_user_views) | **GET** /UserViews | Get user views.


# **get_grouping_options**
> List[SpecialViewOptionDto] get_grouping_options(user_id=user_id)

Get user view grouping options.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.special_view_option_dto import SpecialViewOptionDto
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
    api_instance = jellyfin.generated.api_10_11.UserViewsApi(api_client)
    user_id = 'user_id_example' # str | User id. (optional)

    try:
        # Get user view grouping options.
        api_response = api_instance.get_grouping_options(user_id=user_id)
        print("The response of UserViewsApi->get_grouping_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserViewsApi->get_grouping_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User id. | [optional] 

### Return type

[**List[SpecialViewOptionDto]**](SpecialViewOptionDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User view grouping options returned. |  -  |
**404** | User not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_views**
> BaseItemDtoQueryResult get_user_views(user_id=user_id, include_external_content=include_external_content, preset_views=preset_views, include_hidden=include_hidden)

Get user views.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.base_item_dto_query_result import BaseItemDtoQueryResult
from jellyfin.generated.api_10_11.models.collection_type import CollectionType
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
    api_instance = jellyfin.generated.api_10_11.UserViewsApi(api_client)
    user_id = 'user_id_example' # str | User id. (optional)
    include_external_content = True # bool | Whether or not to include external views such as channels or live tv. (optional)
    preset_views = [jellyfin.generated.api_10_11.CollectionType()] # List[CollectionType] | Preset views. (optional)
    include_hidden = False # bool | Whether or not to include hidden content. (optional) (default to False)

    try:
        # Get user views.
        api_response = api_instance.get_user_views(user_id=user_id, include_external_content=include_external_content, preset_views=preset_views, include_hidden=include_hidden)
        print("The response of UserViewsApi->get_user_views:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserViewsApi->get_user_views: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User id. | [optional] 
 **include_external_content** | **bool**| Whether or not to include external views such as channels or live tv. | [optional] 
 **preset_views** | [**List[CollectionType]**](CollectionType.md)| Preset views. | [optional] 
 **include_hidden** | **bool**| Whether or not to include hidden content. | [optional] [default to False]

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
**200** | User views returned. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

