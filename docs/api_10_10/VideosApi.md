# jellyfin.generated.api_10_10.VideosApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_alternate_sources**](VideosApi.md#delete_alternate_sources) | **DELETE** /Videos/{itemId}/AlternateSources | Removes alternate video sources.
[**get_additional_part**](VideosApi.md#get_additional_part) | **GET** /Videos/{itemId}/AdditionalParts | Gets additional parts for a video.
[**get_video_stream**](VideosApi.md#get_video_stream) | **GET** /Videos/{itemId}/stream | Gets a video stream.
[**get_video_stream_by_container**](VideosApi.md#get_video_stream_by_container) | **GET** /Videos/{itemId}/stream.{container} | Gets a video stream.
[**head_video_stream**](VideosApi.md#head_video_stream) | **HEAD** /Videos/{itemId}/stream | Gets a video stream.
[**head_video_stream_by_container**](VideosApi.md#head_video_stream_by_container) | **HEAD** /Videos/{itemId}/stream.{container} | Gets a video stream.
[**merge_versions**](VideosApi.md#merge_versions) | **POST** /Videos/MergeVersions | Merges videos into a single record.


# **delete_alternate_sources**
> delete_alternate_sources(item_id)

Removes alternate video sources.

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
    api_instance = jellyfin.generated.api_10_10.VideosApi(api_client)
    item_id = 'item_id_example' # str | The item id.

    try:
        # Removes alternate video sources.
        api_instance.delete_alternate_sources(item_id)
    except Exception as e:
        print("Exception when calling VideosApi->delete_alternate_sources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 

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
**204** | Alternate sources deleted. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Video not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_additional_part**
> BaseItemDtoQueryResult get_additional_part(item_id, user_id=user_id)

Gets additional parts for a video.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.base_item_dto_query_result import BaseItemDtoQueryResult
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
    api_instance = jellyfin.generated.api_10_10.VideosApi(api_client)
    item_id = 'item_id_example' # str | The item id.
    user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data. (optional)

    try:
        # Gets additional parts for a video.
        api_response = api_instance.get_additional_part(item_id, user_id=user_id)
        print("The response of VideosApi->get_additional_part:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->get_additional_part: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **user_id** | **str**| Optional. Filter by user id, and attach user data. | [optional] 

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
**200** | Additional parts returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video_stream**
> bytearray get_video_stream(item_id, container=container, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, media_source_id=media_source_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, enable_audio_vbr_encoding=enable_audio_vbr_encoding)

Gets a video stream.

### Example


```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.encoding_context import EncodingContext
from jellyfin.generated.api_10_10.models.subtitle_delivery_method import SubtitleDeliveryMethod
from jellyfin.generated.api_10_10.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jellyfin.generated.api_10_10.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with jellyfin.generated.api_10_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jellyfin.generated.api_10_10.VideosApi(api_client)
    item_id = 'item_id_example' # str | The item id.
    container = 'container_example' # str | The video container. Possible values are: ts, webm, asf, wmv, ogv, mp4, m4v, mkv, mpeg, mpg, avi, 3gp, wmv, wtv, m2ts, mov, iso, flv. (optional)
    static = True # bool | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false. (optional)
    params = 'params_example' # str | The streaming parameters. (optional)
    tag = 'tag_example' # str | The tag. (optional)
    device_profile_id = 'device_profile_id_example' # str | Optional. The dlna device profile id to utilize. (optional)
    play_session_id = 'play_session_id_example' # str | The play session id. (optional)
    segment_container = 'segment_container_example' # str | The segment container. (optional)
    segment_length = 56 # int | The segment length. (optional)
    min_segments = 56 # int | The minimum number of segments. (optional)
    media_source_id = 'media_source_id_example' # str | The media version id, if playing an alternate version. (optional)
    device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
    audio_codec = 'audio_codec_example' # str | Optional. Specify an audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. (optional)
    enable_auto_stream_copy = True # bool | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. (optional)
    allow_video_stream_copy = True # bool | Whether or not to allow copying of the video stream url. (optional)
    allow_audio_stream_copy = True # bool | Whether or not to allow copying of the audio stream url. (optional)
    break_on_non_key_frames = True # bool | Optional. Whether to break on non key frames. (optional)
    audio_sample_rate = 56 # int | Optional. Specify a specific audio sample rate, e.g. 44100. (optional)
    max_audio_bit_depth = 56 # int | Optional. The maximum audio bit depth. (optional)
    audio_bit_rate = 56 # int | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. (optional)
    audio_channels = 56 # int | Optional. Specify a specific number of audio channels to encode to, e.g. 2. (optional)
    max_audio_channels = 56 # int | Optional. Specify a maximum number of audio channels to encode to, e.g. 2. (optional)
    profile = 'profile_example' # str | Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high. (optional)
    level = 'level_example' # str | Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1. (optional)
    framerate = 3.4 # float | Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. (optional)
    max_framerate = 3.4 # float | Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. (optional)
    copy_timestamps = True # bool | Whether or not to copy timestamps when transcoding with an offset. Defaults to false. (optional)
    start_time_ticks = 56 # int | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms. (optional)
    width = 56 # int | Optional. The fixed horizontal resolution of the encoded video. (optional)
    height = 56 # int | Optional. The fixed vertical resolution of the encoded video. (optional)
    max_width = 56 # int | Optional. The maximum horizontal resolution of the encoded video. (optional)
    max_height = 56 # int | Optional. The maximum vertical resolution of the encoded video. (optional)
    video_bit_rate = 56 # int | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. (optional)
    subtitle_stream_index = 56 # int | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. (optional)
    subtitle_method = jellyfin.generated.api_10_10.SubtitleDeliveryMethod() # SubtitleDeliveryMethod | Optional. Specify the subtitle delivery method. (optional)
    max_ref_frames = 56 # int | Optional. (optional)
    max_video_bit_depth = 56 # int | Optional. The maximum video bit depth. (optional)
    require_avc = True # bool | Optional. Whether to require avc. (optional)
    de_interlace = True # bool | Optional. Whether to deinterlace the video. (optional)
    require_non_anamorphic = True # bool | Optional. Whether to require a non anamorphic stream. (optional)
    transcoding_max_audio_channels = 56 # int | Optional. The maximum number of audio channels to transcode. (optional)
    cpu_core_limit = 56 # int | Optional. The limit of how many cpu cores to use. (optional)
    live_stream_id = 'live_stream_id_example' # str | The live stream id. (optional)
    enable_mpegts_m2_ts_mode = True # bool | Optional. Whether to enable the MpegtsM2Ts mode. (optional)
    video_codec = 'video_codec_example' # str | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. (optional)
    subtitle_codec = 'subtitle_codec_example' # str | Optional. Specify a subtitle codec to encode to. (optional)
    transcode_reasons = 'transcode_reasons_example' # str | Optional. The transcoding reason. (optional)
    audio_stream_index = 56 # int | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. (optional)
    video_stream_index = 56 # int | Optional. The index of the video stream to use. If omitted the first video stream will be used. (optional)
    context = jellyfin.generated.api_10_10.EncodingContext() # EncodingContext | Optional. The MediaBrowser.Model.Dlna.EncodingContext. (optional)
    stream_options = {'key': 'stream_options_example'} # Dict[str, Optional[str]] | Optional. The streaming options. (optional)
    enable_audio_vbr_encoding = True # bool | Optional. Whether to enable Audio Encoding. (optional) (default to True)

    try:
        # Gets a video stream.
        api_response = api_instance.get_video_stream(item_id, container=container, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, media_source_id=media_source_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, enable_audio_vbr_encoding=enable_audio_vbr_encoding)
        print("The response of VideosApi->get_video_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->get_video_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **container** | **str**| The video container. Possible values are: ts, webm, asf, wmv, ogv, mp4, m4v, mkv, mpeg, mpg, avi, 3gp, wmv, wtv, m2ts, mov, iso, flv. | [optional] 
 **static** | **bool**| Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false. | [optional] 
 **params** | **str**| The streaming parameters. | [optional] 
 **tag** | **str**| The tag. | [optional] 
 **device_profile_id** | **str**| Optional. The dlna device profile id to utilize. | [optional] 
 **play_session_id** | **str**| The play session id. | [optional] 
 **segment_container** | **str**| The segment container. | [optional] 
 **segment_length** | **int**| The segment length. | [optional] 
 **min_segments** | **int**| The minimum number of segments. | [optional] 
 **media_source_id** | **str**| The media version id, if playing an alternate version. | [optional] 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **audio_codec** | **str**| Optional. Specify an audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url&#39;s extension. | [optional] 
 **enable_auto_stream_copy** | **bool**| Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. | [optional] 
 **allow_video_stream_copy** | **bool**| Whether or not to allow copying of the video stream url. | [optional] 
 **allow_audio_stream_copy** | **bool**| Whether or not to allow copying of the audio stream url. | [optional] 
 **break_on_non_key_frames** | **bool**| Optional. Whether to break on non key frames. | [optional] 
 **audio_sample_rate** | **int**| Optional. Specify a specific audio sample rate, e.g. 44100. | [optional] 
 **max_audio_bit_depth** | **int**| Optional. The maximum audio bit depth. | [optional] 
 **audio_bit_rate** | **int**| Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. | [optional] 
 **audio_channels** | **int**| Optional. Specify a specific number of audio channels to encode to, e.g. 2. | [optional] 
 **max_audio_channels** | **int**| Optional. Specify a maximum number of audio channels to encode to, e.g. 2. | [optional] 
 **profile** | **str**| Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high. | [optional] 
 **level** | **str**| Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1. | [optional] 
 **framerate** | **float**| Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **max_framerate** | **float**| Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **copy_timestamps** | **bool**| Whether or not to copy timestamps when transcoding with an offset. Defaults to false. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1 tick &#x3D; 10000 ms. | [optional] 
 **width** | **int**| Optional. The fixed horizontal resolution of the encoded video. | [optional] 
 **height** | **int**| Optional. The fixed vertical resolution of the encoded video. | [optional] 
 **max_width** | **int**| Optional. The maximum horizontal resolution of the encoded video. | [optional] 
 **max_height** | **int**| Optional. The maximum vertical resolution of the encoded video. | [optional] 
 **video_bit_rate** | **int**| Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. | [optional] 
 **subtitle_stream_index** | **int**| Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. | [optional] 
 **subtitle_method** | [**SubtitleDeliveryMethod**](.md)| Optional. Specify the subtitle delivery method. | [optional] 
 **max_ref_frames** | **int**| Optional. | [optional] 
 **max_video_bit_depth** | **int**| Optional. The maximum video bit depth. | [optional] 
 **require_avc** | **bool**| Optional. Whether to require avc. | [optional] 
 **de_interlace** | **bool**| Optional. Whether to deinterlace the video. | [optional] 
 **require_non_anamorphic** | **bool**| Optional. Whether to require a non anamorphic stream. | [optional] 
 **transcoding_max_audio_channels** | **int**| Optional. The maximum number of audio channels to transcode. | [optional] 
 **cpu_core_limit** | **int**| Optional. The limit of how many cpu cores to use. | [optional] 
 **live_stream_id** | **str**| The live stream id. | [optional] 
 **enable_mpegts_m2_ts_mode** | **bool**| Optional. Whether to enable the MpegtsM2Ts mode. | [optional] 
 **video_codec** | **str**| Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url&#39;s extension. | [optional] 
 **subtitle_codec** | **str**| Optional. Specify a subtitle codec to encode to. | [optional] 
 **transcode_reasons** | **str**| Optional. The transcoding reason. | [optional] 
 **audio_stream_index** | **int**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **video_stream_index** | **int**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 
 **context** | [**EncodingContext**](.md)| Optional. The MediaBrowser.Model.Dlna.EncodingContext. | [optional] 
 **stream_options** | [**Dict[str, Optional[str]]**](str.md)| Optional. The streaming options. | [optional] 
 **enable_audio_vbr_encoding** | **bool**| Optional. Whether to enable Audio Encoding. | [optional] [default to True]

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: video/*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Video stream returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video_stream_by_container**
> bytearray get_video_stream_by_container(item_id, container, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, media_source_id=media_source_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, enable_audio_vbr_encoding=enable_audio_vbr_encoding)

Gets a video stream.

### Example


```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.encoding_context import EncodingContext
from jellyfin.generated.api_10_10.models.subtitle_delivery_method import SubtitleDeliveryMethod
from jellyfin.generated.api_10_10.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jellyfin.generated.api_10_10.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with jellyfin.generated.api_10_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jellyfin.generated.api_10_10.VideosApi(api_client)
    item_id = 'item_id_example' # str | The item id.
    container = 'container_example' # str | The video container. Possible values are: ts, webm, asf, wmv, ogv, mp4, m4v, mkv, mpeg, mpg, avi, 3gp, wmv, wtv, m2ts, mov, iso, flv.
    static = True # bool | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false. (optional)
    params = 'params_example' # str | The streaming parameters. (optional)
    tag = 'tag_example' # str | The tag. (optional)
    device_profile_id = 'device_profile_id_example' # str | Optional. The dlna device profile id to utilize. (optional)
    play_session_id = 'play_session_id_example' # str | The play session id. (optional)
    segment_container = 'segment_container_example' # str | The segment container. (optional)
    segment_length = 56 # int | The segment length. (optional)
    min_segments = 56 # int | The minimum number of segments. (optional)
    media_source_id = 'media_source_id_example' # str | The media version id, if playing an alternate version. (optional)
    device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
    audio_codec = 'audio_codec_example' # str | Optional. Specify an audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. (optional)
    enable_auto_stream_copy = True # bool | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. (optional)
    allow_video_stream_copy = True # bool | Whether or not to allow copying of the video stream url. (optional)
    allow_audio_stream_copy = True # bool | Whether or not to allow copying of the audio stream url. (optional)
    break_on_non_key_frames = True # bool | Optional. Whether to break on non key frames. (optional)
    audio_sample_rate = 56 # int | Optional. Specify a specific audio sample rate, e.g. 44100. (optional)
    max_audio_bit_depth = 56 # int | Optional. The maximum audio bit depth. (optional)
    audio_bit_rate = 56 # int | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. (optional)
    audio_channels = 56 # int | Optional. Specify a specific number of audio channels to encode to, e.g. 2. (optional)
    max_audio_channels = 56 # int | Optional. Specify a maximum number of audio channels to encode to, e.g. 2. (optional)
    profile = 'profile_example' # str | Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high. (optional)
    level = 'level_example' # str | Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1. (optional)
    framerate = 3.4 # float | Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. (optional)
    max_framerate = 3.4 # float | Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. (optional)
    copy_timestamps = True # bool | Whether or not to copy timestamps when transcoding with an offset. Defaults to false. (optional)
    start_time_ticks = 56 # int | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms. (optional)
    width = 56 # int | Optional. The fixed horizontal resolution of the encoded video. (optional)
    height = 56 # int | Optional. The fixed vertical resolution of the encoded video. (optional)
    max_width = 56 # int | Optional. The maximum horizontal resolution of the encoded video. (optional)
    max_height = 56 # int | Optional. The maximum vertical resolution of the encoded video. (optional)
    video_bit_rate = 56 # int | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. (optional)
    subtitle_stream_index = 56 # int | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. (optional)
    subtitle_method = jellyfin.generated.api_10_10.SubtitleDeliveryMethod() # SubtitleDeliveryMethod | Optional. Specify the subtitle delivery method. (optional)
    max_ref_frames = 56 # int | Optional. (optional)
    max_video_bit_depth = 56 # int | Optional. The maximum video bit depth. (optional)
    require_avc = True # bool | Optional. Whether to require avc. (optional)
    de_interlace = True # bool | Optional. Whether to deinterlace the video. (optional)
    require_non_anamorphic = True # bool | Optional. Whether to require a non anamorphic stream. (optional)
    transcoding_max_audio_channels = 56 # int | Optional. The maximum number of audio channels to transcode. (optional)
    cpu_core_limit = 56 # int | Optional. The limit of how many cpu cores to use. (optional)
    live_stream_id = 'live_stream_id_example' # str | The live stream id. (optional)
    enable_mpegts_m2_ts_mode = True # bool | Optional. Whether to enable the MpegtsM2Ts mode. (optional)
    video_codec = 'video_codec_example' # str | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. (optional)
    subtitle_codec = 'subtitle_codec_example' # str | Optional. Specify a subtitle codec to encode to. (optional)
    transcode_reasons = 'transcode_reasons_example' # str | Optional. The transcoding reason. (optional)
    audio_stream_index = 56 # int | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. (optional)
    video_stream_index = 56 # int | Optional. The index of the video stream to use. If omitted the first video stream will be used. (optional)
    context = jellyfin.generated.api_10_10.EncodingContext() # EncodingContext | Optional. The MediaBrowser.Model.Dlna.EncodingContext. (optional)
    stream_options = {'key': 'stream_options_example'} # Dict[str, Optional[str]] | Optional. The streaming options. (optional)
    enable_audio_vbr_encoding = True # bool | Optional. Whether to enable Audio Encoding. (optional) (default to True)

    try:
        # Gets a video stream.
        api_response = api_instance.get_video_stream_by_container(item_id, container, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, media_source_id=media_source_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, enable_audio_vbr_encoding=enable_audio_vbr_encoding)
        print("The response of VideosApi->get_video_stream_by_container:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->get_video_stream_by_container: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **container** | **str**| The video container. Possible values are: ts, webm, asf, wmv, ogv, mp4, m4v, mkv, mpeg, mpg, avi, 3gp, wmv, wtv, m2ts, mov, iso, flv. | 
 **static** | **bool**| Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false. | [optional] 
 **params** | **str**| The streaming parameters. | [optional] 
 **tag** | **str**| The tag. | [optional] 
 **device_profile_id** | **str**| Optional. The dlna device profile id to utilize. | [optional] 
 **play_session_id** | **str**| The play session id. | [optional] 
 **segment_container** | **str**| The segment container. | [optional] 
 **segment_length** | **int**| The segment length. | [optional] 
 **min_segments** | **int**| The minimum number of segments. | [optional] 
 **media_source_id** | **str**| The media version id, if playing an alternate version. | [optional] 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **audio_codec** | **str**| Optional. Specify an audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url&#39;s extension. | [optional] 
 **enable_auto_stream_copy** | **bool**| Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. | [optional] 
 **allow_video_stream_copy** | **bool**| Whether or not to allow copying of the video stream url. | [optional] 
 **allow_audio_stream_copy** | **bool**| Whether or not to allow copying of the audio stream url. | [optional] 
 **break_on_non_key_frames** | **bool**| Optional. Whether to break on non key frames. | [optional] 
 **audio_sample_rate** | **int**| Optional. Specify a specific audio sample rate, e.g. 44100. | [optional] 
 **max_audio_bit_depth** | **int**| Optional. The maximum audio bit depth. | [optional] 
 **audio_bit_rate** | **int**| Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. | [optional] 
 **audio_channels** | **int**| Optional. Specify a specific number of audio channels to encode to, e.g. 2. | [optional] 
 **max_audio_channels** | **int**| Optional. Specify a maximum number of audio channels to encode to, e.g. 2. | [optional] 
 **profile** | **str**| Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high. | [optional] 
 **level** | **str**| Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1. | [optional] 
 **framerate** | **float**| Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **max_framerate** | **float**| Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **copy_timestamps** | **bool**| Whether or not to copy timestamps when transcoding with an offset. Defaults to false. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1 tick &#x3D; 10000 ms. | [optional] 
 **width** | **int**| Optional. The fixed horizontal resolution of the encoded video. | [optional] 
 **height** | **int**| Optional. The fixed vertical resolution of the encoded video. | [optional] 
 **max_width** | **int**| Optional. The maximum horizontal resolution of the encoded video. | [optional] 
 **max_height** | **int**| Optional. The maximum vertical resolution of the encoded video. | [optional] 
 **video_bit_rate** | **int**| Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. | [optional] 
 **subtitle_stream_index** | **int**| Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. | [optional] 
 **subtitle_method** | [**SubtitleDeliveryMethod**](.md)| Optional. Specify the subtitle delivery method. | [optional] 
 **max_ref_frames** | **int**| Optional. | [optional] 
 **max_video_bit_depth** | **int**| Optional. The maximum video bit depth. | [optional] 
 **require_avc** | **bool**| Optional. Whether to require avc. | [optional] 
 **de_interlace** | **bool**| Optional. Whether to deinterlace the video. | [optional] 
 **require_non_anamorphic** | **bool**| Optional. Whether to require a non anamorphic stream. | [optional] 
 **transcoding_max_audio_channels** | **int**| Optional. The maximum number of audio channels to transcode. | [optional] 
 **cpu_core_limit** | **int**| Optional. The limit of how many cpu cores to use. | [optional] 
 **live_stream_id** | **str**| The live stream id. | [optional] 
 **enable_mpegts_m2_ts_mode** | **bool**| Optional. Whether to enable the MpegtsM2Ts mode. | [optional] 
 **video_codec** | **str**| Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url&#39;s extension. | [optional] 
 **subtitle_codec** | **str**| Optional. Specify a subtitle codec to encode to. | [optional] 
 **transcode_reasons** | **str**| Optional. The transcoding reason. | [optional] 
 **audio_stream_index** | **int**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **video_stream_index** | **int**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 
 **context** | [**EncodingContext**](.md)| Optional. The MediaBrowser.Model.Dlna.EncodingContext. | [optional] 
 **stream_options** | [**Dict[str, Optional[str]]**](str.md)| Optional. The streaming options. | [optional] 
 **enable_audio_vbr_encoding** | **bool**| Optional. Whether to enable Audio Encoding. | [optional] [default to True]

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: video/*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Video stream returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_video_stream**
> bytearray head_video_stream(item_id, container=container, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, media_source_id=media_source_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, enable_audio_vbr_encoding=enable_audio_vbr_encoding)

Gets a video stream.

### Example


```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.encoding_context import EncodingContext
from jellyfin.generated.api_10_10.models.subtitle_delivery_method import SubtitleDeliveryMethod
from jellyfin.generated.api_10_10.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jellyfin.generated.api_10_10.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with jellyfin.generated.api_10_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jellyfin.generated.api_10_10.VideosApi(api_client)
    item_id = 'item_id_example' # str | The item id.
    container = 'container_example' # str | The video container. Possible values are: ts, webm, asf, wmv, ogv, mp4, m4v, mkv, mpeg, mpg, avi, 3gp, wmv, wtv, m2ts, mov, iso, flv. (optional)
    static = True # bool | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false. (optional)
    params = 'params_example' # str | The streaming parameters. (optional)
    tag = 'tag_example' # str | The tag. (optional)
    device_profile_id = 'device_profile_id_example' # str | Optional. The dlna device profile id to utilize. (optional)
    play_session_id = 'play_session_id_example' # str | The play session id. (optional)
    segment_container = 'segment_container_example' # str | The segment container. (optional)
    segment_length = 56 # int | The segment length. (optional)
    min_segments = 56 # int | The minimum number of segments. (optional)
    media_source_id = 'media_source_id_example' # str | The media version id, if playing an alternate version. (optional)
    device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
    audio_codec = 'audio_codec_example' # str | Optional. Specify an audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. (optional)
    enable_auto_stream_copy = True # bool | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. (optional)
    allow_video_stream_copy = True # bool | Whether or not to allow copying of the video stream url. (optional)
    allow_audio_stream_copy = True # bool | Whether or not to allow copying of the audio stream url. (optional)
    break_on_non_key_frames = True # bool | Optional. Whether to break on non key frames. (optional)
    audio_sample_rate = 56 # int | Optional. Specify a specific audio sample rate, e.g. 44100. (optional)
    max_audio_bit_depth = 56 # int | Optional. The maximum audio bit depth. (optional)
    audio_bit_rate = 56 # int | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. (optional)
    audio_channels = 56 # int | Optional. Specify a specific number of audio channels to encode to, e.g. 2. (optional)
    max_audio_channels = 56 # int | Optional. Specify a maximum number of audio channels to encode to, e.g. 2. (optional)
    profile = 'profile_example' # str | Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high. (optional)
    level = 'level_example' # str | Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1. (optional)
    framerate = 3.4 # float | Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. (optional)
    max_framerate = 3.4 # float | Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. (optional)
    copy_timestamps = True # bool | Whether or not to copy timestamps when transcoding with an offset. Defaults to false. (optional)
    start_time_ticks = 56 # int | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms. (optional)
    width = 56 # int | Optional. The fixed horizontal resolution of the encoded video. (optional)
    height = 56 # int | Optional. The fixed vertical resolution of the encoded video. (optional)
    max_width = 56 # int | Optional. The maximum horizontal resolution of the encoded video. (optional)
    max_height = 56 # int | Optional. The maximum vertical resolution of the encoded video. (optional)
    video_bit_rate = 56 # int | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. (optional)
    subtitle_stream_index = 56 # int | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. (optional)
    subtitle_method = jellyfin.generated.api_10_10.SubtitleDeliveryMethod() # SubtitleDeliveryMethod | Optional. Specify the subtitle delivery method. (optional)
    max_ref_frames = 56 # int | Optional. (optional)
    max_video_bit_depth = 56 # int | Optional. The maximum video bit depth. (optional)
    require_avc = True # bool | Optional. Whether to require avc. (optional)
    de_interlace = True # bool | Optional. Whether to deinterlace the video. (optional)
    require_non_anamorphic = True # bool | Optional. Whether to require a non anamorphic stream. (optional)
    transcoding_max_audio_channels = 56 # int | Optional. The maximum number of audio channels to transcode. (optional)
    cpu_core_limit = 56 # int | Optional. The limit of how many cpu cores to use. (optional)
    live_stream_id = 'live_stream_id_example' # str | The live stream id. (optional)
    enable_mpegts_m2_ts_mode = True # bool | Optional. Whether to enable the MpegtsM2Ts mode. (optional)
    video_codec = 'video_codec_example' # str | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. (optional)
    subtitle_codec = 'subtitle_codec_example' # str | Optional. Specify a subtitle codec to encode to. (optional)
    transcode_reasons = 'transcode_reasons_example' # str | Optional. The transcoding reason. (optional)
    audio_stream_index = 56 # int | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. (optional)
    video_stream_index = 56 # int | Optional. The index of the video stream to use. If omitted the first video stream will be used. (optional)
    context = jellyfin.generated.api_10_10.EncodingContext() # EncodingContext | Optional. The MediaBrowser.Model.Dlna.EncodingContext. (optional)
    stream_options = {'key': 'stream_options_example'} # Dict[str, Optional[str]] | Optional. The streaming options. (optional)
    enable_audio_vbr_encoding = True # bool | Optional. Whether to enable Audio Encoding. (optional) (default to True)

    try:
        # Gets a video stream.
        api_response = api_instance.head_video_stream(item_id, container=container, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, media_source_id=media_source_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, enable_audio_vbr_encoding=enable_audio_vbr_encoding)
        print("The response of VideosApi->head_video_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->head_video_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **container** | **str**| The video container. Possible values are: ts, webm, asf, wmv, ogv, mp4, m4v, mkv, mpeg, mpg, avi, 3gp, wmv, wtv, m2ts, mov, iso, flv. | [optional] 
 **static** | **bool**| Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false. | [optional] 
 **params** | **str**| The streaming parameters. | [optional] 
 **tag** | **str**| The tag. | [optional] 
 **device_profile_id** | **str**| Optional. The dlna device profile id to utilize. | [optional] 
 **play_session_id** | **str**| The play session id. | [optional] 
 **segment_container** | **str**| The segment container. | [optional] 
 **segment_length** | **int**| The segment length. | [optional] 
 **min_segments** | **int**| The minimum number of segments. | [optional] 
 **media_source_id** | **str**| The media version id, if playing an alternate version. | [optional] 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **audio_codec** | **str**| Optional. Specify an audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url&#39;s extension. | [optional] 
 **enable_auto_stream_copy** | **bool**| Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. | [optional] 
 **allow_video_stream_copy** | **bool**| Whether or not to allow copying of the video stream url. | [optional] 
 **allow_audio_stream_copy** | **bool**| Whether or not to allow copying of the audio stream url. | [optional] 
 **break_on_non_key_frames** | **bool**| Optional. Whether to break on non key frames. | [optional] 
 **audio_sample_rate** | **int**| Optional. Specify a specific audio sample rate, e.g. 44100. | [optional] 
 **max_audio_bit_depth** | **int**| Optional. The maximum audio bit depth. | [optional] 
 **audio_bit_rate** | **int**| Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. | [optional] 
 **audio_channels** | **int**| Optional. Specify a specific number of audio channels to encode to, e.g. 2. | [optional] 
 **max_audio_channels** | **int**| Optional. Specify a maximum number of audio channels to encode to, e.g. 2. | [optional] 
 **profile** | **str**| Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high. | [optional] 
 **level** | **str**| Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1. | [optional] 
 **framerate** | **float**| Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **max_framerate** | **float**| Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **copy_timestamps** | **bool**| Whether or not to copy timestamps when transcoding with an offset. Defaults to false. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1 tick &#x3D; 10000 ms. | [optional] 
 **width** | **int**| Optional. The fixed horizontal resolution of the encoded video. | [optional] 
 **height** | **int**| Optional. The fixed vertical resolution of the encoded video. | [optional] 
 **max_width** | **int**| Optional. The maximum horizontal resolution of the encoded video. | [optional] 
 **max_height** | **int**| Optional. The maximum vertical resolution of the encoded video. | [optional] 
 **video_bit_rate** | **int**| Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. | [optional] 
 **subtitle_stream_index** | **int**| Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. | [optional] 
 **subtitle_method** | [**SubtitleDeliveryMethod**](.md)| Optional. Specify the subtitle delivery method. | [optional] 
 **max_ref_frames** | **int**| Optional. | [optional] 
 **max_video_bit_depth** | **int**| Optional. The maximum video bit depth. | [optional] 
 **require_avc** | **bool**| Optional. Whether to require avc. | [optional] 
 **de_interlace** | **bool**| Optional. Whether to deinterlace the video. | [optional] 
 **require_non_anamorphic** | **bool**| Optional. Whether to require a non anamorphic stream. | [optional] 
 **transcoding_max_audio_channels** | **int**| Optional. The maximum number of audio channels to transcode. | [optional] 
 **cpu_core_limit** | **int**| Optional. The limit of how many cpu cores to use. | [optional] 
 **live_stream_id** | **str**| The live stream id. | [optional] 
 **enable_mpegts_m2_ts_mode** | **bool**| Optional. Whether to enable the MpegtsM2Ts mode. | [optional] 
 **video_codec** | **str**| Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url&#39;s extension. | [optional] 
 **subtitle_codec** | **str**| Optional. Specify a subtitle codec to encode to. | [optional] 
 **transcode_reasons** | **str**| Optional. The transcoding reason. | [optional] 
 **audio_stream_index** | **int**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **video_stream_index** | **int**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 
 **context** | [**EncodingContext**](.md)| Optional. The MediaBrowser.Model.Dlna.EncodingContext. | [optional] 
 **stream_options** | [**Dict[str, Optional[str]]**](str.md)| Optional. The streaming options. | [optional] 
 **enable_audio_vbr_encoding** | **bool**| Optional. Whether to enable Audio Encoding. | [optional] [default to True]

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: video/*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Video stream returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_video_stream_by_container**
> bytearray head_video_stream_by_container(item_id, container, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, media_source_id=media_source_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, enable_audio_vbr_encoding=enable_audio_vbr_encoding)

Gets a video stream.

### Example


```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.encoding_context import EncodingContext
from jellyfin.generated.api_10_10.models.subtitle_delivery_method import SubtitleDeliveryMethod
from jellyfin.generated.api_10_10.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jellyfin.generated.api_10_10.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with jellyfin.generated.api_10_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jellyfin.generated.api_10_10.VideosApi(api_client)
    item_id = 'item_id_example' # str | The item id.
    container = 'container_example' # str | The video container. Possible values are: ts, webm, asf, wmv, ogv, mp4, m4v, mkv, mpeg, mpg, avi, 3gp, wmv, wtv, m2ts, mov, iso, flv.
    static = True # bool | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false. (optional)
    params = 'params_example' # str | The streaming parameters. (optional)
    tag = 'tag_example' # str | The tag. (optional)
    device_profile_id = 'device_profile_id_example' # str | Optional. The dlna device profile id to utilize. (optional)
    play_session_id = 'play_session_id_example' # str | The play session id. (optional)
    segment_container = 'segment_container_example' # str | The segment container. (optional)
    segment_length = 56 # int | The segment length. (optional)
    min_segments = 56 # int | The minimum number of segments. (optional)
    media_source_id = 'media_source_id_example' # str | The media version id, if playing an alternate version. (optional)
    device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
    audio_codec = 'audio_codec_example' # str | Optional. Specify an audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. (optional)
    enable_auto_stream_copy = True # bool | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. (optional)
    allow_video_stream_copy = True # bool | Whether or not to allow copying of the video stream url. (optional)
    allow_audio_stream_copy = True # bool | Whether or not to allow copying of the audio stream url. (optional)
    break_on_non_key_frames = True # bool | Optional. Whether to break on non key frames. (optional)
    audio_sample_rate = 56 # int | Optional. Specify a specific audio sample rate, e.g. 44100. (optional)
    max_audio_bit_depth = 56 # int | Optional. The maximum audio bit depth. (optional)
    audio_bit_rate = 56 # int | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. (optional)
    audio_channels = 56 # int | Optional. Specify a specific number of audio channels to encode to, e.g. 2. (optional)
    max_audio_channels = 56 # int | Optional. Specify a maximum number of audio channels to encode to, e.g. 2. (optional)
    profile = 'profile_example' # str | Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high. (optional)
    level = 'level_example' # str | Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1. (optional)
    framerate = 3.4 # float | Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. (optional)
    max_framerate = 3.4 # float | Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. (optional)
    copy_timestamps = True # bool | Whether or not to copy timestamps when transcoding with an offset. Defaults to false. (optional)
    start_time_ticks = 56 # int | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms. (optional)
    width = 56 # int | Optional. The fixed horizontal resolution of the encoded video. (optional)
    height = 56 # int | Optional. The fixed vertical resolution of the encoded video. (optional)
    max_width = 56 # int | Optional. The maximum horizontal resolution of the encoded video. (optional)
    max_height = 56 # int | Optional. The maximum vertical resolution of the encoded video. (optional)
    video_bit_rate = 56 # int | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. (optional)
    subtitle_stream_index = 56 # int | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. (optional)
    subtitle_method = jellyfin.generated.api_10_10.SubtitleDeliveryMethod() # SubtitleDeliveryMethod | Optional. Specify the subtitle delivery method. (optional)
    max_ref_frames = 56 # int | Optional. (optional)
    max_video_bit_depth = 56 # int | Optional. The maximum video bit depth. (optional)
    require_avc = True # bool | Optional. Whether to require avc. (optional)
    de_interlace = True # bool | Optional. Whether to deinterlace the video. (optional)
    require_non_anamorphic = True # bool | Optional. Whether to require a non anamorphic stream. (optional)
    transcoding_max_audio_channels = 56 # int | Optional. The maximum number of audio channels to transcode. (optional)
    cpu_core_limit = 56 # int | Optional. The limit of how many cpu cores to use. (optional)
    live_stream_id = 'live_stream_id_example' # str | The live stream id. (optional)
    enable_mpegts_m2_ts_mode = True # bool | Optional. Whether to enable the MpegtsM2Ts mode. (optional)
    video_codec = 'video_codec_example' # str | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. (optional)
    subtitle_codec = 'subtitle_codec_example' # str | Optional. Specify a subtitle codec to encode to. (optional)
    transcode_reasons = 'transcode_reasons_example' # str | Optional. The transcoding reason. (optional)
    audio_stream_index = 56 # int | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. (optional)
    video_stream_index = 56 # int | Optional. The index of the video stream to use. If omitted the first video stream will be used. (optional)
    context = jellyfin.generated.api_10_10.EncodingContext() # EncodingContext | Optional. The MediaBrowser.Model.Dlna.EncodingContext. (optional)
    stream_options = {'key': 'stream_options_example'} # Dict[str, Optional[str]] | Optional. The streaming options. (optional)
    enable_audio_vbr_encoding = True # bool | Optional. Whether to enable Audio Encoding. (optional) (default to True)

    try:
        # Gets a video stream.
        api_response = api_instance.head_video_stream_by_container(item_id, container, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, media_source_id=media_source_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, enable_audio_vbr_encoding=enable_audio_vbr_encoding)
        print("The response of VideosApi->head_video_stream_by_container:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->head_video_stream_by_container: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **container** | **str**| The video container. Possible values are: ts, webm, asf, wmv, ogv, mp4, m4v, mkv, mpeg, mpg, avi, 3gp, wmv, wtv, m2ts, mov, iso, flv. | 
 **static** | **bool**| Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false. | [optional] 
 **params** | **str**| The streaming parameters. | [optional] 
 **tag** | **str**| The tag. | [optional] 
 **device_profile_id** | **str**| Optional. The dlna device profile id to utilize. | [optional] 
 **play_session_id** | **str**| The play session id. | [optional] 
 **segment_container** | **str**| The segment container. | [optional] 
 **segment_length** | **int**| The segment length. | [optional] 
 **min_segments** | **int**| The minimum number of segments. | [optional] 
 **media_source_id** | **str**| The media version id, if playing an alternate version. | [optional] 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **audio_codec** | **str**| Optional. Specify an audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url&#39;s extension. | [optional] 
 **enable_auto_stream_copy** | **bool**| Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. | [optional] 
 **allow_video_stream_copy** | **bool**| Whether or not to allow copying of the video stream url. | [optional] 
 **allow_audio_stream_copy** | **bool**| Whether or not to allow copying of the audio stream url. | [optional] 
 **break_on_non_key_frames** | **bool**| Optional. Whether to break on non key frames. | [optional] 
 **audio_sample_rate** | **int**| Optional. Specify a specific audio sample rate, e.g. 44100. | [optional] 
 **max_audio_bit_depth** | **int**| Optional. The maximum audio bit depth. | [optional] 
 **audio_bit_rate** | **int**| Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. | [optional] 
 **audio_channels** | **int**| Optional. Specify a specific number of audio channels to encode to, e.g. 2. | [optional] 
 **max_audio_channels** | **int**| Optional. Specify a maximum number of audio channels to encode to, e.g. 2. | [optional] 
 **profile** | **str**| Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high. | [optional] 
 **level** | **str**| Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1. | [optional] 
 **framerate** | **float**| Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **max_framerate** | **float**| Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **copy_timestamps** | **bool**| Whether or not to copy timestamps when transcoding with an offset. Defaults to false. | [optional] 
 **start_time_ticks** | **int**| Optional. Specify a starting offset, in ticks. 1 tick &#x3D; 10000 ms. | [optional] 
 **width** | **int**| Optional. The fixed horizontal resolution of the encoded video. | [optional] 
 **height** | **int**| Optional. The fixed vertical resolution of the encoded video. | [optional] 
 **max_width** | **int**| Optional. The maximum horizontal resolution of the encoded video. | [optional] 
 **max_height** | **int**| Optional. The maximum vertical resolution of the encoded video. | [optional] 
 **video_bit_rate** | **int**| Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. | [optional] 
 **subtitle_stream_index** | **int**| Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. | [optional] 
 **subtitle_method** | [**SubtitleDeliveryMethod**](.md)| Optional. Specify the subtitle delivery method. | [optional] 
 **max_ref_frames** | **int**| Optional. | [optional] 
 **max_video_bit_depth** | **int**| Optional. The maximum video bit depth. | [optional] 
 **require_avc** | **bool**| Optional. Whether to require avc. | [optional] 
 **de_interlace** | **bool**| Optional. Whether to deinterlace the video. | [optional] 
 **require_non_anamorphic** | **bool**| Optional. Whether to require a non anamorphic stream. | [optional] 
 **transcoding_max_audio_channels** | **int**| Optional. The maximum number of audio channels to transcode. | [optional] 
 **cpu_core_limit** | **int**| Optional. The limit of how many cpu cores to use. | [optional] 
 **live_stream_id** | **str**| The live stream id. | [optional] 
 **enable_mpegts_m2_ts_mode** | **bool**| Optional. Whether to enable the MpegtsM2Ts mode. | [optional] 
 **video_codec** | **str**| Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url&#39;s extension. | [optional] 
 **subtitle_codec** | **str**| Optional. Specify a subtitle codec to encode to. | [optional] 
 **transcode_reasons** | **str**| Optional. The transcoding reason. | [optional] 
 **audio_stream_index** | **int**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **video_stream_index** | **int**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 
 **context** | [**EncodingContext**](.md)| Optional. The MediaBrowser.Model.Dlna.EncodingContext. | [optional] 
 **stream_options** | [**Dict[str, Optional[str]]**](str.md)| Optional. The streaming options. | [optional] 
 **enable_audio_vbr_encoding** | **bool**| Optional. Whether to enable Audio Encoding. | [optional] [default to True]

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: video/*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Video stream returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_versions**
> merge_versions(ids)

Merges videos into a single record.

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
    api_instance = jellyfin.generated.api_10_10.VideosApi(api_client)
    ids = ['ids_example'] # List[str] | Item id list. This allows multiple, comma delimited.

    try:
        # Merges videos into a single record.
        api_instance.merge_versions(ids)
    except Exception as e:
        print("Exception when calling VideosApi->merge_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[str]**](str.md)| Item id list. This allows multiple, comma delimited. | 

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
**204** | Videos merged. |  -  |
**400** | Supply at least 2 video ids. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

