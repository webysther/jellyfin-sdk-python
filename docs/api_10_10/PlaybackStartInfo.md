# PlaybackStartInfo

Class PlaybackStartInfo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_seek** | **bool** | Gets or sets a value indicating whether this instance can seek. | [optional] 
**item** | [**BaseItemDto**](BaseItemDto.md) |  | [optional] 
**item_id** | **str** | Gets or sets the item identifier. | [optional] 
**session_id** | **str** | Gets or sets the session id. | [optional] 
**media_source_id** | **str** | Gets or sets the media version identifier. | [optional] 
**audio_stream_index** | **int** | Gets or sets the index of the audio stream. | [optional] 
**subtitle_stream_index** | **int** | Gets or sets the index of the subtitle stream. | [optional] 
**is_paused** | **bool** | Gets or sets a value indicating whether this instance is paused. | [optional] 
**is_muted** | **bool** | Gets or sets a value indicating whether this instance is muted. | [optional] 
**position_ticks** | **int** | Gets or sets the position ticks. | [optional] 
**playback_start_time_ticks** | **int** |  | [optional] 
**volume_level** | **int** | Gets or sets the volume level. | [optional] 
**brightness** | **int** |  | [optional] 
**aspect_ratio** | **str** |  | [optional] 
**play_method** | [**PlayMethod**](PlayMethod.md) |  | [optional] 
**live_stream_id** | **str** | Gets or sets the live stream identifier. | [optional] 
**play_session_id** | **str** | Gets or sets the play session identifier. | [optional] 
**repeat_mode** | [**RepeatMode**](RepeatMode.md) |  | [optional] 
**playback_order** | [**PlaybackOrder**](PlaybackOrder.md) |  | [optional] 
**now_playing_queue** | [**List[QueueItem]**](QueueItem.md) |  | [optional] 
**playlist_item_id** | **str** |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.playback_start_info import PlaybackStartInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PlaybackStartInfo from a JSON string
playback_start_info_instance = PlaybackStartInfo.from_json(json)
# print the JSON string representation of the object
print(PlaybackStartInfo.to_json())

# convert the object into a dict
playback_start_info_dict = playback_start_info_instance.to_dict()
# create an instance of PlaybackStartInfo from a dict
playback_start_info_from_dict = PlaybackStartInfo.from_dict(playback_start_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


