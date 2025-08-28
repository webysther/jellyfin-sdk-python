# jellyfin.generated.api_10_11.ItemLookupApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_search_criteria**](ItemLookupApi.md#apply_search_criteria) | **POST** /Items/RemoteSearch/Apply/{itemId} | Applies search criteria to an item and refreshes metadata.
[**get_book_remote_search_results**](ItemLookupApi.md#get_book_remote_search_results) | **POST** /Items/RemoteSearch/Book | Get book remote search.
[**get_box_set_remote_search_results**](ItemLookupApi.md#get_box_set_remote_search_results) | **POST** /Items/RemoteSearch/BoxSet | Get box set remote search.
[**get_external_id_infos**](ItemLookupApi.md#get_external_id_infos) | **GET** /Items/{itemId}/ExternalIdInfos | Get the item&#39;s external id info.
[**get_movie_remote_search_results**](ItemLookupApi.md#get_movie_remote_search_results) | **POST** /Items/RemoteSearch/Movie | Get movie remote search.
[**get_music_album_remote_search_results**](ItemLookupApi.md#get_music_album_remote_search_results) | **POST** /Items/RemoteSearch/MusicAlbum | Get music album remote search.
[**get_music_artist_remote_search_results**](ItemLookupApi.md#get_music_artist_remote_search_results) | **POST** /Items/RemoteSearch/MusicArtist | Get music artist remote search.
[**get_music_video_remote_search_results**](ItemLookupApi.md#get_music_video_remote_search_results) | **POST** /Items/RemoteSearch/MusicVideo | Get music video remote search.
[**get_person_remote_search_results**](ItemLookupApi.md#get_person_remote_search_results) | **POST** /Items/RemoteSearch/Person | Get person remote search.
[**get_series_remote_search_results**](ItemLookupApi.md#get_series_remote_search_results) | **POST** /Items/RemoteSearch/Series | Get series remote search.
[**get_trailer_remote_search_results**](ItemLookupApi.md#get_trailer_remote_search_results) | **POST** /Items/RemoteSearch/Trailer | Get trailer remote search.


# **apply_search_criteria**
> apply_search_criteria(item_id, remote_search_result, replace_all_images=replace_all_images)

Applies search criteria to an item and refreshes metadata.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.remote_search_result import RemoteSearchResult
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
    api_instance = jellyfin.generated.api_10_11.ItemLookupApi(api_client)
    item_id = 'item_id_example' # str | Item id.
    remote_search_result = jellyfin.generated.api_10_11.RemoteSearchResult() # RemoteSearchResult | The remote search result.
    replace_all_images = True # bool | Optional. Whether or not to replace all images. Default: True. (optional) (default to True)

    try:
        # Applies search criteria to an item and refreshes metadata.
        api_instance.apply_search_criteria(item_id, remote_search_result, replace_all_images=replace_all_images)
    except Exception as e:
        print("Exception when calling ItemLookupApi->apply_search_criteria: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item id. | 
 **remote_search_result** | [**RemoteSearchResult**](RemoteSearchResult.md)| The remote search result. | 
 **replace_all_images** | **bool**| Optional. Whether or not to replace all images. Default: True. | [optional] [default to True]

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Item metadata refreshed. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_book_remote_search_results**
> List[RemoteSearchResult] get_book_remote_search_results(book_info_remote_search_query)

Get book remote search.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.book_info_remote_search_query import BookInfoRemoteSearchQuery
from jellyfin.generated.api_10_11.models.remote_search_result import RemoteSearchResult
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
    api_instance = jellyfin.generated.api_10_11.ItemLookupApi(api_client)
    book_info_remote_search_query = jellyfin.generated.api_10_11.BookInfoRemoteSearchQuery() # BookInfoRemoteSearchQuery | Remote search query.

    try:
        # Get book remote search.
        api_response = api_instance.get_book_remote_search_results(book_info_remote_search_query)
        print("The response of ItemLookupApi->get_book_remote_search_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemLookupApi->get_book_remote_search_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_info_remote_search_query** | [**BookInfoRemoteSearchQuery**](BookInfoRemoteSearchQuery.md)| Remote search query. | 

### Return type

[**List[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Book remote search executed. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_box_set_remote_search_results**
> List[RemoteSearchResult] get_box_set_remote_search_results(box_set_info_remote_search_query)

Get box set remote search.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.box_set_info_remote_search_query import BoxSetInfoRemoteSearchQuery
from jellyfin.generated.api_10_11.models.remote_search_result import RemoteSearchResult
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
    api_instance = jellyfin.generated.api_10_11.ItemLookupApi(api_client)
    box_set_info_remote_search_query = jellyfin.generated.api_10_11.BoxSetInfoRemoteSearchQuery() # BoxSetInfoRemoteSearchQuery | Remote search query.

    try:
        # Get box set remote search.
        api_response = api_instance.get_box_set_remote_search_results(box_set_info_remote_search_query)
        print("The response of ItemLookupApi->get_box_set_remote_search_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemLookupApi->get_box_set_remote_search_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **box_set_info_remote_search_query** | [**BoxSetInfoRemoteSearchQuery**](BoxSetInfoRemoteSearchQuery.md)| Remote search query. | 

### Return type

[**List[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Box set remote search executed. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_id_infos**
> List[ExternalIdInfo] get_external_id_infos(item_id)

Get the item's external id info.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.external_id_info import ExternalIdInfo
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
    api_instance = jellyfin.generated.api_10_11.ItemLookupApi(api_client)
    item_id = 'item_id_example' # str | Item id.

    try:
        # Get the item's external id info.
        api_response = api_instance.get_external_id_infos(item_id)
        print("The response of ItemLookupApi->get_external_id_infos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemLookupApi->get_external_id_infos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item id. | 

### Return type

[**List[ExternalIdInfo]**](ExternalIdInfo.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | External id info retrieved. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_movie_remote_search_results**
> List[RemoteSearchResult] get_movie_remote_search_results(movie_info_remote_search_query)

Get movie remote search.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.movie_info_remote_search_query import MovieInfoRemoteSearchQuery
from jellyfin.generated.api_10_11.models.remote_search_result import RemoteSearchResult
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
    api_instance = jellyfin.generated.api_10_11.ItemLookupApi(api_client)
    movie_info_remote_search_query = jellyfin.generated.api_10_11.MovieInfoRemoteSearchQuery() # MovieInfoRemoteSearchQuery | Remote search query.

    try:
        # Get movie remote search.
        api_response = api_instance.get_movie_remote_search_results(movie_info_remote_search_query)
        print("The response of ItemLookupApi->get_movie_remote_search_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemLookupApi->get_movie_remote_search_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_info_remote_search_query** | [**MovieInfoRemoteSearchQuery**](MovieInfoRemoteSearchQuery.md)| Remote search query. | 

### Return type

[**List[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Movie remote search executed. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_music_album_remote_search_results**
> List[RemoteSearchResult] get_music_album_remote_search_results(album_info_remote_search_query)

Get music album remote search.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.album_info_remote_search_query import AlbumInfoRemoteSearchQuery
from jellyfin.generated.api_10_11.models.remote_search_result import RemoteSearchResult
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
    api_instance = jellyfin.generated.api_10_11.ItemLookupApi(api_client)
    album_info_remote_search_query = jellyfin.generated.api_10_11.AlbumInfoRemoteSearchQuery() # AlbumInfoRemoteSearchQuery | Remote search query.

    try:
        # Get music album remote search.
        api_response = api_instance.get_music_album_remote_search_results(album_info_remote_search_query)
        print("The response of ItemLookupApi->get_music_album_remote_search_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemLookupApi->get_music_album_remote_search_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **album_info_remote_search_query** | [**AlbumInfoRemoteSearchQuery**](AlbumInfoRemoteSearchQuery.md)| Remote search query. | 

### Return type

[**List[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Music album remote search executed. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_music_artist_remote_search_results**
> List[RemoteSearchResult] get_music_artist_remote_search_results(artist_info_remote_search_query)

Get music artist remote search.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.artist_info_remote_search_query import ArtistInfoRemoteSearchQuery
from jellyfin.generated.api_10_11.models.remote_search_result import RemoteSearchResult
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
    api_instance = jellyfin.generated.api_10_11.ItemLookupApi(api_client)
    artist_info_remote_search_query = jellyfin.generated.api_10_11.ArtistInfoRemoteSearchQuery() # ArtistInfoRemoteSearchQuery | Remote search query.

    try:
        # Get music artist remote search.
        api_response = api_instance.get_music_artist_remote_search_results(artist_info_remote_search_query)
        print("The response of ItemLookupApi->get_music_artist_remote_search_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemLookupApi->get_music_artist_remote_search_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artist_info_remote_search_query** | [**ArtistInfoRemoteSearchQuery**](ArtistInfoRemoteSearchQuery.md)| Remote search query. | 

### Return type

[**List[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Music artist remote search executed. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_music_video_remote_search_results**
> List[RemoteSearchResult] get_music_video_remote_search_results(music_video_info_remote_search_query)

Get music video remote search.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.music_video_info_remote_search_query import MusicVideoInfoRemoteSearchQuery
from jellyfin.generated.api_10_11.models.remote_search_result import RemoteSearchResult
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
    api_instance = jellyfin.generated.api_10_11.ItemLookupApi(api_client)
    music_video_info_remote_search_query = jellyfin.generated.api_10_11.MusicVideoInfoRemoteSearchQuery() # MusicVideoInfoRemoteSearchQuery | Remote search query.

    try:
        # Get music video remote search.
        api_response = api_instance.get_music_video_remote_search_results(music_video_info_remote_search_query)
        print("The response of ItemLookupApi->get_music_video_remote_search_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemLookupApi->get_music_video_remote_search_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **music_video_info_remote_search_query** | [**MusicVideoInfoRemoteSearchQuery**](MusicVideoInfoRemoteSearchQuery.md)| Remote search query. | 

### Return type

[**List[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Music video remote search executed. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_person_remote_search_results**
> List[RemoteSearchResult] get_person_remote_search_results(person_lookup_info_remote_search_query)

Get person remote search.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.person_lookup_info_remote_search_query import PersonLookupInfoRemoteSearchQuery
from jellyfin.generated.api_10_11.models.remote_search_result import RemoteSearchResult
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
    api_instance = jellyfin.generated.api_10_11.ItemLookupApi(api_client)
    person_lookup_info_remote_search_query = jellyfin.generated.api_10_11.PersonLookupInfoRemoteSearchQuery() # PersonLookupInfoRemoteSearchQuery | Remote search query.

    try:
        # Get person remote search.
        api_response = api_instance.get_person_remote_search_results(person_lookup_info_remote_search_query)
        print("The response of ItemLookupApi->get_person_remote_search_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemLookupApi->get_person_remote_search_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_lookup_info_remote_search_query** | [**PersonLookupInfoRemoteSearchQuery**](PersonLookupInfoRemoteSearchQuery.md)| Remote search query. | 

### Return type

[**List[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Person remote search executed. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_series_remote_search_results**
> List[RemoteSearchResult] get_series_remote_search_results(series_info_remote_search_query)

Get series remote search.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.remote_search_result import RemoteSearchResult
from jellyfin.generated.api_10_11.models.series_info_remote_search_query import SeriesInfoRemoteSearchQuery
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
    api_instance = jellyfin.generated.api_10_11.ItemLookupApi(api_client)
    series_info_remote_search_query = jellyfin.generated.api_10_11.SeriesInfoRemoteSearchQuery() # SeriesInfoRemoteSearchQuery | Remote search query.

    try:
        # Get series remote search.
        api_response = api_instance.get_series_remote_search_results(series_info_remote_search_query)
        print("The response of ItemLookupApi->get_series_remote_search_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemLookupApi->get_series_remote_search_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_info_remote_search_query** | [**SeriesInfoRemoteSearchQuery**](SeriesInfoRemoteSearchQuery.md)| Remote search query. | 

### Return type

[**List[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Series remote search executed. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trailer_remote_search_results**
> List[RemoteSearchResult] get_trailer_remote_search_results(trailer_info_remote_search_query)

Get trailer remote search.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.remote_search_result import RemoteSearchResult
from jellyfin.generated.api_10_11.models.trailer_info_remote_search_query import TrailerInfoRemoteSearchQuery
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
    api_instance = jellyfin.generated.api_10_11.ItemLookupApi(api_client)
    trailer_info_remote_search_query = jellyfin.generated.api_10_11.TrailerInfoRemoteSearchQuery() # TrailerInfoRemoteSearchQuery | Remote search query.

    try:
        # Get trailer remote search.
        api_response = api_instance.get_trailer_remote_search_results(trailer_info_remote_search_query)
        print("The response of ItemLookupApi->get_trailer_remote_search_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemLookupApi->get_trailer_remote_search_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trailer_info_remote_search_query** | [**TrailerInfoRemoteSearchQuery**](TrailerInfoRemoteSearchQuery.md)| Remote search query. | 

### Return type

[**List[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Trailer remote search executed. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

