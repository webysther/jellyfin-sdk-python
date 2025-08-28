# MediaSourceInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | [**MediaProtocol**](MediaProtocol.md) |  | [optional] 
**id** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**encoder_path** | **str** |  | [optional] 
**encoder_protocol** | [**MediaProtocol**](MediaProtocol.md) |  | [optional] 
**type** | [**MediaSourceType**](MediaSourceType.md) |  | [optional] 
**container** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**is_remote** | **bool** | Gets or sets a value indicating whether the media is remote.  Differentiate internet url vs local network. | [optional] 
**e_tag** | **str** |  | [optional] 
**run_time_ticks** | **int** |  | [optional] 
**read_at_native_framerate** | **bool** |  | [optional] 
**ignore_dts** | **bool** |  | [optional] 
**ignore_index** | **bool** |  | [optional] 
**gen_pts_input** | **bool** |  | [optional] 
**supports_transcoding** | **bool** |  | [optional] 
**supports_direct_stream** | **bool** |  | [optional] 
**supports_direct_play** | **bool** |  | [optional] 
**is_infinite_stream** | **bool** |  | [optional] 
**use_most_compatible_transcoding_profile** | **bool** |  | [optional] [default to False]
**requires_opening** | **bool** |  | [optional] 
**open_token** | **str** |  | [optional] 
**requires_closing** | **bool** |  | [optional] 
**live_stream_id** | **str** |  | [optional] 
**buffer_ms** | **int** |  | [optional] 
**requires_looping** | **bool** |  | [optional] 
**supports_probing** | **bool** |  | [optional] 
**video_type** | [**VideoType**](VideoType.md) |  | [optional] 
**iso_type** | [**IsoType**](IsoType.md) |  | [optional] 
**video3_d_format** | [**Video3DFormat**](Video3DFormat.md) |  | [optional] 
**media_streams** | [**List[MediaStream]**](MediaStream.md) |  | [optional] 
**media_attachments** | [**List[MediaAttachment]**](MediaAttachment.md) |  | [optional] 
**formats** | **List[str]** |  | [optional] 
**bitrate** | **int** |  | [optional] 
**fallback_max_streaming_bitrate** | **int** |  | [optional] 
**timestamp** | [**TransportStreamTimestamp**](TransportStreamTimestamp.md) |  | [optional] 
**required_http_headers** | **Dict[str, Optional[str]]** |  | [optional] 
**transcoding_url** | **str** |  | [optional] 
**transcoding_sub_protocol** | [**MediaStreamProtocol**](MediaStreamProtocol.md) | Media streaming protocol.  Lowercase for backwards compatibility. | [optional] 
**transcoding_container** | **str** |  | [optional] 
**analyze_duration_ms** | **int** |  | [optional] 
**default_audio_stream_index** | **int** |  | [optional] 
**default_subtitle_stream_index** | **int** |  | [optional] 
**has_segments** | **bool** |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.media_source_info import MediaSourceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MediaSourceInfo from a JSON string
media_source_info_instance = MediaSourceInfo.from_json(json)
# print the JSON string representation of the object
print(MediaSourceInfo.to_json())

# convert the object into a dict
media_source_info_dict = media_source_info_instance.to_dict()
# create an instance of MediaSourceInfo from a dict
media_source_info_from_dict = MediaSourceInfo.from_dict(media_source_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


