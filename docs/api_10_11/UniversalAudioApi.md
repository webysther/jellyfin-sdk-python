# jellyfin.generated.api_10_11.UniversalAudioApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_universal_audio_stream**](UniversalAudioApi.md#get_universal_audio_stream) | **GET** /Audio/{itemId}/universal | Gets an audio stream.
[**head_universal_audio_stream**](UniversalAudioApi.md#head_universal_audio_stream) | **HEAD** /Audio/{itemId}/universal | Gets an audio stream.


# **get_universal_audio_stream**
> bytearray get_universal_audio_stream(item_id, container=container, media_source_id=media_source_id, device_id=device_id, user_id=user_id, audio_codec=audio_codec, max_audio_channels=max_audio_channels, transcoding_audio_channels=transcoding_audio_channels, max_streaming_bitrate=max_streaming_bitrate, audio_bit_rate=audio_bit_rate, start_time_ticks=start_time_ticks, transcoding_container=transcoding_container, transcoding_protocol=transcoding_protocol, max_audio_sample_rate=max_audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, enable_remote_media=enable_remote_media, enable_audio_vbr_encoding=enable_audio_vbr_encoding, break_on_non_key_frames=break_on_non_key_frames, enable_redirection=enable_redirection)

Gets an audio stream.

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
    api_instance = jellyfin.generated.api_10_11.UniversalAudioApi(api_client)
    item_id = 'item_id_example' # str | The item id.
    container = ['container_example'] # List[str] | Optional. The audio container. (optional)
    media_source_id = 'media_source_id_example' # str | The media version id, if playing an alternate version. (optional)
    device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
    user_id = 'user_id_example' # str | Optional. The user id. (optional)
    audio_codec = 'audio_codec_example' # str | Optional. The audio codec to transcode to. (optional)
    max_audio_channels = 56 # int | Optional. The maximum number of audio channels. (optional)
    transcoding_audio_channels = 56 # int | Optional. The number of how many audio channels to transcode to. (optional)
    max_streaming_bitrate = 56 # int | Optional. The maximum streaming bitrate. (optional)
    audio_bit_rate = 56 # int | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. (optional)
    start_time_ticks = 56 # int | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms. (optional)
    transcoding_container = 'transcoding_container_example' # str | Optional. The container to transcode to. (optional)
    transcoding_protocol = jellyfin.generated.api_10_11.MediaStreamProtocol() # MediaStreamProtocol | Optional. The transcoding protocol. (optional)
    max_audio_sample_rate = 56 # int | Optional. The maximum audio sample rate. (optional)
    max_audio_bit_depth = 56 # int | Optional. The maximum audio bit depth. (optional)
    enable_remote_media = True # bool | Optional. Whether to enable remote media. (optional)
    enable_audio_vbr_encoding = True # bool | Optional. Whether to enable Audio Encoding. (optional) (default to True)
    break_on_non_key_frames = False # bool | Optional. Whether to break on non key frames. (optional) (default to False)
    enable_redirection = True # bool | Whether to enable redirection. Defaults to true. (optional) (default to True)

    try:
        # Gets an audio stream.
        api_response = api_instance.get_universal_audio_stream(item_id, container=container, media_source_id=media_source_id, device_id=device_id, user_id=user_id, audio_codec=audio_codec, max_audio_channels=max_audio_channels, transcoding_audio_channels=transcoding_audio_channels, max_streaming_bitrate=max_streaming_bitrate, audio_bit_rate=audio_bit_rate, start_time_ticks=start_time_ticks, transcoding_container=transcoding_container, transcoding_protocol=transcoding_protocol, max_audio_sample_rate=max_audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, enable_remote_media=enable_remote_media, enable_audio_vbr_encoding=enable_audio_vbr_encoding, break_on_non_key_frames=break_on_non_key_frames, enable_redirection=enable_redirection)
        print("The response of UniversalAudioApi->get_universal_audio_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniversalAudioApi->get_universal_audio_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **container** | [**List[str]**](str.md)| Optional. The audio container. | [optional] 
 **media_source_id** | **str**| The media version id, if playing an alternate version. | [optional] 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **user_id** | **str**| Optional. The user id. | [optional] 
 **audio_codec** | **str**| Optional. The audio codec to transcode to. | [optional] 
 **max_audio_channels** | **int**| Optional. The maximum number of audio channels. | [optional] 
 **transcoding_audio_channels** | **int**| Optional. The number of how many audio channels to transcode to. | [optional] 
 **max_streaming_bitrate** | **int**| Optional. The maximum streaming bitrate. | [optional] 
 **audio_bit_rate** | **int**| Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1 tick &#x3D; 10000 ms. | [optional] 
 **transcoding_container** | **str**| Optional. The container to transcode to. | [optional] 
 **transcoding_protocol** | **MediaStreamProtocol**| Optional. The transcoding protocol. | [optional] 
 **max_audio_sample_rate** | **int**| Optional. The maximum audio sample rate. | [optional] 
 **max_audio_bit_depth** | **int**| Optional. The maximum audio bit depth. | [optional] 
 **enable_remote_media** | **bool**| Optional. Whether to enable remote media. | [optional] 
 **enable_audio_vbr_encoding** | **bool**| Optional. Whether to enable Audio Encoding. | [optional] [default to True]
 **break_on_non_key_frames** | **bool**| Optional. Whether to break on non key frames. | [optional] [default to False]
 **enable_redirection** | **bool**| Whether to enable redirection. Defaults to true. | [optional] [default to True]

### Return type

**bytearray**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: audio/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Audio stream returned. |  -  |
**302** | Redirected to remote audio stream. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_universal_audio_stream**
> bytearray head_universal_audio_stream(item_id, container=container, media_source_id=media_source_id, device_id=device_id, user_id=user_id, audio_codec=audio_codec, max_audio_channels=max_audio_channels, transcoding_audio_channels=transcoding_audio_channels, max_streaming_bitrate=max_streaming_bitrate, audio_bit_rate=audio_bit_rate, start_time_ticks=start_time_ticks, transcoding_container=transcoding_container, transcoding_protocol=transcoding_protocol, max_audio_sample_rate=max_audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, enable_remote_media=enable_remote_media, enable_audio_vbr_encoding=enable_audio_vbr_encoding, break_on_non_key_frames=break_on_non_key_frames, enable_redirection=enable_redirection)

Gets an audio stream.

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
    api_instance = jellyfin.generated.api_10_11.UniversalAudioApi(api_client)
    item_id = 'item_id_example' # str | The item id.
    container = ['container_example'] # List[str] | Optional. The audio container. (optional)
    media_source_id = 'media_source_id_example' # str | The media version id, if playing an alternate version. (optional)
    device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
    user_id = 'user_id_example' # str | Optional. The user id. (optional)
    audio_codec = 'audio_codec_example' # str | Optional. The audio codec to transcode to. (optional)
    max_audio_channels = 56 # int | Optional. The maximum number of audio channels. (optional)
    transcoding_audio_channels = 56 # int | Optional. The number of how many audio channels to transcode to. (optional)
    max_streaming_bitrate = 56 # int | Optional. The maximum streaming bitrate. (optional)
    audio_bit_rate = 56 # int | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. (optional)
    start_time_ticks = 56 # int | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms. (optional)
    transcoding_container = 'transcoding_container_example' # str | Optional. The container to transcode to. (optional)
    transcoding_protocol = jellyfin.generated.api_10_11.MediaStreamProtocol() # MediaStreamProtocol | Optional. The transcoding protocol. (optional)
    max_audio_sample_rate = 56 # int | Optional. The maximum audio sample rate. (optional)
    max_audio_bit_depth = 56 # int | Optional. The maximum audio bit depth. (optional)
    enable_remote_media = True # bool | Optional. Whether to enable remote media. (optional)
    enable_audio_vbr_encoding = True # bool | Optional. Whether to enable Audio Encoding. (optional) (default to True)
    break_on_non_key_frames = False # bool | Optional. Whether to break on non key frames. (optional) (default to False)
    enable_redirection = True # bool | Whether to enable redirection. Defaults to true. (optional) (default to True)

    try:
        # Gets an audio stream.
        api_response = api_instance.head_universal_audio_stream(item_id, container=container, media_source_id=media_source_id, device_id=device_id, user_id=user_id, audio_codec=audio_codec, max_audio_channels=max_audio_channels, transcoding_audio_channels=transcoding_audio_channels, max_streaming_bitrate=max_streaming_bitrate, audio_bit_rate=audio_bit_rate, start_time_ticks=start_time_ticks, transcoding_container=transcoding_container, transcoding_protocol=transcoding_protocol, max_audio_sample_rate=max_audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, enable_remote_media=enable_remote_media, enable_audio_vbr_encoding=enable_audio_vbr_encoding, break_on_non_key_frames=break_on_non_key_frames, enable_redirection=enable_redirection)
        print("The response of UniversalAudioApi->head_universal_audio_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UniversalAudioApi->head_universal_audio_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **container** | [**List[str]**](str.md)| Optional. The audio container. | [optional] 
 **media_source_id** | **str**| The media version id, if playing an alternate version. | [optional] 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **user_id** | **str**| Optional. The user id. | [optional] 
 **audio_codec** | **str**| Optional. The audio codec to transcode to. | [optional] 
 **max_audio_channels** | **int**| Optional. The maximum number of audio channels. | [optional] 
 **transcoding_audio_channels** | **int**| Optional. The number of how many audio channels to transcode to. | [optional] 
 **max_streaming_bitrate** | **int**| Optional. The maximum streaming bitrate. | [optional] 
 **audio_bit_rate** | **int**| Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1 tick &#x3D; 10000 ms. | [optional] 
 **transcoding_container** | **str**| Optional. The container to transcode to. | [optional] 
 **transcoding_protocol** | **MediaStreamProtocol**| Optional. The transcoding protocol. | [optional] 
 **max_audio_sample_rate** | **int**| Optional. The maximum audio sample rate. | [optional] 
 **max_audio_bit_depth** | **int**| Optional. The maximum audio bit depth. | [optional] 
 **enable_remote_media** | **bool**| Optional. Whether to enable remote media. | [optional] 
 **enable_audio_vbr_encoding** | **bool**| Optional. Whether to enable Audio Encoding. | [optional] [default to True]
 **break_on_non_key_frames** | **bool**| Optional. Whether to break on non key frames. | [optional] [default to False]
 **enable_redirection** | **bool**| Whether to enable redirection. Defaults to true. | [optional] [default to True]

### Return type

**bytearray**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: audio/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Audio stream returned. |  -  |
**302** | Redirected to remote audio stream. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

