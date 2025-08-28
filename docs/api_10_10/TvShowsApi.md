# jellyfin.generated.api_10_10.TvShowsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_episodes**](TvShowsApi.md#get_episodes) | **GET** /Shows/{seriesId}/Episodes | Gets episodes for a tv season.
[**get_next_up**](TvShowsApi.md#get_next_up) | **GET** /Shows/NextUp | Gets a list of next up episodes.
[**get_seasons**](TvShowsApi.md#get_seasons) | **GET** /Shows/{seriesId}/Seasons | Gets seasons for a tv series.
[**get_upcoming_episodes**](TvShowsApi.md#get_upcoming_episodes) | **GET** /Shows/Upcoming | Gets a list of upcoming episodes.


# **get_episodes**
> BaseItemDtoQueryResult get_episodes(series_id, user_id=user_id, fields=fields, season=season, season_id=season_id, is_missing=is_missing, adjacent_to=adjacent_to, start_item_id=start_item_id, start_index=start_index, limit=limit, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, enable_user_data=enable_user_data, sort_by=sort_by)

Gets episodes for a tv season.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.base_item_dto_query_result import BaseItemDtoQueryResult
from jellyfin.generated.api_10_10.models.image_type import ImageType
from jellyfin.generated.api_10_10.models.item_fields import ItemFields
from jellyfin.generated.api_10_10.models.item_sort_by import ItemSortBy
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
    api_instance = jellyfin.generated.api_10_10.TvShowsApi(api_client)
    series_id = 'series_id_example' # str | The series id.
    user_id = 'user_id_example' # str | The user id. (optional)
    fields = [jellyfin.generated.api_10_10.ItemFields()] # List[ItemFields] | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls. (optional)
    season = 56 # int | Optional filter by season number. (optional)
    season_id = 'season_id_example' # str | Optional. Filter by season id. (optional)
    is_missing = True # bool | Optional. Filter by items that are missing episodes or not. (optional)
    adjacent_to = 'adjacent_to_example' # str | Optional. Return items that are siblings of a supplied item. (optional)
    start_item_id = 'start_item_id_example' # str | Optional. Skip through the list until a given item is found. (optional)
    start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
    limit = 56 # int | Optional. The maximum number of records to return. (optional)
    enable_images = True # bool | Optional, include image information in output. (optional)
    image_type_limit = 56 # int | Optional, the max number of images to return, per image type. (optional)
    enable_image_types = [jellyfin.generated.api_10_10.ImageType()] # List[ImageType] | Optional. The image types to include in the output. (optional)
    enable_user_data = True # bool | Optional. Include user data. (optional)
    sort_by = jellyfin.generated.api_10_10.ItemSortBy() # ItemSortBy | Optional. Specify one or more sort orders, comma delimited. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime. (optional)

    try:
        # Gets episodes for a tv season.
        api_response = api_instance.get_episodes(series_id, user_id=user_id, fields=fields, season=season, season_id=season_id, is_missing=is_missing, adjacent_to=adjacent_to, start_item_id=start_item_id, start_index=start_index, limit=limit, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, enable_user_data=enable_user_data, sort_by=sort_by)
        print("The response of TvShowsApi->get_episodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TvShowsApi->get_episodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **str**| The series id. | 
 **user_id** | **str**| The user id. | [optional] 
 **fields** | [**List[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls. | [optional] 
 **season** | **int**| Optional filter by season number. | [optional] 
 **season_id** | **str**| Optional. Filter by season id. | [optional] 
 **is_missing** | **bool**| Optional. Filter by items that are missing episodes or not. | [optional] 
 **adjacent_to** | **str**| Optional. Return items that are siblings of a supplied item. | [optional] 
 **start_item_id** | **str**| Optional. Skip through the list until a given item is found. | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output. | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type. | [optional] 
 **enable_image_types** | [**List[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 
 **enable_user_data** | **bool**| Optional. Include user data. | [optional] 
 **sort_by** | [**ItemSortBy**](.md)| Optional. Specify one or more sort orders, comma delimited. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime. | [optional] 

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
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_next_up**
> BaseItemDtoQueryResult get_next_up(user_id=user_id, start_index=start_index, limit=limit, fields=fields, series_id=series_id, parent_id=parent_id, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, enable_user_data=enable_user_data, next_up_date_cutoff=next_up_date_cutoff, enable_total_record_count=enable_total_record_count, disable_first_episode=disable_first_episode, enable_resumable=enable_resumable, enable_rewatching=enable_rewatching)

Gets a list of next up episodes.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.base_item_dto_query_result import BaseItemDtoQueryResult
from jellyfin.generated.api_10_10.models.image_type import ImageType
from jellyfin.generated.api_10_10.models.item_fields import ItemFields
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
    api_instance = jellyfin.generated.api_10_10.TvShowsApi(api_client)
    user_id = 'user_id_example' # str | The user id of the user to get the next up episodes for. (optional)
    start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
    limit = 56 # int | Optional. The maximum number of records to return. (optional)
    fields = [jellyfin.generated.api_10_10.ItemFields()] # List[ItemFields] | Optional. Specify additional fields of information to return in the output. (optional)
    series_id = 'series_id_example' # str | Optional. Filter by series id. (optional)
    parent_id = 'parent_id_example' # str | Optional. Specify this to localize the search to a specific item or folder. Omit to use the root. (optional)
    enable_images = True # bool | Optional. Include image information in output. (optional)
    image_type_limit = 56 # int | Optional. The max number of images to return, per image type. (optional)
    enable_image_types = [jellyfin.generated.api_10_10.ImageType()] # List[ImageType] | Optional. The image types to include in the output. (optional)
    enable_user_data = True # bool | Optional. Include user data. (optional)
    next_up_date_cutoff = '2013-10-20T19:20:30+01:00' # datetime | Optional. Starting date of shows to show in Next Up section. (optional)
    enable_total_record_count = True # bool | Whether to enable the total records count. Defaults to true. (optional) (default to True)
    disable_first_episode = False # bool | Whether to disable sending the first episode in a series as next up. (optional) (default to False)
    enable_resumable = True # bool | Whether to include resumable episodes in next up results. (optional) (default to True)
    enable_rewatching = False # bool | Whether to include watched episodes in next up results. (optional) (default to False)

    try:
        # Gets a list of next up episodes.
        api_response = api_instance.get_next_up(user_id=user_id, start_index=start_index, limit=limit, fields=fields, series_id=series_id, parent_id=parent_id, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, enable_user_data=enable_user_data, next_up_date_cutoff=next_up_date_cutoff, enable_total_record_count=enable_total_record_count, disable_first_episode=disable_first_episode, enable_resumable=enable_resumable, enable_rewatching=enable_rewatching)
        print("The response of TvShowsApi->get_next_up:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TvShowsApi->get_next_up: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user id of the user to get the next up episodes for. | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return. | [optional] 
 **fields** | [**List[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. | [optional] 
 **series_id** | **str**| Optional. Filter by series id. | [optional] 
 **parent_id** | **str**| Optional. Specify this to localize the search to a specific item or folder. Omit to use the root. | [optional] 
 **enable_images** | **bool**| Optional. Include image information in output. | [optional] 
 **image_type_limit** | **int**| Optional. The max number of images to return, per image type. | [optional] 
 **enable_image_types** | [**List[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 
 **enable_user_data** | **bool**| Optional. Include user data. | [optional] 
 **next_up_date_cutoff** | **datetime**| Optional. Starting date of shows to show in Next Up section. | [optional] 
 **enable_total_record_count** | **bool**| Whether to enable the total records count. Defaults to true. | [optional] [default to True]
 **disable_first_episode** | **bool**| Whether to disable sending the first episode in a series as next up. | [optional] [default to False]
 **enable_resumable** | **bool**| Whether to include resumable episodes in next up results. | [optional] [default to True]
 **enable_rewatching** | **bool**| Whether to include watched episodes in next up results. | [optional] [default to False]

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
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_seasons**
> BaseItemDtoQueryResult get_seasons(series_id, user_id=user_id, fields=fields, is_special_season=is_special_season, is_missing=is_missing, adjacent_to=adjacent_to, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, enable_user_data=enable_user_data)

Gets seasons for a tv series.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.base_item_dto_query_result import BaseItemDtoQueryResult
from jellyfin.generated.api_10_10.models.image_type import ImageType
from jellyfin.generated.api_10_10.models.item_fields import ItemFields
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
    api_instance = jellyfin.generated.api_10_10.TvShowsApi(api_client)
    series_id = 'series_id_example' # str | The series id.
    user_id = 'user_id_example' # str | The user id. (optional)
    fields = [jellyfin.generated.api_10_10.ItemFields()] # List[ItemFields] | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls. (optional)
    is_special_season = True # bool | Optional. Filter by special season. (optional)
    is_missing = True # bool | Optional. Filter by items that are missing episodes or not. (optional)
    adjacent_to = 'adjacent_to_example' # str | Optional. Return items that are siblings of a supplied item. (optional)
    enable_images = True # bool | Optional. Include image information in output. (optional)
    image_type_limit = 56 # int | Optional. The max number of images to return, per image type. (optional)
    enable_image_types = [jellyfin.generated.api_10_10.ImageType()] # List[ImageType] | Optional. The image types to include in the output. (optional)
    enable_user_data = True # bool | Optional. Include user data. (optional)

    try:
        # Gets seasons for a tv series.
        api_response = api_instance.get_seasons(series_id, user_id=user_id, fields=fields, is_special_season=is_special_season, is_missing=is_missing, adjacent_to=adjacent_to, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, enable_user_data=enable_user_data)
        print("The response of TvShowsApi->get_seasons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TvShowsApi->get_seasons: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **str**| The series id. | 
 **user_id** | **str**| The user id. | [optional] 
 **fields** | [**List[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls. | [optional] 
 **is_special_season** | **bool**| Optional. Filter by special season. | [optional] 
 **is_missing** | **bool**| Optional. Filter by items that are missing episodes or not. | [optional] 
 **adjacent_to** | **str**| Optional. Return items that are siblings of a supplied item. | [optional] 
 **enable_images** | **bool**| Optional. Include image information in output. | [optional] 
 **image_type_limit** | **int**| Optional. The max number of images to return, per image type. | [optional] 
 **enable_image_types** | [**List[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 
 **enable_user_data** | **bool**| Optional. Include user data. | [optional] 

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
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upcoming_episodes**
> BaseItemDtoQueryResult get_upcoming_episodes(user_id=user_id, start_index=start_index, limit=limit, fields=fields, parent_id=parent_id, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, enable_user_data=enable_user_data)

Gets a list of upcoming episodes.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.base_item_dto_query_result import BaseItemDtoQueryResult
from jellyfin.generated.api_10_10.models.image_type import ImageType
from jellyfin.generated.api_10_10.models.item_fields import ItemFields
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
    api_instance = jellyfin.generated.api_10_10.TvShowsApi(api_client)
    user_id = 'user_id_example' # str | The user id of the user to get the upcoming episodes for. (optional)
    start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
    limit = 56 # int | Optional. The maximum number of records to return. (optional)
    fields = [jellyfin.generated.api_10_10.ItemFields()] # List[ItemFields] | Optional. Specify additional fields of information to return in the output. (optional)
    parent_id = 'parent_id_example' # str | Optional. Specify this to localize the search to a specific item or folder. Omit to use the root. (optional)
    enable_images = True # bool | Optional. Include image information in output. (optional)
    image_type_limit = 56 # int | Optional. The max number of images to return, per image type. (optional)
    enable_image_types = [jellyfin.generated.api_10_10.ImageType()] # List[ImageType] | Optional. The image types to include in the output. (optional)
    enable_user_data = True # bool | Optional. Include user data. (optional)

    try:
        # Gets a list of upcoming episodes.
        api_response = api_instance.get_upcoming_episodes(user_id=user_id, start_index=start_index, limit=limit, fields=fields, parent_id=parent_id, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, enable_user_data=enable_user_data)
        print("The response of TvShowsApi->get_upcoming_episodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TvShowsApi->get_upcoming_episodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user id of the user to get the upcoming episodes for. | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return. | [optional] 
 **fields** | [**List[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. | [optional] 
 **parent_id** | **str**| Optional. Specify this to localize the search to a specific item or folder. Omit to use the root. | [optional] 
 **enable_images** | **bool**| Optional. Include image information in output. | [optional] 
 **image_type_limit** | **int**| Optional. The max number of images to return, per image type. | [optional] 
 **enable_image_types** | [**List[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 
 **enable_user_data** | **bool**| Optional. Include user data. | [optional] 

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
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

