# SyncPlayQueueItem

Class QueueItem.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | Gets the item identifier. | [optional] 
**playlist_item_id** | **str** | Gets the playlist identifier of the item. | [optional] [readonly] 

## Example

```python
from jellyfin.generated.api_10_11.models.sync_play_queue_item import SyncPlayQueueItem

# TODO update the JSON string below
json = "{}"
# create an instance of SyncPlayQueueItem from a JSON string
sync_play_queue_item_instance = SyncPlayQueueItem.from_json(json)
# print the JSON string representation of the object
print(SyncPlayQueueItem.to_json())

# convert the object into a dict
sync_play_queue_item_dict = sync_play_queue_item_instance.to_dict()
# create an instance of SyncPlayQueueItem from a dict
sync_play_queue_item_from_dict = SyncPlayQueueItem.from_dict(sync_play_queue_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


