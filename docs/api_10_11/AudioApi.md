# jellyfin.generated.api_10_11.AudioApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audio_stream**](AudioApi.md#get_audio_stream) | **GET** /Audio/{itemId}/stream | Gets an audio stream.
[**get_audio_stream_by_container**](AudioApi.md#get_audio_stream_by_container) | **GET** /Audio/{itemId}/stream.{container} | Gets an audio stream.
[**head_audio_stream**](AudioApi.md#head_audio_stream) | **HEAD** /Audio/{itemId}/stream | Gets an audio stream.
[**head_audio_stream_by_container**](AudioApi.md#head_audio_stream_by_container) | **HEAD** /Audio/{itemId}/stream.{container} | Gets an audio stream.


# **get_audio_stream**
> bytearray get_audio_stream(item_id, container=container, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, media_source_id=media_source_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, enable_audio_vbr_encoding=enable_audio_vbr_encoding)

Gets an audio stream.

### Example


```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jellyfin.generated.api_10_11.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with jellyfin.generated.api_10_11.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jellyfin.generated.api_10_11.AudioApi(api_client)
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
    video_bit_rate = 56 # int | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. (optional)
    subtitle_stream_index = 56 # int | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. (optional)
    subtitle_method = jellyfin.generated.api_10_11.SubtitleDeliveryMethod() # SubtitleDeliveryMethod | Optional. Specify the subtitle delivery method. (optional)
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
    context = jellyfin.generated.api_10_11.EncodingContext() # EncodingContext | Optional. The MediaBrowser.Model.Dlna.EncodingContext. (optional)
    stream_options = {'key': 'stream_options_example'} # Dict[str, Optional[str]] | Optional. The streaming options. (optional)
    enable_audio_vbr_encoding = True # bool | Optional. Whether to enable Audio Encoding. (optional) (default to True)

    try:
        # Gets an audio stream.
        api_response = api_instance.get_audio_stream(item_id, container=container, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, media_source_id=media_source_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, enable_audio_vbr_encoding=enable_audio_vbr_encoding)
        print("The response of AudioApi->get_audio_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudioApi->get_audio_stream: %s\n" % e)
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
 **video_bit_rate** | **int**| Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. | [optional] 
 **subtitle_stream_index** | **int**| Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. | [optional] 
 **subtitle_method** | **SubtitleDeliveryMethod**| Optional. Specify the subtitle delivery method. | [optional] 
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
 **context** | **EncodingContext**| Optional. The MediaBrowser.Model.Dlna.EncodingContext. | [optional] 
 **stream_options** | [**Dict[str, Optional[str]]**](str.md)| Optional. The streaming options. | [optional] 
 **enable_audio_vbr_encoding** | **bool**| Optional. Whether to enable Audio Encoding. | [optional] [default to True]

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: audio/*, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Audio stream returned. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audio_stream_by_container**
> bytearray get_audio_stream_by_container(item_id, container, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, media_source_id=media_source_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, enable_audio_vbr_encoding=enable_audio_vbr_encoding)

Gets an audio stream.

### Example


```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jellyfin.generated.api_10_11.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with jellyfin.generated.api_10_11.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jellyfin.generated.api_10_11.AudioApi(api_client)
    item_id = 'item_id_example' # str | The item id.
    container = 'container_example' # str | The audio container.
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
    video_bit_rate = 56 # int | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. (optional)
    subtitle_stream_index = 56 # int | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. (optional)
    subtitle_method = jellyfin.generated.api_10_11.SubtitleDeliveryMethod() # SubtitleDeliveryMethod | Optional. Specify the subtitle delivery method. (optional)
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
    context = jellyfin.generated.api_10_11.EncodingContext() # EncodingContext | Optional. The MediaBrowser.Model.Dlna.EncodingContext. (optional)
    stream_options = {'key': 'stream_options_example'} # Dict[str, Optional[str]] | Optional. The streaming options. (optional)
    enable_audio_vbr_encoding = True # bool | Optional. Whether to enable Audio Encoding. (optional) (default to True)

    try:
        # Gets an audio stream.
        api_response = api_instance.get_audio_stream_by_container(item_id, container, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, media_source_id=media_source_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, enable_audio_vbr_encoding=enable_audio_vbr_encoding)
        print("The response of AudioApi->get_audio_stream_by_container:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudioApi->get_audio_stream_by_container: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **container** | **str**| The audio container. | 
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
 **video_bit_rate** | **int**| Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. | [optional] 
 **subtitle_stream_index** | **int**| Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. | [optional] 
 **subtitle_method** | **SubtitleDeliveryMethod**| Optional. Specify the subtitle delivery method. | [optional] 
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
 **context** | **EncodingContext**| Optional. The MediaBrowser.Model.Dlna.EncodingContext. | [optional] 
 **stream_options** | [**Dict[str, Optional[str]]**](str.md)| Optional. The streaming options. | [optional] 
 **enable_audio_vbr_encoding** | **bool**| Optional. Whether to enable Audio Encoding. | [optional] [default to True]

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: audio/*, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Audio stream returned. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_audio_stream**
> bytearray head_audio_stream(item_id, container=container, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, media_source_id=media_source_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, enable_audio_vbr_encoding=enable_audio_vbr_encoding)

Gets an audio stream.

### Example


```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jellyfin.generated.api_10_11.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with jellyfin.generated.api_10_11.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jellyfin.generated.api_10_11.AudioApi(api_client)
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
    video_bit_rate = 56 # int | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. (optional)
    subtitle_stream_index = 56 # int | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. (optional)
    subtitle_method = jellyfin.generated.api_10_11.SubtitleDeliveryMethod() # SubtitleDeliveryMethod | Optional. Specify the subtitle delivery method. (optional)
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
    context = jellyfin.generated.api_10_11.EncodingContext() # EncodingContext | Optional. The MediaBrowser.Model.Dlna.EncodingContext. (optional)
    stream_options = {'key': 'stream_options_example'} # Dict[str, Optional[str]] | Optional. The streaming options. (optional)
    enable_audio_vbr_encoding = True # bool | Optional. Whether to enable Audio Encoding. (optional) (default to True)

    try:
        # Gets an audio stream.
        api_response = api_instance.head_audio_stream(item_id, container=container, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, media_source_id=media_source_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, enable_audio_vbr_encoding=enable_audio_vbr_encoding)
        print("The response of AudioApi->head_audio_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudioApi->head_audio_stream: %s\n" % e)
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
 **video_bit_rate** | **int**| Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. | [optional] 
 **subtitle_stream_index** | **int**| Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. | [optional] 
 **subtitle_method** | **SubtitleDeliveryMethod**| Optional. Specify the subtitle delivery method. | [optional] 
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
 **context** | **EncodingContext**| Optional. The MediaBrowser.Model.Dlna.EncodingContext. | [optional] 
 **stream_options** | [**Dict[str, Optional[str]]**](str.md)| Optional. The streaming options. | [optional] 
 **enable_audio_vbr_encoding** | **bool**| Optional. Whether to enable Audio Encoding. | [optional] [default to True]

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: audio/*, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Audio stream returned. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_audio_stream_by_container**
> bytearray head_audio_stream_by_container(item_id, container, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, media_source_id=media_source_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, enable_audio_vbr_encoding=enable_audio_vbr_encoding)

Gets an audio stream.

### Example


```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jellyfin.generated.api_10_11.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with jellyfin.generated.api_10_11.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jellyfin.generated.api_10_11.AudioApi(api_client)
    item_id = 'item_id_example' # str | The item id.
    container = 'container_example' # str | The audio container.
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
    video_bit_rate = 56 # int | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. (optional)
    subtitle_stream_index = 56 # int | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. (optional)
    subtitle_method = jellyfin.generated.api_10_11.SubtitleDeliveryMethod() # SubtitleDeliveryMethod | Optional. Specify the subtitle delivery method. (optional)
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
    context = jellyfin.generated.api_10_11.EncodingContext() # EncodingContext | Optional. The MediaBrowser.Model.Dlna.EncodingContext. (optional)
    stream_options = {'key': 'stream_options_example'} # Dict[str, Optional[str]] | Optional. The streaming options. (optional)
    enable_audio_vbr_encoding = True # bool | Optional. Whether to enable Audio Encoding. (optional) (default to True)

    try:
        # Gets an audio stream.
        api_response = api_instance.head_audio_stream_by_container(item_id, container, static=static, params=params, tag=tag, device_profile_id=device_profile_id, play_session_id=play_session_id, segment_container=segment_container, segment_length=segment_length, min_segments=min_segments, media_source_id=media_source_id, device_id=device_id, audio_codec=audio_codec, enable_auto_stream_copy=enable_auto_stream_copy, allow_video_stream_copy=allow_video_stream_copy, allow_audio_stream_copy=allow_audio_stream_copy, break_on_non_key_frames=break_on_non_key_frames, audio_sample_rate=audio_sample_rate, max_audio_bit_depth=max_audio_bit_depth, audio_bit_rate=audio_bit_rate, audio_channels=audio_channels, max_audio_channels=max_audio_channels, profile=profile, level=level, framerate=framerate, max_framerate=max_framerate, copy_timestamps=copy_timestamps, start_time_ticks=start_time_ticks, width=width, height=height, video_bit_rate=video_bit_rate, subtitle_stream_index=subtitle_stream_index, subtitle_method=subtitle_method, max_ref_frames=max_ref_frames, max_video_bit_depth=max_video_bit_depth, require_avc=require_avc, de_interlace=de_interlace, require_non_anamorphic=require_non_anamorphic, transcoding_max_audio_channels=transcoding_max_audio_channels, cpu_core_limit=cpu_core_limit, live_stream_id=live_stream_id, enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode, video_codec=video_codec, subtitle_codec=subtitle_codec, transcode_reasons=transcode_reasons, audio_stream_index=audio_stream_index, video_stream_index=video_stream_index, context=context, stream_options=stream_options, enable_audio_vbr_encoding=enable_audio_vbr_encoding)
        print("The response of AudioApi->head_audio_stream_by_container:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudioApi->head_audio_stream_by_container: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **container** | **str**| The audio container. | 
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
 **video_bit_rate** | **int**| Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. | [optional] 
 **subtitle_stream_index** | **int**| Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. | [optional] 
 **subtitle_method** | **SubtitleDeliveryMethod**| Optional. Specify the subtitle delivery method. | [optional] 
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
 **context** | **EncodingContext**| Optional. The MediaBrowser.Model.Dlna.EncodingContext. | [optional] 
 **stream_options** | [**Dict[str, Optional[str]]**](str.md)| Optional. The streaming options. | [optional] 
 **enable_audio_vbr_encoding** | **bool**| Optional. Whether to enable Audio Encoding. | [optional] [default to True]

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: audio/*, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Audio stream returned. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

