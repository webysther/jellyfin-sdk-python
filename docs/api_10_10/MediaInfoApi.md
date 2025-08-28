# jellyfin.generated.api_10_10.MediaInfoApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close_live_stream**](MediaInfoApi.md#close_live_stream) | **POST** /LiveStreams/Close | Closes a media source.
[**get_bitrate_test_bytes**](MediaInfoApi.md#get_bitrate_test_bytes) | **GET** /Playback/BitrateTest | Tests the network with a request with the size of the bitrate.
[**get_playback_info**](MediaInfoApi.md#get_playback_info) | **GET** /Items/{itemId}/PlaybackInfo | Gets live playback media info for an item.
[**get_posted_playback_info**](MediaInfoApi.md#get_posted_playback_info) | **POST** /Items/{itemId}/PlaybackInfo | Gets live playback media info for an item.
[**open_live_stream**](MediaInfoApi.md#open_live_stream) | **POST** /LiveStreams/Open | Opens a media source.


# **close_live_stream**
> close_live_stream(live_stream_id)

Closes a media source.

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
    api_instance = jellyfin.generated.api_10_10.MediaInfoApi(api_client)
    live_stream_id = 'live_stream_id_example' # str | The livestream id.

    try:
        # Closes a media source.
        api_instance.close_live_stream(live_stream_id)
    except Exception as e:
        print("Exception when calling MediaInfoApi->close_live_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The livestream id. | 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Livestream closed. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bitrate_test_bytes**
> bytearray get_bitrate_test_bytes(size=size)

Tests the network with a request with the size of the bitrate.

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
    api_instance = jellyfin.generated.api_10_10.MediaInfoApi(api_client)
    size = 102400 # int | The bitrate. Defaults to 102400. (optional) (default to 102400)

    try:
        # Tests the network with a request with the size of the bitrate.
        api_response = api_instance.get_bitrate_test_bytes(size=size)
        print("The response of MediaInfoApi->get_bitrate_test_bytes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaInfoApi->get_bitrate_test_bytes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The bitrate. Defaults to 102400. | [optional] [default to 102400]

### Return type

**bytearray**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Test buffer returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_playback_info**
> PlaybackInfoResponse get_playback_info(item_id, user_id=user_id)

Gets live playback media info for an item.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.playback_info_response import PlaybackInfoResponse
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
    api_instance = jellyfin.generated.api_10_10.MediaInfoApi(api_client)
    item_id = 'item_id_example' # str | The item id.
    user_id = 'user_id_example' # str | The user id. (optional)

    try:
        # Gets live playback media info for an item.
        api_response = api_instance.get_playback_info(item_id, user_id=user_id)
        print("The response of MediaInfoApi->get_playback_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaInfoApi->get_playback_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **user_id** | **str**| The user id. | [optional] 

### Return type

[**PlaybackInfoResponse**](PlaybackInfoResponse.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Playback info returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Item not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_posted_playback_info**
> PlaybackInfoResponse get_posted_playback_info(item_id, user_id=user_id, max_streaming_bitrate=max_streaming_bitrate, start_time_ticks=start_time_ticks, audio_stream_index=audio_stream_index, subtitle_stream_index=subtitle_stream_index, max_audio_channels=max_audio_channels, media_source_id=media_source_id, live_stream_id=live_stream_id, auto_open_live_stream=auto_open_live_stream, enable_direct_play=enable_direct_play, enable_direct_stream=enable_direct_stream, enable_transcoding=enable_transcoding, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, playback_info_dto=playback_info_dto)

Gets live playback media info for an item.

For backwards compatibility parameters can be sent via Query or Body, with Query having higher precedence.
Query parameters are obsolete.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.playback_info_dto import PlaybackInfoDto
from jellyfin.generated.api_10_10.models.playback_info_response import PlaybackInfoResponse
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
    api_instance = jellyfin.generated.api_10_10.MediaInfoApi(api_client)
    item_id = 'item_id_example' # str | The item id.
    user_id = 'user_id_example' # str | The user id. (optional)
    max_streaming_bitrate = 56 # int | The maximum streaming bitrate. (optional)
    start_time_ticks = 56 # int | The start time in ticks. (optional)
    audio_stream_index = 56 # int | The audio stream index. (optional)
    subtitle_stream_index = 56 # int | The subtitle stream index. (optional)
    max_audio_channels = 56 # int | The maximum number of audio channels. (optional)
    media_source_id = 'media_source_id_example' # str | The media source id. (optional)
    live_stream_id = 'live_stream_id_example' # str | The livestream id. (optional)
    auto_open_live_stream = True # bool | Whether to auto open the livestream. (optional)
    enable_direct_play = True # bool | Whether to enable direct play. Default: true. (optional)
    enable_direct_stream = True # bool | Whether to enable direct stream. Default: true. (optional)
    enable_transcoding = True # bool | Whether to enable transcoding. Default: true. (optional)
    allow_video_stream_copy = True # bool | Whether to allow to copy the video stream. Default: true. (optional)
    allow_audio_stream_copy = True # bool | Whether to allow to copy the audio stream. Default: true. (optional)
    playback_info_dto = jellyfin.generated.api_10_10.PlaybackInfoDto() # PlaybackInfoDto | The playback info. (optional)

    try:
        # Gets live playback media info for an item.
        api_response = api_instance.get_posted_playback_info(item_id, user_id=user_id, max_streaming_bitrate=max_streaming_bitrate, start_time_ticks=start_time_ticks, audio_stream_index=audio_stream_index, subtitle_stream_index=subtitle_stream_index, max_audio_channels=max_audio_channels, media_source_id=media_source_id, live_stream_id=live_stream_id, auto_open_live_stream=auto_open_live_stream, enable_direct_play=enable_direct_play, enable_direct_stream=enable_direct_stream, enable_transcoding=enable_transcoding, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, playback_info_dto=playback_info_dto)
        print("The response of MediaInfoApi->get_posted_playback_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaInfoApi->get_posted_playback_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **user_id** | **str**| The user id. | [optional] 
 **max_streaming_bitrate** | **int**| The maximum streaming bitrate. | [optional] 
 **start_time_ticks** | **int**| The start time in ticks. | [optional] 
 **audio_stream_index** | **int**| The audio stream index. | [optional] 
 **subtitle_stream_index** | **int**| The subtitle stream index. | [optional] 
 **max_audio_channels** | **int**| The maximum number of audio channels. | [optional] 
 **media_source_id** | **str**| The media source id. | [optional] 
 **live_stream_id** | **str**| The livestream id. | [optional] 
 **auto_open_live_stream** | **bool**| Whether to auto open the livestream. | [optional] 
 **enable_direct_play** | **bool**| Whether to enable direct play. Default: true. | [optional] 
 **enable_direct_stream** | **bool**| Whether to enable direct stream. Default: true. | [optional] 
 **enable_transcoding** | **bool**| Whether to enable transcoding. Default: true. | [optional] 
 **allow_video_stream_copy** | **bool**| Whether to allow to copy the video stream. Default: true. | [optional] 
 **allow_audio_stream_copy** | **bool**| Whether to allow to copy the audio stream. Default: true. | [optional] 
 **playback_info_dto** | [**PlaybackInfoDto**](PlaybackInfoDto.md)| The playback info. | [optional] 

### Return type

[**PlaybackInfoResponse**](PlaybackInfoResponse.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Playback info returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Item not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_live_stream**
> LiveStreamResponse open_live_stream(open_token=open_token, user_id=user_id, play_session_id=play_session_id, max_streaming_bitrate=max_streaming_bitrate, start_time_ticks=start_time_ticks, audio_stream_index=audio_stream_index, subtitle_stream_index=subtitle_stream_index, max_audio_channels=max_audio_channels, item_id=item_id, enable_direct_play=enable_direct_play, enable_direct_stream=enable_direct_stream, always_burn_in_subtitle_when_transcoding=always_burn_in_subtitle_when_transcoding, open_live_stream_dto=open_live_stream_dto)

Opens a media source.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.live_stream_response import LiveStreamResponse
from jellyfin.generated.api_10_10.models.open_live_stream_dto import OpenLiveStreamDto
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
    api_instance = jellyfin.generated.api_10_10.MediaInfoApi(api_client)
    open_token = 'open_token_example' # str | The open token. (optional)
    user_id = 'user_id_example' # str | The user id. (optional)
    play_session_id = 'play_session_id_example' # str | The play session id. (optional)
    max_streaming_bitrate = 56 # int | The maximum streaming bitrate. (optional)
    start_time_ticks = 56 # int | The start time in ticks. (optional)
    audio_stream_index = 56 # int | The audio stream index. (optional)
    subtitle_stream_index = 56 # int | The subtitle stream index. (optional)
    max_audio_channels = 56 # int | The maximum number of audio channels. (optional)
    item_id = 'item_id_example' # str | The item id. (optional)
    enable_direct_play = True # bool | Whether to enable direct play. Default: true. (optional)
    enable_direct_stream = True # bool | Whether to enable direct stream. Default: true. (optional)
    always_burn_in_subtitle_when_transcoding = True # bool | Always burn-in subtitle when transcoding. (optional)
    open_live_stream_dto = jellyfin.generated.api_10_10.OpenLiveStreamDto() # OpenLiveStreamDto | The open live stream dto. (optional)

    try:
        # Opens a media source.
        api_response = api_instance.open_live_stream(open_token=open_token, user_id=user_id, play_session_id=play_session_id, max_streaming_bitrate=max_streaming_bitrate, start_time_ticks=start_time_ticks, audio_stream_index=audio_stream_index, subtitle_stream_index=subtitle_stream_index, max_audio_channels=max_audio_channels, item_id=item_id, enable_direct_play=enable_direct_play, enable_direct_stream=enable_direct_stream, always_burn_in_subtitle_when_transcoding=always_burn_in_subtitle_when_transcoding, open_live_stream_dto=open_live_stream_dto)
        print("The response of MediaInfoApi->open_live_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaInfoApi->open_live_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_token** | **str**| The open token. | [optional] 
 **user_id** | **str**| The user id. | [optional] 
 **play_session_id** | **str**| The play session id. | [optional] 
 **max_streaming_bitrate** | **int**| The maximum streaming bitrate. | [optional] 
 **start_time_ticks** | **int**| The start time in ticks. | [optional] 
 **audio_stream_index** | **int**| The audio stream index. | [optional] 
 **subtitle_stream_index** | **int**| The subtitle stream index. | [optional] 
 **max_audio_channels** | **int**| The maximum number of audio channels. | [optional] 
 **item_id** | **str**| The item id. | [optional] 
 **enable_direct_play** | **bool**| Whether to enable direct play. Default: true. | [optional] 
 **enable_direct_stream** | **bool**| Whether to enable direct stream. Default: true. | [optional] 
 **always_burn_in_subtitle_when_transcoding** | **bool**| Always burn-in subtitle when transcoding. | [optional] 
 **open_live_stream_dto** | [**OpenLiveStreamDto**](OpenLiveStreamDto.md)| The open live stream dto. | [optional] 

### Return type

[**LiveStreamResponse**](LiveStreamResponse.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Media source opened. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

