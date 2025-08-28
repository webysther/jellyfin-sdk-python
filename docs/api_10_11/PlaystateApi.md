# jellyfin.generated.api_10_11.PlaystateApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mark_played_item**](PlaystateApi.md#mark_played_item) | **POST** /UserPlayedItems/{itemId} | Marks an item as played for user.
[**mark_unplayed_item**](PlaystateApi.md#mark_unplayed_item) | **DELETE** /UserPlayedItems/{itemId} | Marks an item as unplayed for user.
[**on_playback_progress**](PlaystateApi.md#on_playback_progress) | **POST** /PlayingItems/{itemId}/Progress | Reports a session&#39;s playback progress.
[**on_playback_start**](PlaystateApi.md#on_playback_start) | **POST** /PlayingItems/{itemId} | Reports that a session has begun playing an item.
[**on_playback_stopped**](PlaystateApi.md#on_playback_stopped) | **DELETE** /PlayingItems/{itemId} | Reports that a session has stopped playing an item.
[**ping_playback_session**](PlaystateApi.md#ping_playback_session) | **POST** /Sessions/Playing/Ping | Pings a playback session.
[**report_playback_progress**](PlaystateApi.md#report_playback_progress) | **POST** /Sessions/Playing/Progress | Reports playback progress within a session.
[**report_playback_start**](PlaystateApi.md#report_playback_start) | **POST** /Sessions/Playing | Reports playback has started within a session.
[**report_playback_stopped**](PlaystateApi.md#report_playback_stopped) | **POST** /Sessions/Playing/Stopped | Reports playback has stopped within a session.


# **mark_played_item**
> UserItemDataDto mark_played_item(item_id, user_id=user_id, date_played=date_played)

Marks an item as played for user.

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
    api_instance = jellyfin.generated.api_10_11.PlaystateApi(api_client)
    item_id = 'item_id_example' # str | Item id.
    user_id = 'user_id_example' # str | User id. (optional)
    date_played = '2013-10-20T19:20:30+01:00' # datetime | Optional. The date the item was played. (optional)

    try:
        # Marks an item as played for user.
        api_response = api_instance.mark_played_item(item_id, user_id=user_id, date_played=date_played)
        print("The response of PlaystateApi->mark_played_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaystateApi->mark_played_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item id. | 
 **user_id** | **str**| User id. | [optional] 
 **date_played** | **datetime**| Optional. The date the item was played. | [optional] 

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
**200** | Item marked as played. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_unplayed_item**
> UserItemDataDto mark_unplayed_item(item_id, user_id=user_id)

Marks an item as unplayed for user.

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
    api_instance = jellyfin.generated.api_10_11.PlaystateApi(api_client)
    item_id = 'item_id_example' # str | Item id.
    user_id = 'user_id_example' # str | User id. (optional)

    try:
        # Marks an item as unplayed for user.
        api_response = api_instance.mark_unplayed_item(item_id, user_id=user_id)
        print("The response of PlaystateApi->mark_unplayed_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaystateApi->mark_unplayed_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item id. | 
 **user_id** | **str**| User id. | [optional] 

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
**200** | Item marked as unplayed. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **on_playback_progress**
> on_playback_progress(item_id, media_source_id=media_source_id, position_ticks=position_ticks, audio_stream_index=audio_stream_index, subtitle_stream_index=subtitle_stream_index, volume_level=volume_level, play_method=play_method, live_stream_id=live_stream_id, play_session_id=play_session_id, repeat_mode=repeat_mode, is_paused=is_paused, is_muted=is_muted)

Reports a session's playback progress.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
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
    api_instance = jellyfin.generated.api_10_11.PlaystateApi(api_client)
    item_id = 'item_id_example' # str | Item id.
    media_source_id = 'media_source_id_example' # str | The id of the MediaSource. (optional)
    position_ticks = 56 # int | Optional. The current position, in ticks. 1 tick = 10000 ms. (optional)
    audio_stream_index = 56 # int | The audio stream index. (optional)
    subtitle_stream_index = 56 # int | The subtitle stream index. (optional)
    volume_level = 56 # int | Scale of 0-100. (optional)
    play_method = jellyfin.generated.api_10_11.PlayMethod() # PlayMethod | The play method. (optional)
    live_stream_id = 'live_stream_id_example' # str | The live stream id. (optional)
    play_session_id = 'play_session_id_example' # str | The play session id. (optional)
    repeat_mode = jellyfin.generated.api_10_11.RepeatMode() # RepeatMode | The repeat mode. (optional)
    is_paused = False # bool | Indicates if the player is paused. (optional) (default to False)
    is_muted = False # bool | Indicates if the player is muted. (optional) (default to False)

    try:
        # Reports a session's playback progress.
        api_instance.on_playback_progress(item_id, media_source_id=media_source_id, position_ticks=position_ticks, audio_stream_index=audio_stream_index, subtitle_stream_index=subtitle_stream_index, volume_level=volume_level, play_method=play_method, live_stream_id=live_stream_id, play_session_id=play_session_id, repeat_mode=repeat_mode, is_paused=is_paused, is_muted=is_muted)
    except Exception as e:
        print("Exception when calling PlaystateApi->on_playback_progress: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item id. | 
 **media_source_id** | **str**| The id of the MediaSource. | [optional] 
 **position_ticks** | **int**| Optional. The current position, in ticks. 1 tick &#x3D; 10000 ms. | [optional] 
 **audio_stream_index** | **int**| The audio stream index. | [optional] 
 **subtitle_stream_index** | **int**| The subtitle stream index. | [optional] 
 **volume_level** | **int**| Scale of 0-100. | [optional] 
 **play_method** | **PlayMethod**| The play method. | [optional] 
 **live_stream_id** | **str**| The live stream id. | [optional] 
 **play_session_id** | **str**| The play session id. | [optional] 
 **repeat_mode** | **RepeatMode**| The repeat mode. | [optional] 
 **is_paused** | **bool**| Indicates if the player is paused. | [optional] [default to False]
 **is_muted** | **bool**| Indicates if the player is muted. | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Play progress recorded. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **on_playback_start**
> on_playback_start(item_id, media_source_id=media_source_id, audio_stream_index=audio_stream_index, subtitle_stream_index=subtitle_stream_index, play_method=play_method, live_stream_id=live_stream_id, play_session_id=play_session_id, can_seek=can_seek)

Reports that a session has begun playing an item.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
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
    api_instance = jellyfin.generated.api_10_11.PlaystateApi(api_client)
    item_id = 'item_id_example' # str | Item id.
    media_source_id = 'media_source_id_example' # str | The id of the MediaSource. (optional)
    audio_stream_index = 56 # int | The audio stream index. (optional)
    subtitle_stream_index = 56 # int | The subtitle stream index. (optional)
    play_method = jellyfin.generated.api_10_11.PlayMethod() # PlayMethod | The play method. (optional)
    live_stream_id = 'live_stream_id_example' # str | The live stream id. (optional)
    play_session_id = 'play_session_id_example' # str | The play session id. (optional)
    can_seek = False # bool | Indicates if the client can seek. (optional) (default to False)

    try:
        # Reports that a session has begun playing an item.
        api_instance.on_playback_start(item_id, media_source_id=media_source_id, audio_stream_index=audio_stream_index, subtitle_stream_index=subtitle_stream_index, play_method=play_method, live_stream_id=live_stream_id, play_session_id=play_session_id, can_seek=can_seek)
    except Exception as e:
        print("Exception when calling PlaystateApi->on_playback_start: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item id. | 
 **media_source_id** | **str**| The id of the MediaSource. | [optional] 
 **audio_stream_index** | **int**| The audio stream index. | [optional] 
 **subtitle_stream_index** | **int**| The subtitle stream index. | [optional] 
 **play_method** | **PlayMethod**| The play method. | [optional] 
 **live_stream_id** | **str**| The live stream id. | [optional] 
 **play_session_id** | **str**| The play session id. | [optional] 
 **can_seek** | **bool**| Indicates if the client can seek. | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Play start recorded. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **on_playback_stopped**
> on_playback_stopped(item_id, media_source_id=media_source_id, next_media_type=next_media_type, position_ticks=position_ticks, live_stream_id=live_stream_id, play_session_id=play_session_id)

Reports that a session has stopped playing an item.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
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
    api_instance = jellyfin.generated.api_10_11.PlaystateApi(api_client)
    item_id = 'item_id_example' # str | Item id.
    media_source_id = 'media_source_id_example' # str | The id of the MediaSource. (optional)
    next_media_type = 'next_media_type_example' # str | The next media type that will play. (optional)
    position_ticks = 56 # int | Optional. The position, in ticks, where playback stopped. 1 tick = 10000 ms. (optional)
    live_stream_id = 'live_stream_id_example' # str | The live stream id. (optional)
    play_session_id = 'play_session_id_example' # str | The play session id. (optional)

    try:
        # Reports that a session has stopped playing an item.
        api_instance.on_playback_stopped(item_id, media_source_id=media_source_id, next_media_type=next_media_type, position_ticks=position_ticks, live_stream_id=live_stream_id, play_session_id=play_session_id)
    except Exception as e:
        print("Exception when calling PlaystateApi->on_playback_stopped: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item id. | 
 **media_source_id** | **str**| The id of the MediaSource. | [optional] 
 **next_media_type** | **str**| The next media type that will play. | [optional] 
 **position_ticks** | **int**| Optional. The position, in ticks, where playback stopped. 1 tick &#x3D; 10000 ms. | [optional] 
 **live_stream_id** | **str**| The live stream id. | [optional] 
 **play_session_id** | **str**| The play session id. | [optional] 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Playback stop recorded. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_playback_session**
> ping_playback_session(play_session_id)

Pings a playback session.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
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
    api_instance = jellyfin.generated.api_10_11.PlaystateApi(api_client)
    play_session_id = 'play_session_id_example' # str | Playback session id.

    try:
        # Pings a playback session.
        api_instance.ping_playback_session(play_session_id)
    except Exception as e:
        print("Exception when calling PlaystateApi->ping_playback_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **play_session_id** | **str**| Playback session id. | 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Playback session pinged. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_playback_progress**
> report_playback_progress(playback_progress_info=playback_progress_info)

Reports playback progress within a session.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.playback_progress_info import PlaybackProgressInfo
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
    api_instance = jellyfin.generated.api_10_11.PlaystateApi(api_client)
    playback_progress_info = jellyfin.generated.api_10_11.PlaybackProgressInfo() # PlaybackProgressInfo | The playback progress info. (optional)

    try:
        # Reports playback progress within a session.
        api_instance.report_playback_progress(playback_progress_info=playback_progress_info)
    except Exception as e:
        print("Exception when calling PlaystateApi->report_playback_progress: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playback_progress_info** | [**PlaybackProgressInfo**](PlaybackProgressInfo.md)| The playback progress info. | [optional] 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Playback progress recorded. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_playback_start**
> report_playback_start(playback_start_info=playback_start_info)

Reports playback has started within a session.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.playback_start_info import PlaybackStartInfo
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
    api_instance = jellyfin.generated.api_10_11.PlaystateApi(api_client)
    playback_start_info = jellyfin.generated.api_10_11.PlaybackStartInfo() # PlaybackStartInfo | The playback start info. (optional)

    try:
        # Reports playback has started within a session.
        api_instance.report_playback_start(playback_start_info=playback_start_info)
    except Exception as e:
        print("Exception when calling PlaystateApi->report_playback_start: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playback_start_info** | [**PlaybackStartInfo**](PlaybackStartInfo.md)| The playback start info. | [optional] 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Playback start recorded. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_playback_stopped**
> report_playback_stopped(playback_stop_info=playback_stop_info)

Reports playback has stopped within a session.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.playback_stop_info import PlaybackStopInfo
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
    api_instance = jellyfin.generated.api_10_11.PlaystateApi(api_client)
    playback_stop_info = jellyfin.generated.api_10_11.PlaybackStopInfo() # PlaybackStopInfo | The playback stop info. (optional)

    try:
        # Reports playback has stopped within a session.
        api_instance.report_playback_stopped(playback_stop_info=playback_stop_info)
    except Exception as e:
        print("Exception when calling PlaystateApi->report_playback_stopped: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playback_stop_info** | [**PlaybackStopInfo**](PlaybackStopInfo.md)| The playback stop info. | [optional] 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Playback stop recorded. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

