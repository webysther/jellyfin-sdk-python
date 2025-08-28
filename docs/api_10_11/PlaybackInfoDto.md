# PlaybackInfoDto

Playback info dto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | Gets or sets the playback userId. | [optional] 
**max_streaming_bitrate** | **int** | Gets or sets the max streaming bitrate. | [optional] 
**start_time_ticks** | **int** | Gets or sets the start time in ticks. | [optional] 
**audio_stream_index** | **int** | Gets or sets the audio stream index. | [optional] 
**subtitle_stream_index** | **int** | Gets or sets the subtitle stream index. | [optional] 
**max_audio_channels** | **int** | Gets or sets the max audio channels. | [optional] 
**media_source_id** | **str** | Gets or sets the media source id. | [optional] 
**live_stream_id** | **str** | Gets or sets the live stream id. | [optional] 
**device_profile** | [**DeviceProfile**](DeviceProfile.md) | Gets or sets the device profile. | [optional] 
**enable_direct_play** | **bool** | Gets or sets a value indicating whether to enable direct play. | [optional] 
**enable_direct_stream** | **bool** | Gets or sets a value indicating whether to enable direct stream. | [optional] 
**enable_transcoding** | **bool** | Gets or sets a value indicating whether to enable transcoding. | [optional] 
**allow_video_stream_copy** | **bool** | Gets or sets a value indicating whether to enable video stream copy. | [optional] 
**allow_audio_stream_copy** | **bool** | Gets or sets a value indicating whether to allow audio stream copy. | [optional] 
**auto_open_live_stream** | **bool** | Gets or sets a value indicating whether to auto open the live stream. | [optional] 
**always_burn_in_subtitle_when_transcoding** | **bool** | Gets or sets a value indicating whether always burn in subtitles when transcoding. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.playback_info_dto import PlaybackInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlaybackInfoDto from a JSON string
playback_info_dto_instance = PlaybackInfoDto.from_json(json)
# print the JSON string representation of the object
print(PlaybackInfoDto.to_json())

# convert the object into a dict
playback_info_dto_dict = playback_info_dto_instance.to_dict()
# create an instance of PlaybackInfoDto from a dict
playback_info_dto_from_dict = PlaybackInfoDto.from_dict(playback_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


