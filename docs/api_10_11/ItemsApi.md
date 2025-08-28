# jellyfin.generated.api_10_11.ItemsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_item_user_data**](ItemsApi.md#get_item_user_data) | **GET** /UserItems/{itemId}/UserData | Get Item User Data.
[**get_items**](ItemsApi.md#get_items) | **GET** /Items | Gets items based on a query.
[**get_resume_items**](ItemsApi.md#get_resume_items) | **GET** /UserItems/Resume | Gets items based on a query.
[**update_item_user_data**](ItemsApi.md#update_item_user_data) | **POST** /UserItems/{itemId}/UserData | Update Item User Data.


# **get_item_user_data**
> UserItemDataDto get_item_user_data(item_id, user_id=user_id)

Get Item User Data.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.user_item_data_dto import UserItemDataDto
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
    api_instance = jellyfin.generated.api_10_11.ItemsApi(api_client)
    item_id = 'item_id_example' # str | The item id.
    user_id = 'user_id_example' # str | The user id. (optional)

    try:
        # Get Item User Data.
        api_response = api_instance.get_item_user_data(item_id, user_id=user_id)
        print("The response of ItemsApi->get_item_user_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_item_user_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **user_id** | **str**| The user id. | [optional] 

### Return type

[**UserItemDataDto**](UserItemDataDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | return item user data. |  -  |
**404** | Item is not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items**
> BaseItemDtoQueryResult get_items(user_id=user_id, max_official_rating=max_official_rating, has_theme_song=has_theme_song, has_theme_video=has_theme_video, has_subtitles=has_subtitles, has_special_feature=has_special_feature, has_trailer=has_trailer, adjacent_to=adjacent_to, index_number=index_number, parent_index_number=parent_index_number, has_parental_rating=has_parental_rating, is_hd=is_hd, is4_k=is4_k, location_types=location_types, exclude_location_types=exclude_location_types, is_missing=is_missing, is_unaired=is_unaired, min_community_rating=min_community_rating, min_critic_rating=min_critic_rating, min_premiere_date=min_premiere_date, min_date_last_saved=min_date_last_saved, min_date_last_saved_for_user=min_date_last_saved_for_user, max_premiere_date=max_premiere_date, has_overview=has_overview, has_imdb_id=has_imdb_id, has_tmdb_id=has_tmdb_id, has_tvdb_id=has_tvdb_id, is_movie=is_movie, is_series=is_series, is_news=is_news, is_kids=is_kids, is_sports=is_sports, exclude_item_ids=exclude_item_ids, start_index=start_index, limit=limit, recursive=recursive, search_term=search_term, sort_order=sort_order, parent_id=parent_id, fields=fields, exclude_item_types=exclude_item_types, include_item_types=include_item_types, filters=filters, is_favorite=is_favorite, media_types=media_types, image_types=image_types, sort_by=sort_by, is_played=is_played, genres=genres, official_ratings=official_ratings, tags=tags, years=years, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, person=person, person_ids=person_ids, person_types=person_types, studios=studios, artists=artists, exclude_artist_ids=exclude_artist_ids, artist_ids=artist_ids, album_artist_ids=album_artist_ids, contributing_artist_ids=contributing_artist_ids, albums=albums, album_ids=album_ids, ids=ids, video_types=video_types, min_official_rating=min_official_rating, is_locked=is_locked, is_place_holder=is_place_holder, has_official_rating=has_official_rating, collapse_box_set_items=collapse_box_set_items, min_width=min_width, min_height=min_height, max_width=max_width, max_height=max_height, is3_d=is3_d, series_status=series_status, name_starts_with_or_greater=name_starts_with_or_greater, name_starts_with=name_starts_with, name_less_than=name_less_than, studio_ids=studio_ids, genre_ids=genre_ids, enable_total_record_count=enable_total_record_count, enable_images=enable_images)

Gets items based on a query.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.base_item_dto_query_result import BaseItemDtoQueryResult
from jellyfin.generated.api_10_11.models.base_item_kind import BaseItemKind
from jellyfin.generated.api_10_11.models.image_type import ImageType
from jellyfin.generated.api_10_11.models.item_fields import ItemFields
from jellyfin.generated.api_10_11.models.item_filter import ItemFilter
from jellyfin.generated.api_10_11.models.item_sort_by import ItemSortBy
from jellyfin.generated.api_10_11.models.location_type import LocationType
from jellyfin.generated.api_10_11.models.media_type import MediaType
from jellyfin.generated.api_10_11.models.series_status import SeriesStatus
from jellyfin.generated.api_10_11.models.sort_order import SortOrder
from jellyfin.generated.api_10_11.models.video_type import VideoType
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
    api_instance = jellyfin.generated.api_10_11.ItemsApi(api_client)
    user_id = 'user_id_example' # str | The user id supplied as query parameter; this is required when not using an API key. (optional)
    max_official_rating = 'max_official_rating_example' # str | Optional filter by maximum official rating (PG, PG-13, TV-MA, etc). (optional)
    has_theme_song = True # bool | Optional filter by items with theme songs. (optional)
    has_theme_video = True # bool | Optional filter by items with theme videos. (optional)
    has_subtitles = True # bool | Optional filter by items with subtitles. (optional)
    has_special_feature = True # bool | Optional filter by items with special features. (optional)
    has_trailer = True # bool | Optional filter by items with trailers. (optional)
    adjacent_to = 'adjacent_to_example' # str | Optional. Return items that are siblings of a supplied item. (optional)
    index_number = 56 # int | Optional filter by index number. (optional)
    parent_index_number = 56 # int | Optional filter by parent index number. (optional)
    has_parental_rating = True # bool | Optional filter by items that have or do not have a parental rating. (optional)
    is_hd = True # bool | Optional filter by items that are HD or not. (optional)
    is4_k = True # bool | Optional filter by items that are 4K or not. (optional)
    location_types = [jellyfin.generated.api_10_11.LocationType()] # List[LocationType] | Optional. If specified, results will be filtered based on LocationType. This allows multiple, comma delimited. (optional)
    exclude_location_types = [jellyfin.generated.api_10_11.LocationType()] # List[LocationType] | Optional. If specified, results will be filtered based on the LocationType. This allows multiple, comma delimited. (optional)
    is_missing = True # bool | Optional filter by items that are missing episodes or not. (optional)
    is_unaired = True # bool | Optional filter by items that are unaired episodes or not. (optional)
    min_community_rating = 3.4 # float | Optional filter by minimum community rating. (optional)
    min_critic_rating = 3.4 # float | Optional filter by minimum critic rating. (optional)
    min_premiere_date = '2013-10-20T19:20:30+01:00' # datetime | Optional. The minimum premiere date. Format = ISO. (optional)
    min_date_last_saved = '2013-10-20T19:20:30+01:00' # datetime | Optional. The minimum last saved date. Format = ISO. (optional)
    min_date_last_saved_for_user = '2013-10-20T19:20:30+01:00' # datetime | Optional. The minimum last saved date for the current user. Format = ISO. (optional)
    max_premiere_date = '2013-10-20T19:20:30+01:00' # datetime | Optional. The maximum premiere date. Format = ISO. (optional)
    has_overview = True # bool | Optional filter by items that have an overview or not. (optional)
    has_imdb_id = True # bool | Optional filter by items that have an IMDb id or not. (optional)
    has_tmdb_id = True # bool | Optional filter by items that have a TMDb id or not. (optional)
    has_tvdb_id = True # bool | Optional filter by items that have a TVDb id or not. (optional)
    is_movie = True # bool | Optional filter for live tv movies. (optional)
    is_series = True # bool | Optional filter for live tv series. (optional)
    is_news = True # bool | Optional filter for live tv news. (optional)
    is_kids = True # bool | Optional filter for live tv kids. (optional)
    is_sports = True # bool | Optional filter for live tv sports. (optional)
    exclude_item_ids = ['exclude_item_ids_example'] # List[str] | Optional. If specified, results will be filtered by excluding item ids. This allows multiple, comma delimited. (optional)
    start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
    limit = 56 # int | Optional. The maximum number of records to return. (optional)
    recursive = True # bool | When searching within folders, this determines whether or not the search will be recursive. true/false. (optional)
    search_term = 'search_term_example' # str | Optional. Filter based on a search term. (optional)
    sort_order = [jellyfin.generated.api_10_11.SortOrder()] # List[SortOrder] | Sort Order - Ascending, Descending. (optional)
    parent_id = 'parent_id_example' # str | Specify this to localize the search to a specific item or folder. Omit to use the root. (optional)
    fields = [jellyfin.generated.api_10_11.ItemFields()] # List[ItemFields] | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines. (optional)
    exclude_item_types = [jellyfin.generated.api_10_11.BaseItemKind()] # List[BaseItemKind] | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited. (optional)
    include_item_types = [jellyfin.generated.api_10_11.BaseItemKind()] # List[BaseItemKind] | Optional. If specified, results will be filtered based on the item type. This allows multiple, comma delimited. (optional)
    filters = [jellyfin.generated.api_10_11.ItemFilter()] # List[ItemFilter] | Optional. Specify additional filters to apply. This allows multiple, comma delimited. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes. (optional)
    is_favorite = True # bool | Optional filter by items that are marked as favorite, or not. (optional)
    media_types = [jellyfin.generated.api_10_11.MediaType()] # List[MediaType] | Optional filter by MediaType. Allows multiple, comma delimited. (optional)
    image_types = [jellyfin.generated.api_10_11.ImageType()] # List[ImageType] | Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited. (optional)
    sort_by = [jellyfin.generated.api_10_11.ItemSortBy()] # List[ItemSortBy] | Optional. Specify one or more sort orders, comma delimited. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime. (optional)
    is_played = True # bool | Optional filter by items that are played, or not. (optional)
    genres = ['genres_example'] # List[str] | Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimited. (optional)
    official_ratings = ['official_ratings_example'] # List[str] | Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimited. (optional)
    tags = ['tags_example'] # List[str] | Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimited. (optional)
    years = [56] # List[int] | Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimited. (optional)
    enable_user_data = True # bool | Optional, include user data. (optional)
    image_type_limit = 56 # int | Optional, the max number of images to return, per image type. (optional)
    enable_image_types = [jellyfin.generated.api_10_11.ImageType()] # List[ImageType] | Optional. The image types to include in the output. (optional)
    person = 'person_example' # str | Optional. If specified, results will be filtered to include only those containing the specified person. (optional)
    person_ids = ['person_ids_example'] # List[str] | Optional. If specified, results will be filtered to include only those containing the specified person id. (optional)
    person_types = ['person_types_example'] # List[str] | Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited. (optional)
    studios = ['studios_example'] # List[str] | Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimited. (optional)
    artists = ['artists_example'] # List[str] | Optional. If specified, results will be filtered based on artists. This allows multiple, pipe delimited. (optional)
    exclude_artist_ids = ['exclude_artist_ids_example'] # List[str] | Optional. If specified, results will be filtered based on artist id. This allows multiple, pipe delimited. (optional)
    artist_ids = ['artist_ids_example'] # List[str] | Optional. If specified, results will be filtered to include only those containing the specified artist id. (optional)
    album_artist_ids = ['album_artist_ids_example'] # List[str] | Optional. If specified, results will be filtered to include only those containing the specified album artist id. (optional)
    contributing_artist_ids = ['contributing_artist_ids_example'] # List[str] | Optional. If specified, results will be filtered to include only those containing the specified contributing artist id. (optional)
    albums = ['albums_example'] # List[str] | Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimited. (optional)
    album_ids = ['album_ids_example'] # List[str] | Optional. If specified, results will be filtered based on album id. This allows multiple, pipe delimited. (optional)
    ids = ['ids_example'] # List[str] | Optional. If specific items are needed, specify a list of item id's to retrieve. This allows multiple, comma delimited. (optional)
    video_types = [jellyfin.generated.api_10_11.VideoType()] # List[VideoType] | Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimited. (optional)
    min_official_rating = 'min_official_rating_example' # str | Optional filter by minimum official rating (PG, PG-13, TV-MA, etc). (optional)
    is_locked = True # bool | Optional filter by items that are locked. (optional)
    is_place_holder = True # bool | Optional filter by items that are placeholders. (optional)
    has_official_rating = True # bool | Optional filter by items that have official ratings. (optional)
    collapse_box_set_items = True # bool | Whether or not to hide items behind their boxsets. (optional)
    min_width = 56 # int | Optional. Filter by the minimum width of the item. (optional)
    min_height = 56 # int | Optional. Filter by the minimum height of the item. (optional)
    max_width = 56 # int | Optional. Filter by the maximum width of the item. (optional)
    max_height = 56 # int | Optional. Filter by the maximum height of the item. (optional)
    is3_d = True # bool | Optional filter by items that are 3D, or not. (optional)
    series_status = [jellyfin.generated.api_10_11.SeriesStatus()] # List[SeriesStatus] | Optional filter by Series Status. Allows multiple, comma delimited. (optional)
    name_starts_with_or_greater = 'name_starts_with_or_greater_example' # str | Optional filter by items whose name is sorted equally or greater than a given input string. (optional)
    name_starts_with = 'name_starts_with_example' # str | Optional filter by items whose name is sorted equally than a given input string. (optional)
    name_less_than = 'name_less_than_example' # str | Optional filter by items whose name is equally or lesser than a given input string. (optional)
    studio_ids = ['studio_ids_example'] # List[str] | Optional. If specified, results will be filtered based on studio id. This allows multiple, pipe delimited. (optional)
    genre_ids = ['genre_ids_example'] # List[str] | Optional. If specified, results will be filtered based on genre id. This allows multiple, pipe delimited. (optional)
    enable_total_record_count = True # bool | Optional. Enable the total record count. (optional) (default to True)
    enable_images = True # bool | Optional, include image information in output. (optional) (default to True)

    try:
        # Gets items based on a query.
        api_response = api_instance.get_items(user_id=user_id, max_official_rating=max_official_rating, has_theme_song=has_theme_song, has_theme_video=has_theme_video, has_subtitles=has_subtitles, has_special_feature=has_special_feature, has_trailer=has_trailer, adjacent_to=adjacent_to, index_number=index_number, parent_index_number=parent_index_number, has_parental_rating=has_parental_rating, is_hd=is_hd, is4_k=is4_k, location_types=location_types, exclude_location_types=exclude_location_types, is_missing=is_missing, is_unaired=is_unaired, min_community_rating=min_community_rating, min_critic_rating=min_critic_rating, min_premiere_date=min_premiere_date, min_date_last_saved=min_date_last_saved, min_date_last_saved_for_user=min_date_last_saved_for_user, max_premiere_date=max_premiere_date, has_overview=has_overview, has_imdb_id=has_imdb_id, has_tmdb_id=has_tmdb_id, has_tvdb_id=has_tvdb_id, is_movie=is_movie, is_series=is_series, is_news=is_news, is_kids=is_kids, is_sports=is_sports, exclude_item_ids=exclude_item_ids, start_index=start_index, limit=limit, recursive=recursive, search_term=search_term, sort_order=sort_order, parent_id=parent_id, fields=fields, exclude_item_types=exclude_item_types, include_item_types=include_item_types, filters=filters, is_favorite=is_favorite, media_types=media_types, image_types=image_types, sort_by=sort_by, is_played=is_played, genres=genres, official_ratings=official_ratings, tags=tags, years=years, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, person=person, person_ids=person_ids, person_types=person_types, studios=studios, artists=artists, exclude_artist_ids=exclude_artist_ids, artist_ids=artist_ids, album_artist_ids=album_artist_ids, contributing_artist_ids=contributing_artist_ids, albums=albums, album_ids=album_ids, ids=ids, video_types=video_types, min_official_rating=min_official_rating, is_locked=is_locked, is_place_holder=is_place_holder, has_official_rating=has_official_rating, collapse_box_set_items=collapse_box_set_items, min_width=min_width, min_height=min_height, max_width=max_width, max_height=max_height, is3_d=is3_d, series_status=series_status, name_starts_with_or_greater=name_starts_with_or_greater, name_starts_with=name_starts_with, name_less_than=name_less_than, studio_ids=studio_ids, genre_ids=genre_ids, enable_total_record_count=enable_total_record_count, enable_images=enable_images)
        print("The response of ItemsApi->get_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user id supplied as query parameter; this is required when not using an API key. | [optional] 
 **max_official_rating** | **str**| Optional filter by maximum official rating (PG, PG-13, TV-MA, etc). | [optional] 
 **has_theme_song** | **bool**| Optional filter by items with theme songs. | [optional] 
 **has_theme_video** | **bool**| Optional filter by items with theme videos. | [optional] 
 **has_subtitles** | **bool**| Optional filter by items with subtitles. | [optional] 
 **has_special_feature** | **bool**| Optional filter by items with special features. | [optional] 
 **has_trailer** | **bool**| Optional filter by items with trailers. | [optional] 
 **adjacent_to** | **str**| Optional. Return items that are siblings of a supplied item. | [optional] 
 **index_number** | **int**| Optional filter by index number. | [optional] 
 **parent_index_number** | **int**| Optional filter by parent index number. | [optional] 
 **has_parental_rating** | **bool**| Optional filter by items that have or do not have a parental rating. | [optional] 
 **is_hd** | **bool**| Optional filter by items that are HD or not. | [optional] 
 **is4_k** | **bool**| Optional filter by items that are 4K or not. | [optional] 
 **location_types** | [**List[LocationType]**](LocationType.md)| Optional. If specified, results will be filtered based on LocationType. This allows multiple, comma delimited. | [optional] 
 **exclude_location_types** | [**List[LocationType]**](LocationType.md)| Optional. If specified, results will be filtered based on the LocationType. This allows multiple, comma delimited. | [optional] 
 **is_missing** | **bool**| Optional filter by items that are missing episodes or not. | [optional] 
 **is_unaired** | **bool**| Optional filter by items that are unaired episodes or not. | [optional] 
 **min_community_rating** | **float**| Optional filter by minimum community rating. | [optional] 
 **min_critic_rating** | **float**| Optional filter by minimum critic rating. | [optional] 
 **min_premiere_date** | **datetime**| Optional. The minimum premiere date. Format &#x3D; ISO. | [optional] 
 **min_date_last_saved** | **datetime**| Optional. The minimum last saved date. Format &#x3D; ISO. | [optional] 
 **min_date_last_saved_for_user** | **datetime**| Optional. The minimum last saved date for the current user. Format &#x3D; ISO. | [optional] 
 **max_premiere_date** | **datetime**| Optional. The maximum premiere date. Format &#x3D; ISO. | [optional] 
 **has_overview** | **bool**| Optional filter by items that have an overview or not. | [optional] 
 **has_imdb_id** | **bool**| Optional filter by items that have an IMDb id or not. | [optional] 
 **has_tmdb_id** | **bool**| Optional filter by items that have a TMDb id or not. | [optional] 
 **has_tvdb_id** | **bool**| Optional filter by items that have a TVDb id or not. | [optional] 
 **is_movie** | **bool**| Optional filter for live tv movies. | [optional] 
 **is_series** | **bool**| Optional filter for live tv series. | [optional] 
 **is_news** | **bool**| Optional filter for live tv news. | [optional] 
 **is_kids** | **bool**| Optional filter for live tv kids. | [optional] 
 **is_sports** | **bool**| Optional filter for live tv sports. | [optional] 
 **exclude_item_ids** | [**List[str]**](str.md)| Optional. If specified, results will be filtered by excluding item ids. This allows multiple, comma delimited. | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return. | [optional] 
 **recursive** | **bool**| When searching within folders, this determines whether or not the search will be recursive. true/false. | [optional] 
 **search_term** | **str**| Optional. Filter based on a search term. | [optional] 
 **sort_order** | [**List[SortOrder]**](SortOrder.md)| Sort Order - Ascending, Descending. | [optional] 
 **parent_id** | **str**| Specify this to localize the search to a specific item or folder. Omit to use the root. | [optional] 
 **fields** | [**List[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines. | [optional] 
 **exclude_item_types** | [**List[BaseItemKind]**](BaseItemKind.md)| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited. | [optional] 
 **include_item_types** | [**List[BaseItemKind]**](BaseItemKind.md)| Optional. If specified, results will be filtered based on the item type. This allows multiple, comma delimited. | [optional] 
 **filters** | [**List[ItemFilter]**](ItemFilter.md)| Optional. Specify additional filters to apply. This allows multiple, comma delimited. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes. | [optional] 
 **is_favorite** | **bool**| Optional filter by items that are marked as favorite, or not. | [optional] 
 **media_types** | [**List[MediaType]**](MediaType.md)| Optional filter by MediaType. Allows multiple, comma delimited. | [optional] 
 **image_types** | [**List[ImageType]**](ImageType.md)| Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited. | [optional] 
 **sort_by** | [**List[ItemSortBy]**](ItemSortBy.md)| Optional. Specify one or more sort orders, comma delimited. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime. | [optional] 
 **is_played** | **bool**| Optional filter by items that are played, or not. | [optional] 
 **genres** | [**List[str]**](str.md)| Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimited. | [optional] 
 **official_ratings** | [**List[str]**](str.md)| Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimited. | [optional] 
 **tags** | [**List[str]**](str.md)| Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimited. | [optional] 
 **years** | [**List[int]**](int.md)| Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimited. | [optional] 
 **enable_user_data** | **bool**| Optional, include user data. | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type. | [optional] 
 **enable_image_types** | [**List[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 
 **person** | **str**| Optional. If specified, results will be filtered to include only those containing the specified person. | [optional] 
 **person_ids** | [**List[str]**](str.md)| Optional. If specified, results will be filtered to include only those containing the specified person id. | [optional] 
 **person_types** | [**List[str]**](str.md)| Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited. | [optional] 
 **studios** | [**List[str]**](str.md)| Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimited. | [optional] 
 **artists** | [**List[str]**](str.md)| Optional. If specified, results will be filtered based on artists. This allows multiple, pipe delimited. | [optional] 
 **exclude_artist_ids** | [**List[str]**](str.md)| Optional. If specified, results will be filtered based on artist id. This allows multiple, pipe delimited. | [optional] 
 **artist_ids** | [**List[str]**](str.md)| Optional. If specified, results will be filtered to include only those containing the specified artist id. | [optional] 
 **album_artist_ids** | [**List[str]**](str.md)| Optional. If specified, results will be filtered to include only those containing the specified album artist id. | [optional] 
 **contributing_artist_ids** | [**List[str]**](str.md)| Optional. If specified, results will be filtered to include only those containing the specified contributing artist id. | [optional] 
 **albums** | [**List[str]**](str.md)| Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimited. | [optional] 
 **album_ids** | [**List[str]**](str.md)| Optional. If specified, results will be filtered based on album id. This allows multiple, pipe delimited. | [optional] 
 **ids** | [**List[str]**](str.md)| Optional. If specific items are needed, specify a list of item id&#39;s to retrieve. This allows multiple, comma delimited. | [optional] 
 **video_types** | [**List[VideoType]**](VideoType.md)| Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimited. | [optional] 
 **min_official_rating** | **str**| Optional filter by minimum official rating (PG, PG-13, TV-MA, etc). | [optional] 
 **is_locked** | **bool**| Optional filter by items that are locked. | [optional] 
 **is_place_holder** | **bool**| Optional filter by items that are placeholders. | [optional] 
 **has_official_rating** | **bool**| Optional filter by items that have official ratings. | [optional] 
 **collapse_box_set_items** | **bool**| Whether or not to hide items behind their boxsets. | [optional] 
 **min_width** | **int**| Optional. Filter by the minimum width of the item. | [optional] 
 **min_height** | **int**| Optional. Filter by the minimum height of the item. | [optional] 
 **max_width** | **int**| Optional. Filter by the maximum width of the item. | [optional] 
 **max_height** | **int**| Optional. Filter by the maximum height of the item. | [optional] 
 **is3_d** | **bool**| Optional filter by items that are 3D, or not. | [optional] 
 **series_status** | [**List[SeriesStatus]**](SeriesStatus.md)| Optional filter by Series Status. Allows multiple, comma delimited. | [optional] 
 **name_starts_with_or_greater** | **str**| Optional filter by items whose name is sorted equally or greater than a given input string. | [optional] 
 **name_starts_with** | **str**| Optional filter by items whose name is sorted equally than a given input string. | [optional] 
 **name_less_than** | **str**| Optional filter by items whose name is equally or lesser than a given input string. | [optional] 
 **studio_ids** | [**List[str]**](str.md)| Optional. If specified, results will be filtered based on studio id. This allows multiple, pipe delimited. | [optional] 
 **genre_ids** | [**List[str]**](str.md)| Optional. If specified, results will be filtered based on genre id. This allows multiple, pipe delimited. | [optional] 
 **enable_total_record_count** | **bool**| Optional. Enable the total record count. | [optional] [default to True]
 **enable_images** | **bool**| Optional, include image information in output. | [optional] [default to True]

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
**200** | Success |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resume_items**
> BaseItemDtoQueryResult get_resume_items(user_id=user_id, start_index=start_index, limit=limit, search_term=search_term, parent_id=parent_id, fields=fields, media_types=media_types, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, exclude_item_types=exclude_item_types, include_item_types=include_item_types, enable_total_record_count=enable_total_record_count, enable_images=enable_images, exclude_active_sessions=exclude_active_sessions)

Gets items based on a query.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.base_item_dto_query_result import BaseItemDtoQueryResult
from jellyfin.generated.api_10_11.models.base_item_kind import BaseItemKind
from jellyfin.generated.api_10_11.models.image_type import ImageType
from jellyfin.generated.api_10_11.models.item_fields import ItemFields
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
    api_instance = jellyfin.generated.api_10_11.ItemsApi(api_client)
    user_id = 'user_id_example' # str | The user id. (optional)
    start_index = 56 # int | The start index. (optional)
    limit = 56 # int | The item limit. (optional)
    search_term = 'search_term_example' # str | The search term. (optional)
    parent_id = 'parent_id_example' # str | Specify this to localize the search to a specific item or folder. Omit to use the root. (optional)
    fields = [jellyfin.generated.api_10_11.ItemFields()] # List[ItemFields] | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines. (optional)
    media_types = [jellyfin.generated.api_10_11.MediaType()] # List[MediaType] | Optional. Filter by MediaType. Allows multiple, comma delimited. (optional)
    enable_user_data = True # bool | Optional. Include user data. (optional)
    image_type_limit = 56 # int | Optional. The max number of images to return, per image type. (optional)
    enable_image_types = [jellyfin.generated.api_10_11.ImageType()] # List[ImageType] | Optional. The image types to include in the output. (optional)
    exclude_item_types = [jellyfin.generated.api_10_11.BaseItemKind()] # List[BaseItemKind] | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited. (optional)
    include_item_types = [jellyfin.generated.api_10_11.BaseItemKind()] # List[BaseItemKind] | Optional. If specified, results will be filtered based on the item type. This allows multiple, comma delimited. (optional)
    enable_total_record_count = True # bool | Optional. Enable the total record count. (optional) (default to True)
    enable_images = True # bool | Optional. Include image information in output. (optional) (default to True)
    exclude_active_sessions = False # bool | Optional. Whether to exclude the currently active sessions. (optional) (default to False)

    try:
        # Gets items based on a query.
        api_response = api_instance.get_resume_items(user_id=user_id, start_index=start_index, limit=limit, search_term=search_term, parent_id=parent_id, fields=fields, media_types=media_types, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, exclude_item_types=exclude_item_types, include_item_types=include_item_types, enable_total_record_count=enable_total_record_count, enable_images=enable_images, exclude_active_sessions=exclude_active_sessions)
        print("The response of ItemsApi->get_resume_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_resume_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user id. | [optional] 
 **start_index** | **int**| The start index. | [optional] 
 **limit** | **int**| The item limit. | [optional] 
 **search_term** | **str**| The search term. | [optional] 
 **parent_id** | **str**| Specify this to localize the search to a specific item or folder. Omit to use the root. | [optional] 
 **fields** | [**List[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines. | [optional] 
 **media_types** | [**List[MediaType]**](MediaType.md)| Optional. Filter by MediaType. Allows multiple, comma delimited. | [optional] 
 **enable_user_data** | **bool**| Optional. Include user data. | [optional] 
 **image_type_limit** | **int**| Optional. The max number of images to return, per image type. | [optional] 
 **enable_image_types** | [**List[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 
 **exclude_item_types** | [**List[BaseItemKind]**](BaseItemKind.md)| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited. | [optional] 
 **include_item_types** | [**List[BaseItemKind]**](BaseItemKind.md)| Optional. If specified, results will be filtered based on the item type. This allows multiple, comma delimited. | [optional] 
 **enable_total_record_count** | **bool**| Optional. Enable the total record count. | [optional] [default to True]
 **enable_images** | **bool**| Optional. Include image information in output. | [optional] [default to True]
 **exclude_active_sessions** | **bool**| Optional. Whether to exclude the currently active sessions. | [optional] [default to False]

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
**200** | Items returned. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_user_data**
> UserItemDataDto update_item_user_data(item_id, update_user_item_data_dto, user_id=user_id)

Update Item User Data.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.update_user_item_data_dto import UpdateUserItemDataDto
from jellyfin.generated.api_10_11.models.user_item_data_dto import UserItemDataDto
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
    api_instance = jellyfin.generated.api_10_11.ItemsApi(api_client)
    item_id = 'item_id_example' # str | The item id.
    update_user_item_data_dto = jellyfin.generated.api_10_11.UpdateUserItemDataDto() # UpdateUserItemDataDto | New user data object.
    user_id = 'user_id_example' # str | The user id. (optional)

    try:
        # Update Item User Data.
        api_response = api_instance.update_item_user_data(item_id, update_user_item_data_dto, user_id=user_id)
        print("The response of ItemsApi->update_item_user_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->update_item_user_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **update_user_item_data_dto** | [**UpdateUserItemDataDto**](UpdateUserItemDataDto.md)| New user data object. | 
 **user_id** | **str**| The user id. | [optional] 

### Return type

[**UserItemDataDto**](UserItemDataDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | return updated user item data. |  -  |
**404** | Item is not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

