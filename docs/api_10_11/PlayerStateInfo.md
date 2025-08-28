# PlayerStateInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position_ticks** | **int** | Gets or sets the now playing position ticks. | [optional] 
**can_seek** | **bool** | Gets or sets a value indicating whether this instance can seek. | [optional] 
**is_paused** | **bool** | Gets or sets a value indicating whether this instance is paused. | [optional] 
**is_muted** | **bool** | Gets or sets a value indicating whether this instance is muted. | [optional] 
**volume_level** | **int** | Gets or sets the volume level. | [optional] 
**audio_stream_index** | **int** | Gets or sets the index of the now playing audio stream. | [optional] 
**subtitle_stream_index** | **int** | Gets or sets the index of the now playing subtitle stream. | [optional] 
**media_source_id** | **str** | Gets or sets the now playing media version identifier. | [optional] 
**play_method** | [**PlayMethod**](PlayMethod.md) | Gets or sets the play method. | [optional] 
**repeat_mode** | [**RepeatMode**](RepeatMode.md) | Gets or sets the repeat mode. | [optional] 
**playback_order** | [**PlaybackOrder**](PlaybackOrder.md) | Gets or sets the playback order. | [optional] 
**live_stream_id** | **str** | Gets or sets the now playing live stream identifier. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.player_state_info import PlayerStateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerStateInfo from a JSON string
player_state_info_instance = PlayerStateInfo.from_json(json)
# print the JSON string representation of the object
print(PlayerStateInfo.to_json())

# convert the object into a dict
player_state_info_dict = player_state_info_instance.to_dict()
# create an instance of PlayerStateInfo from a dict
player_state_info_from_dict = PlayerStateInfo.from_dict(player_state_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


