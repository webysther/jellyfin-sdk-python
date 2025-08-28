# PlayQueueUpdate

Class PlayQueueUpdate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | [**PlayQueueUpdateReason**](PlayQueueUpdateReason.md) |  | [optional] 
**last_update** | **datetime** | Gets the UTC time of the last change to the playing queue. | [optional] 
**playlist** | [**List[SyncPlayQueueItem]**](SyncPlayQueueItem.md) | Gets the playlist. | [optional] 
**playing_item_index** | **int** | Gets the playing item index in the playlist. | [optional] 
**start_position_ticks** | **int** | Gets the start position ticks. | [optional] 
**is_playing** | **bool** | Gets a value indicating whether the current item is playing. | [optional] 
**shuffle_mode** | [**GroupShuffleMode**](GroupShuffleMode.md) |  | [optional] 
**repeat_mode** | [**GroupRepeatMode**](GroupRepeatMode.md) |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.play_queue_update import PlayQueueUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueueUpdate from a JSON string
play_queue_update_instance = PlayQueueUpdate.from_json(json)
# print the JSON string representation of the object
print(PlayQueueUpdate.to_json())

# convert the object into a dict
play_queue_update_dict = play_queue_update_instance.to_dict()
# create an instance of PlayQueueUpdate from a dict
play_queue_update_from_dict = PlayQueueUpdate.from_dict(play_queue_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


