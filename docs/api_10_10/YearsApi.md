# jellyfin.generated.api_10_10.YearsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_year**](YearsApi.md#get_year) | **GET** /Years/{year} | Gets a year.
[**get_years**](YearsApi.md#get_years) | **GET** /Years | Get years.


# **get_year**
> BaseItemDto get_year(year, user_id=user_id)

Gets a year.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.base_item_dto import BaseItemDto
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
    api_instance = jellyfin.generated.api_10_10.YearsApi(api_client)
    year = 56 # int | The year.
    user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data. (optional)

    try:
        # Gets a year.
        api_response = api_instance.get_year(year, user_id=user_id)
        print("The response of YearsApi->get_year:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling YearsApi->get_year: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| The year. | 
 **user_id** | **str**| Optional. Filter by user id, and attach user data. | [optional] 

### Return type

[**BaseItemDto**](BaseItemDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Year returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Year not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_years**
> BaseItemDtoQueryResult get_years(start_index=start_index, limit=limit, sort_order=sort_order, parent_id=parent_id, fields=fields, exclude_item_types=exclude_item_types, include_item_types=include_item_types, media_types=media_types, sort_by=sort_by, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, recursive=recursive, enable_images=enable_images)

Get years.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.base_item_dto_query_result import BaseItemDtoQueryResult
from jellyfin.generated.api_10_10.models.base_item_kind import BaseItemKind
from jellyfin.generated.api_10_10.models.image_type import ImageType
from jellyfin.generated.api_10_10.models.item_fields import ItemFields
from jellyfin.generated.api_10_10.models.item_sort_by import ItemSortBy
from jellyfin.generated.api_10_10.models.media_type import MediaType
from jellyfin.generated.api_10_10.models.sort_order import SortOrder
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
    api_instance = jellyfin.generated.api_10_10.YearsApi(api_client)
    start_index = 56 # int | Skips over a given number of items within the results. Use for paging. (optional)
    limit = 56 # int | Optional. The maximum number of records to return. (optional)
    sort_order = [jellyfin.generated.api_10_10.SortOrder()] # List[SortOrder] | Sort Order - Ascending,Descending. (optional)
    parent_id = 'parent_id_example' # str | Specify this to localize the search to a specific item or folder. Omit to use the root. (optional)
    fields = [jellyfin.generated.api_10_10.ItemFields()] # List[ItemFields] | Optional. Specify additional fields of information to return in the output. (optional)
    exclude_item_types = [jellyfin.generated.api_10_10.BaseItemKind()] # List[BaseItemKind] | Optional. If specified, results will be excluded based on item type. This allows multiple, comma delimited. (optional)
    include_item_types = [jellyfin.generated.api_10_10.BaseItemKind()] # List[BaseItemKind] | Optional. If specified, results will be included based on item type. This allows multiple, comma delimited. (optional)
    media_types = [jellyfin.generated.api_10_10.MediaType()] # List[MediaType] | Optional. Filter by MediaType. Allows multiple, comma delimited. (optional)
    sort_by = [jellyfin.generated.api_10_10.ItemSortBy()] # List[ItemSortBy] | Optional. Specify one or more sort orders, comma delimited. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime. (optional)
    enable_user_data = True # bool | Optional. Include user data. (optional)
    image_type_limit = 56 # int | Optional. The max number of images to return, per image type. (optional)
    enable_image_types = [jellyfin.generated.api_10_10.ImageType()] # List[ImageType] | Optional. The image types to include in the output. (optional)
    user_id = 'user_id_example' # str | User Id. (optional)
    recursive = True # bool | Search recursively. (optional) (default to True)
    enable_images = True # bool | Optional. Include image information in output. (optional) (default to True)

    try:
        # Get years.
        api_response = api_instance.get_years(start_index=start_index, limit=limit, sort_order=sort_order, parent_id=parent_id, fields=fields, exclude_item_types=exclude_item_types, include_item_types=include_item_types, media_types=media_types, sort_by=sort_by, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, user_id=user_id, recursive=recursive, enable_images=enable_images)
        print("The response of YearsApi->get_years:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling YearsApi->get_years: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_index** | **int**| Skips over a given number of items within the results. Use for paging. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return. | [optional] 
 **sort_order** | [**List[SortOrder]**](SortOrder.md)| Sort Order - Ascending,Descending. | [optional] 
 **parent_id** | **str**| Specify this to localize the search to a specific item or folder. Omit to use the root. | [optional] 
 **fields** | [**List[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. | [optional] 
 **exclude_item_types** | [**List[BaseItemKind]**](BaseItemKind.md)| Optional. If specified, results will be excluded based on item type. This allows multiple, comma delimited. | [optional] 
 **include_item_types** | [**List[BaseItemKind]**](BaseItemKind.md)| Optional. If specified, results will be included based on item type. This allows multiple, comma delimited. | [optional] 
 **media_types** | [**List[MediaType]**](MediaType.md)| Optional. Filter by MediaType. Allows multiple, comma delimited. | [optional] 
 **sort_by** | [**List[ItemSortBy]**](ItemSortBy.md)| Optional. Specify one or more sort orders, comma delimited. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime. | [optional] 
 **enable_user_data** | **bool**| Optional. Include user data. | [optional] 
 **image_type_limit** | **int**| Optional. The max number of images to return, per image type. | [optional] 
 **enable_image_types** | [**List[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 
 **user_id** | **str**| User Id. | [optional] 
 **recursive** | **bool**| Search recursively. | [optional] [default to True]
 **enable_images** | **bool**| Optional. Include image information in output. | [optional] [default to True]

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Year query returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

