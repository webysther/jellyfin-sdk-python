# jellyfin.generated.api_10_11.ChannelsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_channel_features**](ChannelsApi.md#get_all_channel_features) | **GET** /Channels/Features | Get all channel features.
[**get_channel_features**](ChannelsApi.md#get_channel_features) | **GET** /Channels/{channelId}/Features | Get channel features.
[**get_channel_items**](ChannelsApi.md#get_channel_items) | **GET** /Channels/{channelId}/Items | Get channel items.
[**get_channels**](ChannelsApi.md#get_channels) | **GET** /Channels | Gets available channels.
[**get_latest_channel_items**](ChannelsApi.md#get_latest_channel_items) | **GET** /Channels/Items/Latest | Gets latest channel items.


# **get_all_channel_features**
> List[ChannelFeatures] get_all_channel_features()

Get all channel features.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.channel_features import ChannelFeatures
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
    api_instance = jellyfin.generated.api_10_11.ChannelsApi(api_client)

    try:
        # Get all channel features.
        api_response = api_instance.get_all_channel_features()
        print("The response of ChannelsApi->get_all_channel_features:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->get_all_channel_features: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ChannelFeatures]**](ChannelFeatures.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All channel features returned. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_features**
> ChannelFeatures get_channel_features(channel_id)

Get channel features.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.channel_features import ChannelFeatures
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
    api_instance = jellyfin.generated.api_10_11.ChannelsApi(api_client)
    channel_id = 'channel_id_example' # str | Channel id.

    try:
        # Get channel features.
        api_response = api_instance.get_channel_features(channel_id)
        print("The response of ChannelsApi->get_channel_features:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->get_channel_features: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Channel id. | 

### Return type

[**ChannelFeatures**](ChannelFeatures.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Channel features returned. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_items**
> BaseItemDtoQueryResult get_channel_items(channel_id, folder_id=folder_id, user_id=user_id, start_index=start_index, limit=limit, sort_order=sort_order, filters=filters, sort_by=sort_by, fields=fields)

Get channel items.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.base_item_dto_query_result import BaseItemDtoQueryResult
from jellyfin.generated.api_10_11.models.item_fields import ItemFields
from jellyfin.generated.api_10_11.models.item_filter import ItemFilter
from jellyfin.generated.api_10_11.models.item_sort_by import ItemSortBy
from jellyfin.generated.api_10_11.models.sort_order import SortOrder
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
    api_instance = jellyfin.generated.api_10_11.ChannelsApi(api_client)
    channel_id = 'channel_id_example' # str | Channel Id.
    folder_id = 'folder_id_example' # str | Optional. Folder Id. (optional)
    user_id = 'user_id_example' # str | Optional. User Id. (optional)
    start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
    limit = 56 # int | Optional. The maximum number of records to return. (optional)
    sort_order = [jellyfin.generated.api_10_11.SortOrder()] # List[SortOrder] | Optional. Sort Order - Ascending,Descending. (optional)
    filters = [jellyfin.generated.api_10_11.ItemFilter()] # List[ItemFilter] | Optional. Specify additional filters to apply. (optional)
    sort_by = [jellyfin.generated.api_10_11.ItemSortBy()] # List[ItemSortBy] | Optional. Specify one or more sort orders, comma delimited. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime. (optional)
    fields = [jellyfin.generated.api_10_11.ItemFields()] # List[ItemFields] | Optional. Specify additional fields of information to return in the output. (optional)

    try:
        # Get channel items.
        api_response = api_instance.get_channel_items(channel_id, folder_id=folder_id, user_id=user_id, start_index=start_index, limit=limit, sort_order=sort_order, filters=filters, sort_by=sort_by, fields=fields)
        print("The response of ChannelsApi->get_channel_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->get_channel_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Channel Id. | 
 **folder_id** | **str**| Optional. Folder Id. | [optional] 
 **user_id** | **str**| Optional. User Id. | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return. | [optional] 
 **sort_order** | [**List[SortOrder]**](SortOrder.md)| Optional. Sort Order - Ascending,Descending. | [optional] 
 **filters** | [**List[ItemFilter]**](ItemFilter.md)| Optional. Specify additional filters to apply. | [optional] 
 **sort_by** | [**List[ItemSortBy]**](ItemSortBy.md)| Optional. Specify one or more sort orders, comma delimited. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime. | [optional] 
 **fields** | [**List[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. | [optional] 

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
**200** | Channel items returned. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channels**
> BaseItemDtoQueryResult get_channels(user_id=user_id, start_index=start_index, limit=limit, supports_latest_items=supports_latest_items, supports_media_deletion=supports_media_deletion, is_favorite=is_favorite)

Gets available channels.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.base_item_dto_query_result import BaseItemDtoQueryResult
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
    api_instance = jellyfin.generated.api_10_11.ChannelsApi(api_client)
    user_id = 'user_id_example' # str | User Id to filter by. Use System.Guid.Empty to not filter by user. (optional)
    start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
    limit = 56 # int | Optional. The maximum number of records to return. (optional)
    supports_latest_items = True # bool | Optional. Filter by channels that support getting latest items. (optional)
    supports_media_deletion = True # bool | Optional. Filter by channels that support media deletion. (optional)
    is_favorite = True # bool | Optional. Filter by channels that are favorite. (optional)

    try:
        # Gets available channels.
        api_response = api_instance.get_channels(user_id=user_id, start_index=start_index, limit=limit, supports_latest_items=supports_latest_items, supports_media_deletion=supports_media_deletion, is_favorite=is_favorite)
        print("The response of ChannelsApi->get_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->get_channels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id to filter by. Use System.Guid.Empty to not filter by user. | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return. | [optional] 
 **supports_latest_items** | **bool**| Optional. Filter by channels that support getting latest items. | [optional] 
 **supports_media_deletion** | **bool**| Optional. Filter by channels that support media deletion. | [optional] 
 **is_favorite** | **bool**| Optional. Filter by channels that are favorite. | [optional] 

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
**200** | Channels returned. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_channel_items**
> BaseItemDtoQueryResult get_latest_channel_items(user_id=user_id, start_index=start_index, limit=limit, filters=filters, fields=fields, channel_ids=channel_ids)

Gets latest channel items.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.base_item_dto_query_result import BaseItemDtoQueryResult
from jellyfin.generated.api_10_11.models.item_fields import ItemFields
from jellyfin.generated.api_10_11.models.item_filter import ItemFilter
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
    api_instance = jellyfin.generated.api_10_11.ChannelsApi(api_client)
    user_id = 'user_id_example' # str | Optional. User Id. (optional)
    start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
    limit = 56 # int | Optional. The maximum number of records to return. (optional)
    filters = [jellyfin.generated.api_10_11.ItemFilter()] # List[ItemFilter] | Optional. Specify additional filters to apply. (optional)
    fields = [jellyfin.generated.api_10_11.ItemFields()] # List[ItemFields] | Optional. Specify additional fields of information to return in the output. (optional)
    channel_ids = ['channel_ids_example'] # List[str] | Optional. Specify one or more channel id's, comma delimited. (optional)

    try:
        # Gets latest channel items.
        api_response = api_instance.get_latest_channel_items(user_id=user_id, start_index=start_index, limit=limit, filters=filters, fields=fields, channel_ids=channel_ids)
        print("The response of ChannelsApi->get_latest_channel_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->get_latest_channel_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Optional. User Id. | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return. | [optional] 
 **filters** | [**List[ItemFilter]**](ItemFilter.md)| Optional. Specify additional filters to apply. | [optional] 
 **fields** | [**List[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. | [optional] 
 **channel_ids** | [**List[str]**](str.md)| Optional. Specify one or more channel id&#39;s, comma delimited. | [optional] 

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
**200** | Latest channel items returned. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

