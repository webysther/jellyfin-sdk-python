# OpenLiveStreamDto

Open live stream dto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**open_token** | **str** | Gets or sets the open token. | [optional] 
**user_id** | **str** | Gets or sets the user id. | [optional] 
**play_session_id** | **str** | Gets or sets the play session id. | [optional] 
**max_streaming_bitrate** | **int** | Gets or sets the max streaming bitrate. | [optional] 
**start_time_ticks** | **int** | Gets or sets the start time in ticks. | [optional] 
**audio_stream_index** | **int** | Gets or sets the audio stream index. | [optional] 
**subtitle_stream_index** | **int** | Gets or sets the subtitle stream index. | [optional] 
**max_audio_channels** | **int** | Gets or sets the max audio channels. | [optional] 
**item_id** | **str** | Gets or sets the item id. | [optional] 
**enable_direct_play** | **bool** | Gets or sets a value indicating whether to enable direct play. | [optional] 
**enable_direct_stream** | **bool** | Gets or sets a value indicating whether to enale direct stream. | [optional] 
**always_burn_in_subtitle_when_transcoding** | **bool** | Gets or sets a value indicating whether always burn in subtitles when transcoding. | [optional] 
**device_profile** | [**DeviceProfile**](DeviceProfile.md) |  | [optional] 
**direct_play_protocols** | [**List[MediaProtocol]**](MediaProtocol.md) | Gets or sets the device play protocols. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.open_live_stream_dto import OpenLiveStreamDto

# TODO update the JSON string below
json = "{}"
# create an instance of OpenLiveStreamDto from a JSON string
open_live_stream_dto_instance = OpenLiveStreamDto.from_json(json)
# print the JSON string representation of the object
print(OpenLiveStreamDto.to_json())

# convert the object into a dict
open_live_stream_dto_dict = open_live_stream_dto_instance.to_dict()
# create an instance of OpenLiveStreamDto from a dict
open_live_stream_dto_from_dict = OpenLiveStreamDto.from_dict(open_live_stream_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


