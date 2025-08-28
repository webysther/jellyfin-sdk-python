# jellyfin.generated.api_10_10.PlaylistsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_item_to_playlist**](PlaylistsApi.md#add_item_to_playlist) | **POST** /Playlists/{playlistId}/Items | Adds items to a playlist.
[**create_playlist**](PlaylistsApi.md#create_playlist) | **POST** /Playlists | Creates a new playlist.
[**get_playlist**](PlaylistsApi.md#get_playlist) | **GET** /Playlists/{playlistId} | Get a playlist.
[**get_playlist_items**](PlaylistsApi.md#get_playlist_items) | **GET** /Playlists/{playlistId}/Items | Gets the original items of a playlist.
[**get_playlist_user**](PlaylistsApi.md#get_playlist_user) | **GET** /Playlists/{playlistId}/Users/{userId} | Get a playlist user.
[**get_playlist_users**](PlaylistsApi.md#get_playlist_users) | **GET** /Playlists/{playlistId}/Users | Get a playlist&#39;s users.
[**move_item**](PlaylistsApi.md#move_item) | **POST** /Playlists/{playlistId}/Items/{itemId}/Move/{newIndex} | Moves a playlist item.
[**remove_item_from_playlist**](PlaylistsApi.md#remove_item_from_playlist) | **DELETE** /Playlists/{playlistId}/Items | Removes items from a playlist.
[**remove_user_from_playlist**](PlaylistsApi.md#remove_user_from_playlist) | **DELETE** /Playlists/{playlistId}/Users/{userId} | Remove a user from a playlist&#39;s users.
[**update_playlist**](PlaylistsApi.md#update_playlist) | **POST** /Playlists/{playlistId} | Updates a playlist.
[**update_playlist_user**](PlaylistsApi.md#update_playlist_user) | **POST** /Playlists/{playlistId}/Users/{userId} | Modify a user of a playlist&#39;s users.


# **add_item_to_playlist**
> add_item_to_playlist(playlist_id, ids=ids, user_id=user_id)

Adds items to a playlist.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
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
    api_instance = jellyfin.generated.api_10_10.PlaylistsApi(api_client)
    playlist_id = 'playlist_id_example' # str | The playlist id.
    ids = ['ids_example'] # List[str] | Item id, comma delimited. (optional)
    user_id = 'user_id_example' # str | The userId. (optional)

    try:
        # Adds items to a playlist.
        api_instance.add_item_to_playlist(playlist_id, ids=ids, user_id=user_id)
    except Exception as e:
        print("Exception when calling PlaylistsApi->add_item_to_playlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**| The playlist id. | 
 **ids** | [**List[str]**](str.md)| Item id, comma delimited. | [optional] 
 **user_id** | **str**| The userId. | [optional] 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Items added to playlist. |  -  |
**401** | Unauthorized |  -  |
**403** | Access forbidden. |  -  |
**404** | Playlist not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_playlist**
> PlaylistCreationResult create_playlist(name=name, ids=ids, user_id=user_id, media_type=media_type, create_playlist_dto=create_playlist_dto)

Creates a new playlist.

For backwards compatibility parameters can be sent via Query or Body, with Query having higher precedence.
Query parameters are obsolete.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.create_playlist_dto import CreatePlaylistDto
from jellyfin.generated.api_10_10.models.media_type import MediaType
from jellyfin.generated.api_10_10.models.playlist_creation_result import PlaylistCreationResult
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
    api_instance = jellyfin.generated.api_10_10.PlaylistsApi(api_client)
    name = 'name_example' # str | The playlist name. (optional)
    ids = ['ids_example'] # List[str] | The item ids. (optional)
    user_id = 'user_id_example' # str | The user id. (optional)
    media_type = jellyfin.generated.api_10_10.MediaType() # MediaType | The media type. (optional)
    create_playlist_dto = jellyfin.generated.api_10_10.CreatePlaylistDto() # CreatePlaylistDto | The create playlist payload. (optional)

    try:
        # Creates a new playlist.
        api_response = api_instance.create_playlist(name=name, ids=ids, user_id=user_id, media_type=media_type, create_playlist_dto=create_playlist_dto)
        print("The response of PlaylistsApi->create_playlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->create_playlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The playlist name. | [optional] 
 **ids** | [**List[str]**](str.md)| The item ids. | [optional] 
 **user_id** | **str**| The user id. | [optional] 
 **media_type** | [**MediaType**](.md)| The media type. | [optional] 
 **create_playlist_dto** | [**CreatePlaylistDto**](CreatePlaylistDto.md)| The create playlist payload. | [optional] 

### Return type

[**PlaylistCreationResult**](PlaylistCreationResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Playlist created. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_playlist**
> PlaylistDto get_playlist(playlist_id)

Get a playlist.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.playlist_dto import PlaylistDto
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
    api_instance = jellyfin.generated.api_10_10.PlaylistsApi(api_client)
    playlist_id = 'playlist_id_example' # str | The playlist id.

    try:
        # Get a playlist.
        api_response = api_instance.get_playlist(playlist_id)
        print("The response of PlaylistsApi->get_playlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->get_playlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**| The playlist id. | 

### Return type

[**PlaylistDto**](PlaylistDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The playlist. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Playlist not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_playlist_items**
> BaseItemDtoQueryResult get_playlist_items(playlist_id, user_id=user_id, start_index=start_index, limit=limit, fields=fields, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types)

Gets the original items of a playlist.

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
    api_instance = jellyfin.generated.api_10_10.PlaylistsApi(api_client)
    playlist_id = 'playlist_id_example' # str | The playlist id.
    user_id = 'user_id_example' # str | User id. (optional)
    start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
    limit = 56 # int | Optional. The maximum number of records to return. (optional)
    fields = [jellyfin.generated.api_10_10.ItemFields()] # List[ItemFields] | Optional. Specify additional fields of information to return in the output. (optional)
    enable_images = True # bool | Optional. Include image information in output. (optional)
    enable_user_data = True # bool | Optional. Include user data. (optional)
    image_type_limit = 56 # int | Optional. The max number of images to return, per image type. (optional)
    enable_image_types = [jellyfin.generated.api_10_10.ImageType()] # List[ImageType] | Optional. The image types to include in the output. (optional)

    try:
        # Gets the original items of a playlist.
        api_response = api_instance.get_playlist_items(playlist_id, user_id=user_id, start_index=start_index, limit=limit, fields=fields, enable_images=enable_images, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types)
        print("The response of PlaylistsApi->get_playlist_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->get_playlist_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**| The playlist id. | 
 **user_id** | **str**| User id. | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return. | [optional] 
 **fields** | [**List[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. | [optional] 
 **enable_images** | **bool**| Optional. Include image information in output. | [optional] 
 **enable_user_data** | **bool**| Optional. Include user data. | [optional] 
 **image_type_limit** | **int**| Optional. The max number of images to return, per image type. | [optional] 
 **enable_image_types** | [**List[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 

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
**200** | Original playlist returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Playlist not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_playlist_user**
> PlaylistUserPermissions get_playlist_user(playlist_id, user_id)

Get a playlist user.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.playlist_user_permissions import PlaylistUserPermissions
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
    api_instance = jellyfin.generated.api_10_10.PlaylistsApi(api_client)
    playlist_id = 'playlist_id_example' # str | The playlist id.
    user_id = 'user_id_example' # str | The user id.

    try:
        # Get a playlist user.
        api_response = api_instance.get_playlist_user(playlist_id, user_id)
        print("The response of PlaylistsApi->get_playlist_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->get_playlist_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**| The playlist id. | 
 **user_id** | **str**| The user id. | 

### Return type

[**PlaylistUserPermissions**](PlaylistUserPermissions.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User permission found. |  -  |
**401** | Unauthorized |  -  |
**403** | Access forbidden. |  -  |
**404** | Playlist not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_playlist_users**
> List[PlaylistUserPermissions] get_playlist_users(playlist_id)

Get a playlist's users.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.playlist_user_permissions import PlaylistUserPermissions
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
    api_instance = jellyfin.generated.api_10_10.PlaylistsApi(api_client)
    playlist_id = 'playlist_id_example' # str | The playlist id.

    try:
        # Get a playlist's users.
        api_response = api_instance.get_playlist_users(playlist_id)
        print("The response of PlaylistsApi->get_playlist_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->get_playlist_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**| The playlist id. | 

### Return type

[**List[PlaylistUserPermissions]**](PlaylistUserPermissions.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found shares. |  -  |
**401** | Unauthorized |  -  |
**403** | Access forbidden. |  -  |
**404** | Playlist not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_item**
> move_item(playlist_id, item_id, new_index)

Moves a playlist item.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
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
    api_instance = jellyfin.generated.api_10_10.PlaylistsApi(api_client)
    playlist_id = 'playlist_id_example' # str | The playlist id.
    item_id = 'item_id_example' # str | The item id.
    new_index = 56 # int | The new index.

    try:
        # Moves a playlist item.
        api_instance.move_item(playlist_id, item_id, new_index)
    except Exception as e:
        print("Exception when calling PlaylistsApi->move_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**| The playlist id. | 
 **item_id** | **str**| The item id. | 
 **new_index** | **int**| The new index. | 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Item moved to new index. |  -  |
**401** | Unauthorized |  -  |
**403** | Access forbidden. |  -  |
**404** | Playlist not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_item_from_playlist**
> remove_item_from_playlist(playlist_id, entry_ids=entry_ids)

Removes items from a playlist.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
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
    api_instance = jellyfin.generated.api_10_10.PlaylistsApi(api_client)
    playlist_id = 'playlist_id_example' # str | The playlist id.
    entry_ids = ['entry_ids_example'] # List[str] | The item ids, comma delimited. (optional)

    try:
        # Removes items from a playlist.
        api_instance.remove_item_from_playlist(playlist_id, entry_ids=entry_ids)
    except Exception as e:
        print("Exception when calling PlaylistsApi->remove_item_from_playlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**| The playlist id. | 
 **entry_ids** | [**List[str]**](str.md)| The item ids, comma delimited. | [optional] 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Items removed. |  -  |
**401** | Unauthorized |  -  |
**403** | Access forbidden. |  -  |
**404** | Playlist not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_from_playlist**
> remove_user_from_playlist(playlist_id, user_id)

Remove a user from a playlist's users.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
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
    api_instance = jellyfin.generated.api_10_10.PlaylistsApi(api_client)
    playlist_id = 'playlist_id_example' # str | The playlist id.
    user_id = 'user_id_example' # str | The user id.

    try:
        # Remove a user from a playlist's users.
        api_instance.remove_user_from_playlist(playlist_id, user_id)
    except Exception as e:
        print("Exception when calling PlaylistsApi->remove_user_from_playlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**| The playlist id. | 
 **user_id** | **str**| The user id. | 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | User permissions removed from playlist. |  -  |
**401** | Unauthorized access. |  -  |
**403** | Forbidden |  -  |
**404** | No playlist or user permissions found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_playlist**
> update_playlist(playlist_id, update_playlist_dto)

Updates a playlist.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.update_playlist_dto import UpdatePlaylistDto
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
    api_instance = jellyfin.generated.api_10_10.PlaylistsApi(api_client)
    playlist_id = 'playlist_id_example' # str | The playlist id.
    update_playlist_dto = jellyfin.generated.api_10_10.UpdatePlaylistDto() # UpdatePlaylistDto | The Jellyfin.Api.Models.PlaylistDtos.UpdatePlaylistDto id.

    try:
        # Updates a playlist.
        api_instance.update_playlist(playlist_id, update_playlist_dto)
    except Exception as e:
        print("Exception when calling PlaylistsApi->update_playlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**| The playlist id. | 
 **update_playlist_dto** | [**UpdatePlaylistDto**](UpdatePlaylistDto.md)| The Jellyfin.Api.Models.PlaylistDtos.UpdatePlaylistDto id. | 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Playlist updated. |  -  |
**401** | Unauthorized |  -  |
**403** | Access forbidden. |  -  |
**404** | Playlist not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_playlist_user**
> update_playlist_user(playlist_id, user_id, update_playlist_user_dto)

Modify a user of a playlist's users.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.update_playlist_user_dto import UpdatePlaylistUserDto
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
    api_instance = jellyfin.generated.api_10_10.PlaylistsApi(api_client)
    playlist_id = 'playlist_id_example' # str | The playlist id.
    user_id = 'user_id_example' # str | The user id.
    update_playlist_user_dto = jellyfin.generated.api_10_10.UpdatePlaylistUserDto() # UpdatePlaylistUserDto | The Jellyfin.Api.Models.PlaylistDtos.UpdatePlaylistUserDto.

    try:
        # Modify a user of a playlist's users.
        api_instance.update_playlist_user(playlist_id, user_id, update_playlist_user_dto)
    except Exception as e:
        print("Exception when calling PlaylistsApi->update_playlist_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**| The playlist id. | 
 **user_id** | **str**| The user id. | 
 **update_playlist_user_dto** | [**UpdatePlaylistUserDto**](UpdatePlaylistUserDto.md)| The Jellyfin.Api.Models.PlaylistDtos.UpdatePlaylistUserDto. | 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | User&#39;s permissions modified. |  -  |
**401** | Unauthorized |  -  |
**403** | Access forbidden. |  -  |
**404** | Playlist not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

