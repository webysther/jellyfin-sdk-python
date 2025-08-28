# PlayQueueUpdateGroupUpdate

Class GroupUpdate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | Gets the group identifier. | [optional] [readonly] 
**type** | [**GroupUpdateType**](GroupUpdateType.md) |  | [optional] 
**data** | [**PlayQueueUpdate**](PlayQueueUpdate.md) |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.play_queue_update_group_update import PlayQueueUpdateGroupUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PlayQueueUpdateGroupUpdate from a JSON string
play_queue_update_group_update_instance = PlayQueueUpdateGroupUpdate.from_json(json)
# print the JSON string representation of the object
print(PlayQueueUpdateGroupUpdate.to_json())

# convert the object into a dict
play_queue_update_group_update_dict = play_queue_update_group_update_instance.to_dict()
# create an instance of PlayQueueUpdateGroupUpdate from a dict
play_queue_update_group_update_from_dict = PlayQueueUpdateGroupUpdate.from_dict(play_queue_update_group_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


