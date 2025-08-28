# jellyfin.generated.api_10_10.ArtistsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_album_artists**](ArtistsApi.md#get_album_artists) | **GET** /Artists/AlbumArtists | Gets all album artists from a given item, folder, or the entire library.
[**get_artist_by_name**](ArtistsApi.md#get_artist_by_name) | **GET** /Artists/{name} | Gets an artist by name.
[**get_artists**](ArtistsApi.md#get_artists) | **GET** /Artists | Gets all artists from a given item, folder, or the entire library.


# **get_album_artists**
> BaseItemDtoQueryResult get_album_artists(min_community_rating=min_community_rating, start_index=start_index, limit=limit, search_term=search_term, parent_id=parent_id, fields=fields, exclude_item_types=exclude_item_types, include_item_types=include_item_types, filters=filters, is_favorite=is_favorite, media_types=media_types, genres=genres, genre_ids=genre_ids, official_ratings=official_ratings, tags=tags, years=years, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, person=person, person_ids=person_ids, person_types=person_types, studios=studios, studio_ids=studio_ids, user_id=user_id, name_starts_with_or_greater=name_starts_with_or_greater, name_starts_with=name_starts_with, name_less_than=name_less_than, sort_by=sort_by, sort_order=sort_order, enable_images=enable_images, enable_total_record_count=enable_total_record_count)

Gets all album artists from a given item, folder, or the entire library.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.base_item_dto_query_result import BaseItemDtoQueryResult
from jellyfin.generated.api_10_10.models.base_item_kind import BaseItemKind
from jellyfin.generated.api_10_10.models.image_type import ImageType
from jellyfin.generated.api_10_10.models.item_fields import ItemFields
from jellyfin.generated.api_10_10.models.item_filter import ItemFilter
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
    api_instance = jellyfin.generated.api_10_10.ArtistsApi(api_client)
    min_community_rating = 3.4 # float | Optional filter by minimum community rating. (optional)
    start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
    limit = 56 # int | Optional. The maximum number of records to return. (optional)
    search_term = 'search_term_example' # str | Optional. Search term. (optional)
    parent_id = 'parent_id_example' # str | Specify this to localize the search to a specific item or folder. Omit to use the root. (optional)
    fields = [jellyfin.generated.api_10_10.ItemFields()] # List[ItemFields] | Optional. Specify additional fields of information to return in the output. (optional)
    exclude_item_types = [jellyfin.generated.api_10_10.BaseItemKind()] # List[BaseItemKind] | Optional. If specified, results will be filtered out based on item type. This allows multiple, comma delimited. (optional)
    include_item_types = [jellyfin.generated.api_10_10.BaseItemKind()] # List[BaseItemKind] | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited. (optional)
    filters = [jellyfin.generated.api_10_10.ItemFilter()] # List[ItemFilter] | Optional. Specify additional filters to apply. (optional)
    is_favorite = True # bool | Optional filter by items that are marked as favorite, or not. (optional)
    media_types = [jellyfin.generated.api_10_10.MediaType()] # List[MediaType] | Optional filter by MediaType. Allows multiple, comma delimited. (optional)
    genres = ['genres_example'] # List[str] | Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimited. (optional)
    genre_ids = ['genre_ids_example'] # List[str] | Optional. If specified, results will be filtered based on genre id. This allows multiple, pipe delimited. (optional)
    official_ratings = ['official_ratings_example'] # List[str] | Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimited. (optional)
    tags = ['tags_example'] # List[str] | Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimited. (optional)
    years = [56] # List[int] | Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimited. (optional)
    enable_user_data = True # bool | Optional, include user data. (optional)
    image_type_limit = 56 # int | Optional, the max number of images to return, per image type. (optional)
    enable_image_types = [jellyfin.generated.api_10_10.ImageType()] # List[ImageType] | Optional. The image types to include in the output. (optional)
    person = 'person_example' # str | Optional. If specified, results will be filtered to include only those containing the specified person. (optional)
    person_ids = ['person_ids_example'] # List[str] | Optional. If specified, results will be filtered to include only those containing the specified person ids. (optional)
    person_types = ['person_types_example'] # List[str] | Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited. (optional)
    studios = ['studios_example'] # List[str] | Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimited. (optional)
    studio_ids = ['studio_ids_example'] # List[str] | Optional. If specified, results will be filtered based on studio id. This allows multiple, pipe delimited. (optional)
    user_id = 'user_id_example' # str | User id. (optional)
    name_starts_with_or_greater = 'name_starts_with_or_greater_example' # str | Optional filter by items whose name is sorted equally or greater than a given input string. (optional)
    name_starts_with = 'name_starts_with_example' # str | Optional filter by items whose name is sorted equally than a given input string. (optional)
    name_less_than = 'name_less_than_example' # str | Optional filter by items whose name is equally or lesser than a given input string. (optional)
    sort_by = [jellyfin.generated.api_10_10.ItemSortBy()] # List[ItemSortBy] | Optional. Specify one or more sort orders, comma delimited. (optional)
    sort_order = [jellyfin.generated.api_10_10.SortOrder()] # List[SortOrder] | Sort Order - Ascending,Descending. (optional)
    enable_images = True # bool | Optional, include image information in output. (optional) (default to True)
    enable_total_record_count = True # bool | Total record count. (optional) (default to True)

    try:
        # Gets all album artists from a given item, folder, or the entire library.
        api_response = api_instance.get_album_artists(min_community_rating=min_community_rating, start_index=start_index, limit=limit, search_term=search_term, parent_id=parent_id, fields=fields, exclude_item_types=exclude_item_types, include_item_types=include_item_types, filters=filters, is_favorite=is_favorite, media_types=media_types, genres=genres, genre_ids=genre_ids, official_ratings=official_ratings, tags=tags, years=years, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, person=person, person_ids=person_ids, person_types=person_types, studios=studios, studio_ids=studio_ids, user_id=user_id, name_starts_with_or_greater=name_starts_with_or_greater, name_starts_with=name_starts_with, name_less_than=name_less_than, sort_by=sort_by, sort_order=sort_order, enable_images=enable_images, enable_total_record_count=enable_total_record_count)
        print("The response of ArtistsApi->get_album_artists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistsApi->get_album_artists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_community_rating** | **float**| Optional filter by minimum community rating. | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return. | [optional] 
 **search_term** | **str**| Optional. Search term. | [optional] 
 **parent_id** | **str**| Specify this to localize the search to a specific item or folder. Omit to use the root. | [optional] 
 **fields** | [**List[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. | [optional] 
 **exclude_item_types** | [**List[BaseItemKind]**](BaseItemKind.md)| Optional. If specified, results will be filtered out based on item type. This allows multiple, comma delimited. | [optional] 
 **include_item_types** | [**List[BaseItemKind]**](BaseItemKind.md)| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited. | [optional] 
 **filters** | [**List[ItemFilter]**](ItemFilter.md)| Optional. Specify additional filters to apply. | [optional] 
 **is_favorite** | **bool**| Optional filter by items that are marked as favorite, or not. | [optional] 
 **media_types** | [**List[MediaType]**](MediaType.md)| Optional filter by MediaType. Allows multiple, comma delimited. | [optional] 
 **genres** | [**List[str]**](str.md)| Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimited. | [optional] 
 **genre_ids** | [**List[str]**](str.md)| Optional. If specified, results will be filtered based on genre id. This allows multiple, pipe delimited. | [optional] 
 **official_ratings** | [**List[str]**](str.md)| Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimited. | [optional] 
 **tags** | [**List[str]**](str.md)| Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimited. | [optional] 
 **years** | [**List[int]**](int.md)| Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimited. | [optional] 
 **enable_user_data** | **bool**| Optional, include user data. | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type. | [optional] 
 **enable_image_types** | [**List[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 
 **person** | **str**| Optional. If specified, results will be filtered to include only those containing the specified person. | [optional] 
 **person_ids** | [**List[str]**](str.md)| Optional. If specified, results will be filtered to include only those containing the specified person ids. | [optional] 
 **person_types** | [**List[str]**](str.md)| Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited. | [optional] 
 **studios** | [**List[str]**](str.md)| Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimited. | [optional] 
 **studio_ids** | [**List[str]**](str.md)| Optional. If specified, results will be filtered based on studio id. This allows multiple, pipe delimited. | [optional] 
 **user_id** | **str**| User id. | [optional] 
 **name_starts_with_or_greater** | **str**| Optional filter by items whose name is sorted equally or greater than a given input string. | [optional] 
 **name_starts_with** | **str**| Optional filter by items whose name is sorted equally than a given input string. | [optional] 
 **name_less_than** | **str**| Optional filter by items whose name is equally or lesser than a given input string. | [optional] 
 **sort_by** | [**List[ItemSortBy]**](ItemSortBy.md)| Optional. Specify one or more sort orders, comma delimited. | [optional] 
 **sort_order** | [**List[SortOrder]**](SortOrder.md)| Sort Order - Ascending,Descending. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output. | [optional] [default to True]
 **enable_total_record_count** | **bool**| Total record count. | [optional] [default to True]

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
**200** | Album artists returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artist_by_name**
> BaseItemDto get_artist_by_name(name, user_id=user_id)

Gets an artist by name.

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
    api_instance = jellyfin.generated.api_10_10.ArtistsApi(api_client)
    name = 'name_example' # str | Studio name.
    user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data. (optional)

    try:
        # Gets an artist by name.
        api_response = api_instance.get_artist_by_name(name, user_id=user_id)
        print("The response of ArtistsApi->get_artist_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistsApi->get_artist_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Studio name. | 
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
**200** | Artist returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artists**
> BaseItemDtoQueryResult get_artists(min_community_rating=min_community_rating, start_index=start_index, limit=limit, search_term=search_term, parent_id=parent_id, fields=fields, exclude_item_types=exclude_item_types, include_item_types=include_item_types, filters=filters, is_favorite=is_favorite, media_types=media_types, genres=genres, genre_ids=genre_ids, official_ratings=official_ratings, tags=tags, years=years, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, person=person, person_ids=person_ids, person_types=person_types, studios=studios, studio_ids=studio_ids, user_id=user_id, name_starts_with_or_greater=name_starts_with_or_greater, name_starts_with=name_starts_with, name_less_than=name_less_than, sort_by=sort_by, sort_order=sort_order, enable_images=enable_images, enable_total_record_count=enable_total_record_count)

Gets all artists from a given item, folder, or the entire library.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.base_item_dto_query_result import BaseItemDtoQueryResult
from jellyfin.generated.api_10_10.models.base_item_kind import BaseItemKind
from jellyfin.generated.api_10_10.models.image_type import ImageType
from jellyfin.generated.api_10_10.models.item_fields import ItemFields
from jellyfin.generated.api_10_10.models.item_filter import ItemFilter
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
    api_instance = jellyfin.generated.api_10_10.ArtistsApi(api_client)
    min_community_rating = 3.4 # float | Optional filter by minimum community rating. (optional)
    start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
    limit = 56 # int | Optional. The maximum number of records to return. (optional)
    search_term = 'search_term_example' # str | Optional. Search term. (optional)
    parent_id = 'parent_id_example' # str | Specify this to localize the search to a specific item or folder. Omit to use the root. (optional)
    fields = [jellyfin.generated.api_10_10.ItemFields()] # List[ItemFields] | Optional. Specify additional fields of information to return in the output. (optional)
    exclude_item_types = [jellyfin.generated.api_10_10.BaseItemKind()] # List[BaseItemKind] | Optional. If specified, results will be filtered out based on item type. This allows multiple, comma delimited. (optional)
    include_item_types = [jellyfin.generated.api_10_10.BaseItemKind()] # List[BaseItemKind] | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited. (optional)
    filters = [jellyfin.generated.api_10_10.ItemFilter()] # List[ItemFilter] | Optional. Specify additional filters to apply. (optional)
    is_favorite = True # bool | Optional filter by items that are marked as favorite, or not. (optional)
    media_types = [jellyfin.generated.api_10_10.MediaType()] # List[MediaType] | Optional filter by MediaType. Allows multiple, comma delimited. (optional)
    genres = ['genres_example'] # List[str] | Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimited. (optional)
    genre_ids = ['genre_ids_example'] # List[str] | Optional. If specified, results will be filtered based on genre id. This allows multiple, pipe delimited. (optional)
    official_ratings = ['official_ratings_example'] # List[str] | Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimited. (optional)
    tags = ['tags_example'] # List[str] | Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimited. (optional)
    years = [56] # List[int] | Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimited. (optional)
    enable_user_data = True # bool | Optional, include user data. (optional)
    image_type_limit = 56 # int | Optional, the max number of images to return, per image type. (optional)
    enable_image_types = [jellyfin.generated.api_10_10.ImageType()] # List[ImageType] | Optional. The image types to include in the output. (optional)
    person = 'person_example' # str | Optional. If specified, results will be filtered to include only those containing the specified person. (optional)
    person_ids = ['person_ids_example'] # List[str] | Optional. If specified, results will be filtered to include only those containing the specified person ids. (optional)
    person_types = ['person_types_example'] # List[str] | Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited. (optional)
    studios = ['studios_example'] # List[str] | Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimited. (optional)
    studio_ids = ['studio_ids_example'] # List[str] | Optional. If specified, results will be filtered based on studio id. This allows multiple, pipe delimited. (optional)
    user_id = 'user_id_example' # str | User id. (optional)
    name_starts_with_or_greater = 'name_starts_with_or_greater_example' # str | Optional filter by items whose name is sorted equally or greater than a given input string. (optional)
    name_starts_with = 'name_starts_with_example' # str | Optional filter by items whose name is sorted equally than a given input string. (optional)
    name_less_than = 'name_less_than_example' # str | Optional filter by items whose name is equally or lesser than a given input string. (optional)
    sort_by = [jellyfin.generated.api_10_10.ItemSortBy()] # List[ItemSortBy] | Optional. Specify one or more sort orders, comma delimited. (optional)
    sort_order = [jellyfin.generated.api_10_10.SortOrder()] # List[SortOrder] | Sort Order - Ascending,Descending. (optional)
    enable_images = True # bool | Optional, include image information in output. (optional) (default to True)
    enable_total_record_count = True # bool | Total record count. (optional) (default to True)

    try:
        # Gets all artists from a given item, folder, or the entire library.
        api_response = api_instance.get_artists(min_community_rating=min_community_rating, start_index=start_index, limit=limit, search_term=search_term, parent_id=parent_id, fields=fields, exclude_item_types=exclude_item_types, include_item_types=include_item_types, filters=filters, is_favorite=is_favorite, media_types=media_types, genres=genres, genre_ids=genre_ids, official_ratings=official_ratings, tags=tags, years=years, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, person=person, person_ids=person_ids, person_types=person_types, studios=studios, studio_ids=studio_ids, user_id=user_id, name_starts_with_or_greater=name_starts_with_or_greater, name_starts_with=name_starts_with, name_less_than=name_less_than, sort_by=sort_by, sort_order=sort_order, enable_images=enable_images, enable_total_record_count=enable_total_record_count)
        print("The response of ArtistsApi->get_artists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtistsApi->get_artists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_community_rating** | **float**| Optional filter by minimum community rating. | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return. | [optional] 
 **search_term** | **str**| Optional. Search term. | [optional] 
 **parent_id** | **str**| Specify this to localize the search to a specific item or folder. Omit to use the root. | [optional] 
 **fields** | [**List[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. | [optional] 
 **exclude_item_types** | [**List[BaseItemKind]**](BaseItemKind.md)| Optional. If specified, results will be filtered out based on item type. This allows multiple, comma delimited. | [optional] 
 **include_item_types** | [**List[BaseItemKind]**](BaseItemKind.md)| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited. | [optional] 
 **filters** | [**List[ItemFilter]**](ItemFilter.md)| Optional. Specify additional filters to apply. | [optional] 
 **is_favorite** | **bool**| Optional filter by items that are marked as favorite, or not. | [optional] 
 **media_types** | [**List[MediaType]**](MediaType.md)| Optional filter by MediaType. Allows multiple, comma delimited. | [optional] 
 **genres** | [**List[str]**](str.md)| Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimited. | [optional] 
 **genre_ids** | [**List[str]**](str.md)| Optional. If specified, results will be filtered based on genre id. This allows multiple, pipe delimited. | [optional] 
 **official_ratings** | [**List[str]**](str.md)| Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimited. | [optional] 
 **tags** | [**List[str]**](str.md)| Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimited. | [optional] 
 **years** | [**List[int]**](int.md)| Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimited. | [optional] 
 **enable_user_data** | **bool**| Optional, include user data. | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type. | [optional] 
 **enable_image_types** | [**List[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 
 **person** | **str**| Optional. If specified, results will be filtered to include only those containing the specified person. | [optional] 
 **person_ids** | [**List[str]**](str.md)| Optional. If specified, results will be filtered to include only those containing the specified person ids. | [optional] 
 **person_types** | [**List[str]**](str.md)| Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited. | [optional] 
 **studios** | [**List[str]**](str.md)| Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimited. | [optional] 
 **studio_ids** | [**List[str]**](str.md)| Optional. If specified, results will be filtered based on studio id. This allows multiple, pipe delimited. | [optional] 
 **user_id** | **str**| User id. | [optional] 
 **name_starts_with_or_greater** | **str**| Optional filter by items whose name is sorted equally or greater than a given input string. | [optional] 
 **name_starts_with** | **str**| Optional filter by items whose name is sorted equally than a given input string. | [optional] 
 **name_less_than** | **str**| Optional filter by items whose name is equally or lesser than a given input string. | [optional] 
 **sort_by** | [**List[ItemSortBy]**](ItemSortBy.md)| Optional. Specify one or more sort orders, comma delimited. | [optional] 
 **sort_order** | [**List[SortOrder]**](SortOrder.md)| Sort Order - Ascending,Descending. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output. | [optional] [default to True]
 **enable_total_record_count** | **bool**| Total record count. | [optional] [default to True]

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
**200** | Artists returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

