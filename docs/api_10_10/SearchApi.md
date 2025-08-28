# jellyfin.generated.api_10_10.SearchApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_search_hints**](SearchApi.md#get_search_hints) | **GET** /Search/Hints | Gets the search hint result.


# **get_search_hints**
> SearchHintResult get_search_hints(search_term, start_index=start_index, limit=limit, user_id=user_id, include_item_types=include_item_types, exclude_item_types=exclude_item_types, media_types=media_types, parent_id=parent_id, is_movie=is_movie, is_series=is_series, is_news=is_news, is_kids=is_kids, is_sports=is_sports, include_people=include_people, include_media=include_media, include_genres=include_genres, include_studios=include_studios, include_artists=include_artists)

Gets the search hint result.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.base_item_kind import BaseItemKind
from jellyfin.generated.api_10_10.models.media_type import MediaType
from jellyfin.generated.api_10_10.models.search_hint_result import SearchHintResult
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
    api_instance = jellyfin.generated.api_10_10.SearchApi(api_client)
    search_term = 'search_term_example' # str | The search term to filter on.
    start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
    limit = 56 # int | Optional. The maximum number of records to return. (optional)
    user_id = 'user_id_example' # str | Optional. Supply a user id to search within a user's library or omit to search all. (optional)
    include_item_types = [jellyfin.generated.api_10_10.BaseItemKind()] # List[BaseItemKind] | If specified, only results with the specified item types are returned. This allows multiple, comma delimited. (optional)
    exclude_item_types = [jellyfin.generated.api_10_10.BaseItemKind()] # List[BaseItemKind] | If specified, results with these item types are filtered out. This allows multiple, comma delimited. (optional)
    media_types = [jellyfin.generated.api_10_10.MediaType()] # List[MediaType] | If specified, only results with the specified media types are returned. This allows multiple, comma delimited. (optional)
    parent_id = 'parent_id_example' # str | If specified, only children of the parent are returned. (optional)
    is_movie = True # bool | Optional filter for movies. (optional)
    is_series = True # bool | Optional filter for series. (optional)
    is_news = True # bool | Optional filter for news. (optional)
    is_kids = True # bool | Optional filter for kids. (optional)
    is_sports = True # bool | Optional filter for sports. (optional)
    include_people = True # bool | Optional filter whether to include people. (optional) (default to True)
    include_media = True # bool | Optional filter whether to include media. (optional) (default to True)
    include_genres = True # bool | Optional filter whether to include genres. (optional) (default to True)
    include_studios = True # bool | Optional filter whether to include studios. (optional) (default to True)
    include_artists = True # bool | Optional filter whether to include artists. (optional) (default to True)

    try:
        # Gets the search hint result.
        api_response = api_instance.get_search_hints(search_term, start_index=start_index, limit=limit, user_id=user_id, include_item_types=include_item_types, exclude_item_types=exclude_item_types, media_types=media_types, parent_id=parent_id, is_movie=is_movie, is_series=is_series, is_news=is_news, is_kids=is_kids, is_sports=is_sports, include_people=include_people, include_media=include_media, include_genres=include_genres, include_studios=include_studios, include_artists=include_artists)
        print("The response of SearchApi->get_search_hints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_search_hints: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_term** | **str**| The search term to filter on. | 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return. | [optional] 
 **user_id** | **str**| Optional. Supply a user id to search within a user&#39;s library or omit to search all. | [optional] 
 **include_item_types** | [**List[BaseItemKind]**](BaseItemKind.md)| If specified, only results with the specified item types are returned. This allows multiple, comma delimited. | [optional] 
 **exclude_item_types** | [**List[BaseItemKind]**](BaseItemKind.md)| If specified, results with these item types are filtered out. This allows multiple, comma delimited. | [optional] 
 **media_types** | [**List[MediaType]**](MediaType.md)| If specified, only results with the specified media types are returned. This allows multiple, comma delimited. | [optional] 
 **parent_id** | **str**| If specified, only children of the parent are returned. | [optional] 
 **is_movie** | **bool**| Optional filter for movies. | [optional] 
 **is_series** | **bool**| Optional filter for series. | [optional] 
 **is_news** | **bool**| Optional filter for news. | [optional] 
 **is_kids** | **bool**| Optional filter for kids. | [optional] 
 **is_sports** | **bool**| Optional filter for sports. | [optional] 
 **include_people** | **bool**| Optional filter whether to include people. | [optional] [default to True]
 **include_media** | **bool**| Optional filter whether to include media. | [optional] [default to True]
 **include_genres** | **bool**| Optional filter whether to include genres. | [optional] [default to True]
 **include_studios** | **bool**| Optional filter whether to include studios. | [optional] [default to True]
 **include_artists** | **bool**| Optional filter whether to include artists. | [optional] [default to True]

### Return type

[**SearchHintResult**](SearchHintResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Search hint returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

