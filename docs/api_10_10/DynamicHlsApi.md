# jellyfin.generated.api_10_10.DynamicHlsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_hls_audio_segment**](DynamicHlsApi.md#get_hls_audio_segment) | **GET** /Audio/{itemId}/hls1/{playlistId}/{segmentId}.{container} | Gets a video stream using HTTP live streaming.
[**get_hls_video_segment**](DynamicHlsApi.md#get_hls_video_segment) | **GET** /Videos/{itemId}/hls1/{playlistId}/{segmentId}.{container} | Gets a video stream using HTTP live streaming.
[**get_live_hls_stream**](DynamicHlsApi.md#get_live_hls_stream) | **GET** /Videos/{itemId}/live.m3u8 | Gets a hls live stream.
[**get_master_hls_audio_playlist**](DynamicHlsApi.md#get_master_hls_audio_playlist) | **GET** /Audio/{itemId}/master.m3u8 | Gets an audio hls playlist stream.
[**get_master_hls_video_playlist**](DynamicHlsApi.md#get_master_hls_video_playlist) | **GET** /Videos/{itemId}/master.m3u8 | Gets a video hls playlist stream.
[**get_variant_hls_audio_playlist**](DynamicHlsApi.md#get_variant_hls_audio_playlist) | **GET** /Audio/{itemId}/main.m3u8 | Gets an audio stream using HTTP live streaming.
[**get_variant_hls_video_playlist**](DynamicHlsApi.md#get_variant_hls_video_playlist) | **GET** /Videos/{itemId}/main.m3u8 | Gets a video stream using HTTP live streaming.
[**head_master_hls_audio_playlist**](DynamicHlsApi.md#head_master_hls_audio_playlist) | **HEAD** /Audio/{itemId}/master.m3u8 | Gets an audio hls playlist stream.
[**head_master_hls_video_playlist**](DynamicHlsApi.md#head_master_hls_video_playlist) | **HEAD** /Videos/{itemId}/master.m3u8 | Gets a video hls playlist stream.


# **get_hls_audio_segment**
> bytearray get_hls_audio_segment(item_id, playlist_id, segment_id, container, runtime_ticks, actual_segment_length_ticks, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, media_source_id=media_source_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, max_streaming_bitrate=max_streaming_bitrate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, enable_audio_vbr_encoding=enable_audio_vbr_encoding)

Gets a video stream using HTTP live streaming.

### Example

* Api Key Authentication (CustomAuthentication):

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
    api_instance = jellyfin.generated.api_10_10.DynamicHlsApi(api_client)
    item_id = 'item_id_example' # str | The item id.
    playlist_id = 'playlist_id_example' # str | The playlist id.
    segment_id = 56 # int | The segment id.
    container = 'container_example' # str | The video container. Possible values are: ts, webm, asf, wmv, ogv, mp4, m4v, mkv, mpeg, mpg, avi, 3gp, wmv, wtv, m2ts, mov, iso, flv.
    runtime_ticks = 56 # int | The position of the requested segment in ticks.
    actual_segment_length_ticks = 56 # int | The length of the requested segment in ticks.
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
    audio_codec = 'audio_codec_example' # str | Optional. Specify an audio codec to encode to, e.g. mp3. (optional)
    enable_auto_stream_copy = True # bool | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. (optional)
    allow_video_stream_copy = True # bool | Whether or not to allow copying of the video stream url. (optional)
    allow_audio_stream_copy = True # bool | Whether or not to allow copying of the audio stream url. (optional)
    break_on_non_key_frames = True # bool | Optional. Whether to break on non key frames. (optional)
    audio_sample_rate = 56 # int | Optional. Specify a specific audio sample rate, e.g. 44100. (optional)
    max_audio_bit_depth = 56 # int | Optional. The maximum audio bit depth. (optional)
    max_streaming_bitrate = 56 # int | Optional. The maximum streaming bitrate. (optional)
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
    video_codec = 'video_codec_example' # str | Optional. Specify a video codec to encode to, e.g. h264. (optional)
    subtitle_codec = 'subtitle_codec_example' # str | Optional. Specify a subtitle codec to encode to. (optional)
    transcode_reasons = 'transcode_reasons_example' # str | Optional. The transcoding reason. (optional)
    audio_stream_index = 56 # int | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. (optional)
    video_stream_index = 56 # int | Optional. The index of the video stream to use. If omitted the first video stream will be used. (optional)
    context = jellyfin.generated.api_10_10.EncodingContext() # EncodingContext | Optional. The MediaBrowser.Model.Dlna.EncodingContext. (optional)
    stream_options = {'key': 'stream_options_example'} # Dict[str, Optional[str]] | Optional. The streaming options. (optional)
    enable_audio_vbr_encoding = True # bool | Optional. Whether to enable Audio Encoding. (optional) (default to True)

    try:
        # Gets a video stream using HTTP live streaming.
        api_response = api_instance.get_hls_audio_segment(item_id, playlist_id, segment_id, container, runtime_ticks, actual_segment_length_ticks, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, media_source_id=media_source_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, max_streaming_bitrate=max_streaming_bitrate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, enable_audio_vbr_encoding=enable_audio_vbr_encoding)
        print("The response of DynamicHlsApi->get_hls_audio_segment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicHlsApi->get_hls_audio_segment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **playlist_id** | **str**| The playlist id. | 
 **segment_id** | **int**| The segment id. | 
 **container** | **str**| The video container. Possible values are: ts, webm, asf, wmv, ogv, mp4, m4v, mkv, mpeg, mpg, avi, 3gp, wmv, wtv, m2ts, mov, iso, flv. | 
 **runtime_ticks** | **int**| The position of the requested segment in ticks. | 
 **actual_segment_length_ticks** | **int**| The length of the requested segment in ticks. | 
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
 **audio_codec** | **str**| Optional. Specify an audio codec to encode to, e.g. mp3. | [optional] 
 **enable_auto_stream_copy** | **bool**| Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. | [optional] 
 **allow_video_stream_copy** | **bool**| Whether or not to allow copying of the video stream url. | [optional] 
 **allow_audio_stream_copy** | **bool**| Whether or not to allow copying of the audio stream url. | [optional] 
 **break_on_non_key_frames** | **bool**| Optional. Whether to break on non key frames. | [optional] 
 **audio_sample_rate** | **int**| Optional. Specify a specific audio sample rate, e.g. 44100. | [optional] 
 **max_audio_bit_depth** | **int**| Optional. The maximum audio bit depth. | [optional] 
 **max_streaming_bitrate** | **int**| Optional. The maximum streaming bitrate. | [optional] 
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
 **video_codec** | **str**| Optional. Specify a video codec to encode to, e.g. h264. | [optional] 
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

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: audio/*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Video stream returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hls_video_segment**
> bytearray get_hls_video_segment(item_id, playlist_id, segment_id, container, runtime_ticks, actual_segment_length_ticks, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, media_source_id=media_source_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, enable_audio_vbr_encoding=enable_audio_vbr_encoding, always_burn_in_subtitle_when_transcoding=always_burn_in_subtitle_when_transcoding)

Gets a video stream using HTTP live streaming.

### Example

* Api Key Authentication (CustomAuthentication):

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
    api_instance = jellyfin.generated.api_10_10.DynamicHlsApi(api_client)
    item_id = 'item_id_example' # str | The item id.
    playlist_id = 'playlist_id_example' # str | The playlist id.
    segment_id = 56 # int | The segment id.
    container = 'container_example' # str | The video container. Possible values are: ts, webm, asf, wmv, ogv, mp4, m4v, mkv, mpeg, mpg, avi, 3gp, wmv, wtv, m2ts, mov, iso, flv.
    runtime_ticks = 56 # int | The position of the requested segment in ticks.
    actual_segment_length_ticks = 56 # int | The length of the requested segment in ticks.
    static = True # bool | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false. (optional)
    params = 'params_example' # str | The streaming parameters. (optional)
    tag = 'tag_example' # str | The tag. (optional)
    device_profile_id = 'device_profile_id_example' # str | Optional. The dlna device profile id to utilize. (optional)
    play_session_id = 'play_session_id_example' # str | The play session id. (optional)
    segment_container = 'segment_container_example' # str | The segment container. (optional)
    segment_length = 56 # int | The desired segment length. (optional)
    min_segments = 56 # int | The minimum number of segments. (optional)
    media_source_id = 'media_source_id_example' # str | The media version id, if playing an alternate version. (optional)
    device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
    audio_codec = 'audio_codec_example' # str | Optional. Specify an audio codec to encode to, e.g. mp3. (optional)
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
    video_codec = 'video_codec_example' # str | Optional. Specify a video codec to encode to, e.g. h264. (optional)
    subtitle_codec = 'subtitle_codec_example' # str | Optional. Specify a subtitle codec to encode to. (optional)
    transcode_reasons = 'transcode_reasons_example' # str | Optional. The transcoding reason. (optional)
    audio_stream_index = 56 # int | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. (optional)
    video_stream_index = 56 # int | Optional. The index of the video stream to use. If omitted the first video stream will be used. (optional)
    context = jellyfin.generated.api_10_10.EncodingContext() # EncodingContext | Optional. The MediaBrowser.Model.Dlna.EncodingContext. (optional)
    stream_options = {'key': 'stream_options_example'} # Dict[str, Optional[str]] | Optional. The streaming options. (optional)
    enable_audio_vbr_encoding = True # bool | Optional. Whether to enable Audio Encoding. (optional) (default to True)
    always_burn_in_subtitle_when_transcoding = False # bool | Whether to always burn in subtitles when transcoding. (optional) (default to False)

    try:
        # Gets a video stream using HTTP live streaming.
        api_response = api_instance.get_hls_video_segment(item_id, playlist_id, segment_id, container, runtime_ticks, actual_segment_length_ticks, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, media_source_id=media_source_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, enable_audio_vbr_encoding=enable_audio_vbr_encoding, always_burn_in_subtitle_when_transcoding=always_burn_in_subtitle_when_transcoding)
        print("The response of DynamicHlsApi->get_hls_video_segment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicHlsApi->get_hls_video_segment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **playlist_id** | **str**| The playlist id. | 
 **segment_id** | **int**| The segment id. | 
 **container** | **str**| The video container. Possible values are: ts, webm, asf, wmv, ogv, mp4, m4v, mkv, mpeg, mpg, avi, 3gp, wmv, wtv, m2ts, mov, iso, flv. | 
 **runtime_ticks** | **int**| The position of the requested segment in ticks. | 
 **actual_segment_length_ticks** | **int**| The length of the requested segment in ticks. | 
 **static** | **bool**| Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false. | [optional] 
 **params** | **str**| The streaming parameters. | [optional] 
 **tag** | **str**| The tag. | [optional] 
 **device_profile_id** | **str**| Optional. The dlna device profile id to utilize. | [optional] 
 **play_session_id** | **str**| The play session id. | [optional] 
 **segment_container** | **str**| The segment container. | [optional] 
 **segment_length** | **int**| The desired segment length. | [optional] 
 **min_segments** | **int**| The minimum number of segments. | [optional] 
 **media_source_id** | **str**| The media version id, if playing an alternate version. | [optional] 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **audio_codec** | **str**| Optional. Specify an audio codec to encode to, e.g. mp3. | [optional] 
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
 **video_codec** | **str**| Optional. Specify a video codec to encode to, e.g. h264. | [optional] 
 **subtitle_codec** | **str**| Optional. Specify a subtitle codec to encode to. | [optional] 
 **transcode_reasons** | **str**| Optional. The transcoding reason. | [optional] 
 **audio_stream_index** | **int**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **video_stream_index** | **int**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 
 **context** | [**EncodingContext**](.md)| Optional. The MediaBrowser.Model.Dlna.EncodingContext. | [optional] 
 **stream_options** | [**Dict[str, Optional[str]]**](str.md)| Optional. The streaming options. | [optional] 
 **enable_audio_vbr_encoding** | **bool**| Optional. Whether to enable Audio Encoding. | [optional] [default to True]
 **always_burn_in_subtitle_when_transcoding** | **bool**| Whether to always burn in subtitles when transcoding. | [optional] [default to False]

### Return type

**bytearray**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: video/*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Video stream returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_live_hls_stream**
> bytearray get_live_hls_stream(item_id, container=container, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, media_source_id=media_source_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, max_width=max_width, max_height=max_height, enable_subtitles_in_manifest=enable_subtitles_in_manifest, enable_audio_vbr_encoding=enable_audio_vbr_encoding, always_burn_in_subtitle_when_transcoding=always_burn_in_subtitle_when_transcoding)

Gets a hls live stream.

### Example

* Api Key Authentication (CustomAuthentication):

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
    api_instance = jellyfin.generated.api_10_10.DynamicHlsApi(api_client)
    item_id = 'item_id_example' # str | The item id.
    container = 'container_example' # str | The audio container. (optional)
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
    audio_codec = 'audio_codec_example' # str | Optional. Specify an audio codec to encode to, e.g. mp3. (optional)
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
    video_codec = 'video_codec_example' # str | Optional. Specify a video codec to encode to, e.g. h264. (optional)
    subtitle_codec = 'subtitle_codec_example' # str | Optional. Specify a subtitle codec to encode to. (optional)
    transcode_reasons = 'transcode_reasons_example' # str | Optional. The transcoding reason. (optional)
    audio_stream_index = 56 # int | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. (optional)
    video_stream_index = 56 # int | Optional. The index of the video stream to use. If omitted the first video stream will be used. (optional)
    context = jellyfin.generated.api_10_10.EncodingContext() # EncodingContext | Optional. The MediaBrowser.Model.Dlna.EncodingContext. (optional)
    stream_options = {'key': 'stream_options_example'} # Dict[str, Optional[str]] | Optional. The streaming options. (optional)
    max_width = 56 # int | Optional. The max width. (optional)
    max_height = 56 # int | Optional. The max height. (optional)
    enable_subtitles_in_manifest = True # bool | Optional. Whether to enable subtitles in the manifest. (optional)
    enable_audio_vbr_encoding = True # bool | Optional. Whether to enable Audio Encoding. (optional) (default to True)
    always_burn_in_subtitle_when_transcoding = False # bool | Whether to always burn in subtitles when transcoding. (optional) (default to False)

    try:
        # Gets a hls live stream.
        api_response = api_instance.get_live_hls_stream(item_id, container=container, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, media_source_id=media_source_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, max_width=max_width, max_height=max_height, enable_subtitles_in_manifest=enable_subtitles_in_manifest, enable_audio_vbr_encoding=enable_audio_vbr_encoding, always_burn_in_subtitle_when_transcoding=always_burn_in_subtitle_when_transcoding)
        print("The response of DynamicHlsApi->get_live_hls_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicHlsApi->get_live_hls_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **container** | **str**| The audio container. | [optional] 
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
 **audio_codec** | **str**| Optional. Specify an audio codec to encode to, e.g. mp3. | [optional] 
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
 **video_codec** | **str**| Optional. Specify a video codec to encode to, e.g. h264. | [optional] 
 **subtitle_codec** | **str**| Optional. Specify a subtitle codec to encode to. | [optional] 
 **transcode_reasons** | **str**| Optional. The transcoding reason. | [optional] 
 **audio_stream_index** | **int**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **video_stream_index** | **int**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 
 **context** | [**EncodingContext**](.md)| Optional. The MediaBrowser.Model.Dlna.EncodingContext. | [optional] 
 **stream_options** | [**Dict[str, Optional[str]]**](str.md)| Optional. The streaming options. | [optional] 
 **max_width** | **int**| Optional. The max width. | [optional] 
 **max_height** | **int**| Optional. The max height. | [optional] 
 **enable_subtitles_in_manifest** | **bool**| Optional. Whether to enable subtitles in the manifest. | [optional] 
 **enable_audio_vbr_encoding** | **bool**| Optional. Whether to enable Audio Encoding. | [optional] [default to True]
 **always_burn_in_subtitle_when_transcoding** | **bool**| Whether to always burn in subtitles when transcoding. | [optional] [default to False]

### Return type

**bytearray**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-mpegURL

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hls live stream retrieved. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_master_hls_audio_playlist**
> bytearray get_master_hls_audio_playlist(item_id, media_source_id, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, max_streaming_bitrate=max_streaming_bitrate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, enable_adaptive_bitrate_streaming=enable_adaptive_bitrate_streaming, enable_audio_vbr_encoding=enable_audio_vbr_encoding)

Gets an audio hls playlist stream.

### Example

* Api Key Authentication (CustomAuthentication):

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
    api_instance = jellyfin.generated.api_10_10.DynamicHlsApi(api_client)
    item_id = 'item_id_example' # str | The item id.
    media_source_id = 'media_source_id_example' # str | The media version id, if playing an alternate version.
    static = True # bool | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false. (optional)
    params = 'params_example' # str | The streaming parameters. (optional)
    tag = 'tag_example' # str | The tag. (optional)
    device_profile_id = 'device_profile_id_example' # str | Optional. The dlna device profile id to utilize. (optional)
    play_session_id = 'play_session_id_example' # str | The play session id. (optional)
    segment_container = 'segment_container_example' # str | The segment container. (optional)
    segment_length = 56 # int | The segment length. (optional)
    min_segments = 56 # int | The minimum number of segments. (optional)
    device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
    audio_codec = 'audio_codec_example' # str | Optional. Specify an audio codec to encode to, e.g. mp3. (optional)
    enable_auto_stream_copy = True # bool | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. (optional)
    allow_video_stream_copy = True # bool | Whether or not to allow copying of the video stream url. (optional)
    allow_audio_stream_copy = True # bool | Whether or not to allow copying of the audio stream url. (optional)
    break_on_non_key_frames = True # bool | Optional. Whether to break on non key frames. (optional)
    audio_sample_rate = 56 # int | Optional. Specify a specific audio sample rate, e.g. 44100. (optional)
    max_audio_bit_depth = 56 # int | Optional. The maximum audio bit depth. (optional)
    max_streaming_bitrate = 56 # int | Optional. The maximum streaming bitrate. (optional)
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
    video_codec = 'video_codec_example' # str | Optional. Specify a video codec to encode to, e.g. h264. (optional)
    subtitle_codec = 'subtitle_codec_example' # str | Optional. Specify a subtitle codec to encode to. (optional)
    transcode_reasons = 'transcode_reasons_example' # str | Optional. The transcoding reason. (optional)
    audio_stream_index = 56 # int | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. (optional)
    video_stream_index = 56 # int | Optional. The index of the video stream to use. If omitted the first video stream will be used. (optional)
    context = jellyfin.generated.api_10_10.EncodingContext() # EncodingContext | Optional. The MediaBrowser.Model.Dlna.EncodingContext. (optional)
    stream_options = {'key': 'stream_options_example'} # Dict[str, Optional[str]] | Optional. The streaming options. (optional)
    enable_adaptive_bitrate_streaming = True # bool | Enable adaptive bitrate streaming. (optional) (default to True)
    enable_audio_vbr_encoding = True # bool | Optional. Whether to enable Audio Encoding. (optional) (default to True)

    try:
        # Gets an audio hls playlist stream.
        api_response = api_instance.get_master_hls_audio_playlist(item_id, media_source_id, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, max_streaming_bitrate=max_streaming_bitrate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, enable_adaptive_bitrate_streaming=enable_adaptive_bitrate_streaming, enable_audio_vbr_encoding=enable_audio_vbr_encoding)
        print("The response of DynamicHlsApi->get_master_hls_audio_playlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicHlsApi->get_master_hls_audio_playlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **media_source_id** | **str**| The media version id, if playing an alternate version. | 
 **static** | **bool**| Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false. | [optional] 
 **params** | **str**| The streaming parameters. | [optional] 
 **tag** | **str**| The tag. | [optional] 
 **device_profile_id** | **str**| Optional. The dlna device profile id to utilize. | [optional] 
 **play_session_id** | **str**| The play session id. | [optional] 
 **segment_container** | **str**| The segment container. | [optional] 
 **segment_length** | **int**| The segment length. | [optional] 
 **min_segments** | **int**| The minimum number of segments. | [optional] 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **audio_codec** | **str**| Optional. Specify an audio codec to encode to, e.g. mp3. | [optional] 
 **enable_auto_stream_copy** | **bool**| Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. | [optional] 
 **allow_video_stream_copy** | **bool**| Whether or not to allow copying of the video stream url. | [optional] 
 **allow_audio_stream_copy** | **bool**| Whether or not to allow copying of the audio stream url. | [optional] 
 **break_on_non_key_frames** | **bool**| Optional. Whether to break on non key frames. | [optional] 
 **audio_sample_rate** | **int**| Optional. Specify a specific audio sample rate, e.g. 44100. | [optional] 
 **max_audio_bit_depth** | **int**| Optional. The maximum audio bit depth. | [optional] 
 **max_streaming_bitrate** | **int**| Optional. The maximum streaming bitrate. | [optional] 
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
 **video_codec** | **str**| Optional. Specify a video codec to encode to, e.g. h264. | [optional] 
 **subtitle_codec** | **str**| Optional. Specify a subtitle codec to encode to. | [optional] 
 **transcode_reasons** | **str**| Optional. The transcoding reason. | [optional] 
 **audio_stream_index** | **int**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **video_stream_index** | **int**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 
 **context** | [**EncodingContext**](.md)| Optional. The MediaBrowser.Model.Dlna.EncodingContext. | [optional] 
 **stream_options** | [**Dict[str, Optional[str]]**](str.md)| Optional. The streaming options. | [optional] 
 **enable_adaptive_bitrate_streaming** | **bool**| Enable adaptive bitrate streaming. | [optional] [default to True]
 **enable_audio_vbr_encoding** | **bool**| Optional. Whether to enable Audio Encoding. | [optional] [default to True]

### Return type

**bytearray**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-mpegURL

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Audio stream returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_master_hls_video_playlist**
> bytearray get_master_hls_video_playlist(item_id, media_source_id, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, enable_adaptive_bitrate_streaming=enable_adaptive_bitrate_streaming, enable_trickplay=enable_trickplay, enable_audio_vbr_encoding=enable_audio_vbr_encoding, always_burn_in_subtitle_when_transcoding=always_burn_in_subtitle_when_transcoding)

Gets a video hls playlist stream.

### Example

* Api Key Authentication (CustomAuthentication):

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
    api_instance = jellyfin.generated.api_10_10.DynamicHlsApi(api_client)
    item_id = 'item_id_example' # str | The item id.
    media_source_id = 'media_source_id_example' # str | The media version id, if playing an alternate version.
    static = True # bool | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false. (optional)
    params = 'params_example' # str | The streaming parameters. (optional)
    tag = 'tag_example' # str | The tag. (optional)
    device_profile_id = 'device_profile_id_example' # str | Optional. The dlna device profile id to utilize. (optional)
    play_session_id = 'play_session_id_example' # str | The play session id. (optional)
    segment_container = 'segment_container_example' # str | The segment container. (optional)
    segment_length = 56 # int | The segment length. (optional)
    min_segments = 56 # int | The minimum number of segments. (optional)
    device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
    audio_codec = 'audio_codec_example' # str | Optional. Specify an audio codec to encode to, e.g. mp3. (optional)
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
    video_codec = 'video_codec_example' # str | Optional. Specify a video codec to encode to, e.g. h264. (optional)
    subtitle_codec = 'subtitle_codec_example' # str | Optional. Specify a subtitle codec to encode to. (optional)
    transcode_reasons = 'transcode_reasons_example' # str | Optional. The transcoding reason. (optional)
    audio_stream_index = 56 # int | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. (optional)
    video_stream_index = 56 # int | Optional. The index of the video stream to use. If omitted the first video stream will be used. (optional)
    context = jellyfin.generated.api_10_10.EncodingContext() # EncodingContext | Optional. The MediaBrowser.Model.Dlna.EncodingContext. (optional)
    stream_options = {'key': 'stream_options_example'} # Dict[str, Optional[str]] | Optional. The streaming options. (optional)
    enable_adaptive_bitrate_streaming = True # bool | Enable adaptive bitrate streaming. (optional) (default to True)
    enable_trickplay = True # bool | Enable trickplay image playlists being added to master playlist. (optional) (default to True)
    enable_audio_vbr_encoding = True # bool | Whether to enable Audio Encoding. (optional) (default to True)
    always_burn_in_subtitle_when_transcoding = False # bool | Whether to always burn in subtitles when transcoding. (optional) (default to False)

    try:
        # Gets a video hls playlist stream.
        api_response = api_instance.get_master_hls_video_playlist(item_id, media_source_id, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, enable_adaptive_bitrate_streaming=enable_adaptive_bitrate_streaming, enable_trickplay=enable_trickplay, enable_audio_vbr_encoding=enable_audio_vbr_encoding, always_burn_in_subtitle_when_transcoding=always_burn_in_subtitle_when_transcoding)
        print("The response of DynamicHlsApi->get_master_hls_video_playlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicHlsApi->get_master_hls_video_playlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **media_source_id** | **str**| The media version id, if playing an alternate version. | 
 **static** | **bool**| Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false. | [optional] 
 **params** | **str**| The streaming parameters. | [optional] 
 **tag** | **str**| The tag. | [optional] 
 **device_profile_id** | **str**| Optional. The dlna device profile id to utilize. | [optional] 
 **play_session_id** | **str**| The play session id. | [optional] 
 **segment_container** | **str**| The segment container. | [optional] 
 **segment_length** | **int**| The segment length. | [optional] 
 **min_segments** | **int**| The minimum number of segments. | [optional] 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **audio_codec** | **str**| Optional. Specify an audio codec to encode to, e.g. mp3. | [optional] 
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
 **video_codec** | **str**| Optional. Specify a video codec to encode to, e.g. h264. | [optional] 
 **subtitle_codec** | **str**| Optional. Specify a subtitle codec to encode to. | [optional] 
 **transcode_reasons** | **str**| Optional. The transcoding reason. | [optional] 
 **audio_stream_index** | **int**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **video_stream_index** | **int**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 
 **context** | [**EncodingContext**](.md)| Optional. The MediaBrowser.Model.Dlna.EncodingContext. | [optional] 
 **stream_options** | [**Dict[str, Optional[str]]**](str.md)| Optional. The streaming options. | [optional] 
 **enable_adaptive_bitrate_streaming** | **bool**| Enable adaptive bitrate streaming. | [optional] [default to True]
 **enable_trickplay** | **bool**| Enable trickplay image playlists being added to master playlist. | [optional] [default to True]
 **enable_audio_vbr_encoding** | **bool**| Whether to enable Audio Encoding. | [optional] [default to True]
 **always_burn_in_subtitle_when_transcoding** | **bool**| Whether to always burn in subtitles when transcoding. | [optional] [default to False]

### Return type

**bytearray**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-mpegURL

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Video stream returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variant_hls_audio_playlist**
> bytearray get_variant_hls_audio_playlist(item_id, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, media_source_id=media_source_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, max_streaming_bitrate=max_streaming_bitrate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, enable_audio_vbr_encoding=enable_audio_vbr_encoding)

Gets an audio stream using HTTP live streaming.

### Example

* Api Key Authentication (CustomAuthentication):

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
    api_instance = jellyfin.generated.api_10_10.DynamicHlsApi(api_client)
    item_id = 'item_id_example' # str | The item id.
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
    audio_codec = 'audio_codec_example' # str | Optional. Specify an audio codec to encode to, e.g. mp3. (optional)
    enable_auto_stream_copy = True # bool | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. (optional)
    allow_video_stream_copy = True # bool | Whether or not to allow copying of the video stream url. (optional)
    allow_audio_stream_copy = True # bool | Whether or not to allow copying of the audio stream url. (optional)
    break_on_non_key_frames = True # bool | Optional. Whether to break on non key frames. (optional)
    audio_sample_rate = 56 # int | Optional. Specify a specific audio sample rate, e.g. 44100. (optional)
    max_audio_bit_depth = 56 # int | Optional. The maximum audio bit depth. (optional)
    max_streaming_bitrate = 56 # int | Optional. The maximum streaming bitrate. (optional)
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
    video_codec = 'video_codec_example' # str | Optional. Specify a video codec to encode to, e.g. h264. (optional)
    subtitle_codec = 'subtitle_codec_example' # str | Optional. Specify a subtitle codec to encode to. (optional)
    transcode_reasons = 'transcode_reasons_example' # str | Optional. The transcoding reason. (optional)
    audio_stream_index = 56 # int | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. (optional)
    video_stream_index = 56 # int | Optional. The index of the video stream to use. If omitted the first video stream will be used. (optional)
    context = jellyfin.generated.api_10_10.EncodingContext() # EncodingContext | Optional. The MediaBrowser.Model.Dlna.EncodingContext. (optional)
    stream_options = {'key': 'stream_options_example'} # Dict[str, Optional[str]] | Optional. The streaming options. (optional)
    enable_audio_vbr_encoding = True # bool | Optional. Whether to enable Audio Encoding. (optional) (default to True)

    try:
        # Gets an audio stream using HTTP live streaming.
        api_response = api_instance.get_variant_hls_audio_playlist(item_id, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, media_source_id=media_source_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, max_streaming_bitrate=max_streaming_bitrate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, enable_audio_vbr_encoding=enable_audio_vbr_encoding)
        print("The response of DynamicHlsApi->get_variant_hls_audio_playlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicHlsApi->get_variant_hls_audio_playlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
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
 **audio_codec** | **str**| Optional. Specify an audio codec to encode to, e.g. mp3. | [optional] 
 **enable_auto_stream_copy** | **bool**| Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. | [optional] 
 **allow_video_stream_copy** | **bool**| Whether or not to allow copying of the video stream url. | [optional] 
 **allow_audio_stream_copy** | **bool**| Whether or not to allow copying of the audio stream url. | [optional] 
 **break_on_non_key_frames** | **bool**| Optional. Whether to break on non key frames. | [optional] 
 **audio_sample_rate** | **int**| Optional. Specify a specific audio sample rate, e.g. 44100. | [optional] 
 **max_audio_bit_depth** | **int**| Optional. The maximum audio bit depth. | [optional] 
 **max_streaming_bitrate** | **int**| Optional. The maximum streaming bitrate. | [optional] 
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
 **video_codec** | **str**| Optional. Specify a video codec to encode to, e.g. h264. | [optional] 
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

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-mpegURL

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Audio stream returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variant_hls_video_playlist**
> bytearray get_variant_hls_video_playlist(item_id, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, media_source_id=media_source_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, enable_audio_vbr_encoding=enable_audio_vbr_encoding, always_burn_in_subtitle_when_transcoding=always_burn_in_subtitle_when_transcoding)

Gets a video stream using HTTP live streaming.

### Example

* Api Key Authentication (CustomAuthentication):

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
    api_instance = jellyfin.generated.api_10_10.DynamicHlsApi(api_client)
    item_id = 'item_id_example' # str | The item id.
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
    audio_codec = 'audio_codec_example' # str | Optional. Specify an audio codec to encode to, e.g. mp3. (optional)
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
    video_codec = 'video_codec_example' # str | Optional. Specify a video codec to encode to, e.g. h264. (optional)
    subtitle_codec = 'subtitle_codec_example' # str | Optional. Specify a subtitle codec to encode to. (optional)
    transcode_reasons = 'transcode_reasons_example' # str | Optional. The transcoding reason. (optional)
    audio_stream_index = 56 # int | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. (optional)
    video_stream_index = 56 # int | Optional. The index of the video stream to use. If omitted the first video stream will be used. (optional)
    context = jellyfin.generated.api_10_10.EncodingContext() # EncodingContext | Optional. The MediaBrowser.Model.Dlna.EncodingContext. (optional)
    stream_options = {'key': 'stream_options_example'} # Dict[str, Optional[str]] | Optional. The streaming options. (optional)
    enable_audio_vbr_encoding = True # bool | Optional. Whether to enable Audio Encoding. (optional) (default to True)
    always_burn_in_subtitle_when_transcoding = False # bool | Whether to always burn in subtitles when transcoding. (optional) (default to False)

    try:
        # Gets a video stream using HTTP live streaming.
        api_response = api_instance.get_variant_hls_video_playlist(item_id, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, media_source_id=media_source_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, enable_audio_vbr_encoding=enable_audio_vbr_encoding, always_burn_in_subtitle_when_transcoding=always_burn_in_subtitle_when_transcoding)
        print("The response of DynamicHlsApi->get_variant_hls_video_playlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicHlsApi->get_variant_hls_video_playlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
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
 **audio_codec** | **str**| Optional. Specify an audio codec to encode to, e.g. mp3. | [optional] 
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
 **video_codec** | **str**| Optional. Specify a video codec to encode to, e.g. h264. | [optional] 
 **subtitle_codec** | **str**| Optional. Specify a subtitle codec to encode to. | [optional] 
 **transcode_reasons** | **str**| Optional. The transcoding reason. | [optional] 
 **audio_stream_index** | **int**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **video_stream_index** | **int**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 
 **context** | [**EncodingContext**](.md)| Optional. The MediaBrowser.Model.Dlna.EncodingContext. | [optional] 
 **stream_options** | [**Dict[str, Optional[str]]**](str.md)| Optional. The streaming options. | [optional] 
 **enable_audio_vbr_encoding** | **bool**| Optional. Whether to enable Audio Encoding. | [optional] [default to True]
 **always_burn_in_subtitle_when_transcoding** | **bool**| Whether to always burn in subtitles when transcoding. | [optional] [default to False]

### Return type

**bytearray**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-mpegURL

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Video stream returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_master_hls_audio_playlist**
> bytearray head_master_hls_audio_playlist(item_id, media_source_id, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, max_streaming_bitrate=max_streaming_bitrate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, enable_adaptive_bitrate_streaming=enable_adaptive_bitrate_streaming, enable_audio_vbr_encoding=enable_audio_vbr_encoding)

Gets an audio hls playlist stream.

### Example

* Api Key Authentication (CustomAuthentication):

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
    api_instance = jellyfin.generated.api_10_10.DynamicHlsApi(api_client)
    item_id = 'item_id_example' # str | The item id.
    media_source_id = 'media_source_id_example' # str | The media version id, if playing an alternate version.
    static = True # bool | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false. (optional)
    params = 'params_example' # str | The streaming parameters. (optional)
    tag = 'tag_example' # str | The tag. (optional)
    device_profile_id = 'device_profile_id_example' # str | Optional. The dlna device profile id to utilize. (optional)
    play_session_id = 'play_session_id_example' # str | The play session id. (optional)
    segment_container = 'segment_container_example' # str | The segment container. (optional)
    segment_length = 56 # int | The segment length. (optional)
    min_segments = 56 # int | The minimum number of segments. (optional)
    device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
    audio_codec = 'audio_codec_example' # str | Optional. Specify an audio codec to encode to, e.g. mp3. (optional)
    enable_auto_stream_copy = True # bool | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. (optional)
    allow_video_stream_copy = True # bool | Whether or not to allow copying of the video stream url. (optional)
    allow_audio_stream_copy = True # bool | Whether or not to allow copying of the audio stream url. (optional)
    break_on_non_key_frames = True # bool | Optional. Whether to break on non key frames. (optional)
    audio_sample_rate = 56 # int | Optional. Specify a specific audio sample rate, e.g. 44100. (optional)
    max_audio_bit_depth = 56 # int | Optional. The maximum audio bit depth. (optional)
    max_streaming_bitrate = 56 # int | Optional. The maximum streaming bitrate. (optional)
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
    video_codec = 'video_codec_example' # str | Optional. Specify a video codec to encode to, e.g. h264. (optional)
    subtitle_codec = 'subtitle_codec_example' # str | Optional. Specify a subtitle codec to encode to. (optional)
    transcode_reasons = 'transcode_reasons_example' # str | Optional. The transcoding reason. (optional)
    audio_stream_index = 56 # int | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. (optional)
    video_stream_index = 56 # int | Optional. The index of the video stream to use. If omitted the first video stream will be used. (optional)
    context = jellyfin.generated.api_10_10.EncodingContext() # EncodingContext | Optional. The MediaBrowser.Model.Dlna.EncodingContext. (optional)
    stream_options = {'key': 'stream_options_example'} # Dict[str, Optional[str]] | Optional. The streaming options. (optional)
    enable_adaptive_bitrate_streaming = True # bool | Enable adaptive bitrate streaming. (optional) (default to True)
    enable_audio_vbr_encoding = True # bool | Optional. Whether to enable Audio Encoding. (optional) (default to True)

    try:
        # Gets an audio hls playlist stream.
        api_response = api_instance.head_master_hls_audio_playlist(item_id, media_source_id, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, max_streaming_bitrate=max_streaming_bitrate, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, enable_adaptive_bitrate_streaming=enable_adaptive_bitrate_streaming, enable_audio_vbr_encoding=enable_audio_vbr_encoding)
        print("The response of DynamicHlsApi->head_master_hls_audio_playlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicHlsApi->head_master_hls_audio_playlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **media_source_id** | **str**| The media version id, if playing an alternate version. | 
 **static** | **bool**| Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false. | [optional] 
 **params** | **str**| The streaming parameters. | [optional] 
 **tag** | **str**| The tag. | [optional] 
 **device_profile_id** | **str**| Optional. The dlna device profile id to utilize. | [optional] 
 **play_session_id** | **str**| The play session id. | [optional] 
 **segment_container** | **str**| The segment container. | [optional] 
 **segment_length** | **int**| The segment length. | [optional] 
 **min_segments** | **int**| The minimum number of segments. | [optional] 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **audio_codec** | **str**| Optional. Specify an audio codec to encode to, e.g. mp3. | [optional] 
 **enable_auto_stream_copy** | **bool**| Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. | [optional] 
 **allow_video_stream_copy** | **bool**| Whether or not to allow copying of the video stream url. | [optional] 
 **allow_audio_stream_copy** | **bool**| Whether or not to allow copying of the audio stream url. | [optional] 
 **break_on_non_key_frames** | **bool**| Optional. Whether to break on non key frames. | [optional] 
 **audio_sample_rate** | **int**| Optional. Specify a specific audio sample rate, e.g. 44100. | [optional] 
 **max_audio_bit_depth** | **int**| Optional. The maximum audio bit depth. | [optional] 
 **max_streaming_bitrate** | **int**| Optional. The maximum streaming bitrate. | [optional] 
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
 **video_codec** | **str**| Optional. Specify a video codec to encode to, e.g. h264. | [optional] 
 **subtitle_codec** | **str**| Optional. Specify a subtitle codec to encode to. | [optional] 
 **transcode_reasons** | **str**| Optional. The transcoding reason. | [optional] 
 **audio_stream_index** | **int**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **video_stream_index** | **int**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 
 **context** | [**EncodingContext**](.md)| Optional. The MediaBrowser.Model.Dlna.EncodingContext. | [optional] 
 **stream_options** | [**Dict[str, Optional[str]]**](str.md)| Optional. The streaming options. | [optional] 
 **enable_adaptive_bitrate_streaming** | **bool**| Enable adaptive bitrate streaming. | [optional] [default to True]
 **enable_audio_vbr_encoding** | **bool**| Optional. Whether to enable Audio Encoding. | [optional] [default to True]

### Return type

**bytearray**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-mpegURL

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Audio stream returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_master_hls_video_playlist**
> bytearray head_master_hls_video_playlist(item_id, media_source_id, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, enable_adaptive_bitrate_streaming=enable_adaptive_bitrate_streaming, enable_trickplay=enable_trickplay, enable_audio_vbr_encoding=enable_audio_vbr_encoding, always_burn_in_subtitle_when_transcoding=always_burn_in_subtitle_when_transcoding)

Gets a video hls playlist stream.

### Example

* Api Key Authentication (CustomAuthentication):

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
    api_instance = jellyfin.generated.api_10_10.DynamicHlsApi(api_client)
    item_id = 'item_id_example' # str | The item id.
    media_source_id = 'media_source_id_example' # str | The media version id, if playing an alternate version.
    static = True # bool | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false. (optional)
    params = 'params_example' # str | The streaming parameters. (optional)
    tag = 'tag_example' # str | The tag. (optional)
    device_profile_id = 'device_profile_id_example' # str | Optional. The dlna device profile id to utilize. (optional)
    play_session_id = 'play_session_id_example' # str | The play session id. (optional)
    segment_container = 'segment_container_example' # str | The segment container. (optional)
    segment_length = 56 # int | The segment length. (optional)
    min_segments = 56 # int | The minimum number of segments. (optional)
    device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed. (optional)
    audio_codec = 'audio_codec_example' # str | Optional. Specify an audio codec to encode to, e.g. mp3. (optional)
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
    video_codec = 'video_codec_example' # str | Optional. Specify a video codec to encode to, e.g. h264. (optional)
    subtitle_codec = 'subtitle_codec_example' # str | Optional. Specify a subtitle codec to encode to. (optional)
    transcode_reasons = 'transcode_reasons_example' # str | Optional. The transcoding reason. (optional)
    audio_stream_index = 56 # int | Optional. The index of the audio stream to use. If omitted the first audio stream will be used. (optional)
    video_stream_index = 56 # int | Optional. The index of the video stream to use. If omitted the first video stream will be used. (optional)
    context = jellyfin.generated.api_10_10.EncodingContext() # EncodingContext | Optional. The MediaBrowser.Model.Dlna.EncodingContext. (optional)
    stream_options = {'key': 'stream_options_example'} # Dict[str, Optional[str]] | Optional. The streaming options. (optional)
    enable_adaptive_bitrate_streaming = True # bool | Enable adaptive bitrate streaming. (optional) (default to True)
    enable_trickplay = True # bool | Enable trickplay image playlists being added to master playlist. (optional) (default to True)
    enable_audio_vbr_encoding = True # bool | Whether to enable Audio Encoding. (optional) (default to True)
    always_burn_in_subtitle_when_transcoding = False # bool | Whether to always burn in subtitles when transcoding. (optional) (default to False)

    try:
        # Gets a video hls playlist stream.
        api_response = api_instance.head_master_hls_video_playlist(item_id, media_source_id, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, max_width=max_width, max_height=max_height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, enable_adaptive_bitrate_streaming=enable_adaptive_bitrate_streaming, enable_trickplay=enable_trickplay, enable_audio_vbr_encoding=enable_audio_vbr_encoding, always_burn_in_subtitle_when_transcoding=always_burn_in_subtitle_when_transcoding)
        print("The response of DynamicHlsApi->head_master_hls_video_playlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicHlsApi->head_master_hls_video_playlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **media_source_id** | **str**| The media version id, if playing an alternate version. | 
 **static** | **bool**| Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false. | [optional] 
 **params** | **str**| The streaming parameters. | [optional] 
 **tag** | **str**| The tag. | [optional] 
 **device_profile_id** | **str**| Optional. The dlna device profile id to utilize. | [optional] 
 **play_session_id** | **str**| The play session id. | [optional] 
 **segment_container** | **str**| The segment container. | [optional] 
 **segment_length** | **int**| The segment length. | [optional] 
 **min_segments** | **int**| The minimum number of segments. | [optional] 
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **audio_codec** | **str**| Optional. Specify an audio codec to encode to, e.g. mp3. | [optional] 
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
 **video_codec** | **str**| Optional. Specify a video codec to encode to, e.g. h264. | [optional] 
 **subtitle_codec** | **str**| Optional. Specify a subtitle codec to encode to. | [optional] 
 **transcode_reasons** | **str**| Optional. The transcoding reason. | [optional] 
 **audio_stream_index** | **int**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **video_stream_index** | **int**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 
 **context** | [**EncodingContext**](.md)| Optional. The MediaBrowser.Model.Dlna.EncodingContext. | [optional] 
 **stream_options** | [**Dict[str, Optional[str]]**](str.md)| Optional. The streaming options. | [optional] 
 **enable_adaptive_bitrate_streaming** | **bool**| Enable adaptive bitrate streaming. | [optional] [default to True]
 **enable_trickplay** | **bool**| Enable trickplay image playlists being added to master playlist. | [optional] [default to True]
 **enable_audio_vbr_encoding** | **bool**| Whether to enable Audio Encoding. | [optional] [default to True]
 **always_burn_in_subtitle_when_transcoding** | **bool**| Whether to always burn in subtitles when transcoding. | [optional] [default to False]

### Return type

**bytearray**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-mpegURL

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Video stream returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

