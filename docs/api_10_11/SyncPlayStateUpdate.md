# SyncPlayStateUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | Gets the group identifier. | [optional] [readonly] 
**data** | [**GroupStateUpdate**](GroupStateUpdate.md) | Gets the update data. | [optional] [readonly] 
**type** | [**GroupUpdateType**](GroupUpdateType.md) | Enum GroupUpdateType. | [optional] [readonly] [default to GroupUpdateType.STATEUPDATE]

## Example

```python
from jellyfin.generated.api_10_11.models.sync_play_state_update import SyncPlayStateUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SyncPlayStateUpdate from a JSON string
sync_play_state_update_instance = SyncPlayStateUpdate.from_json(json)
# print the JSON string representation of the object
print(SyncPlayStateUpdate.to_json())

# convert the object into a dict
sync_play_state_update_dict = sync_play_state_update_instance.to_dict()
# create an instance of SyncPlayStateUpdate from a dict
sync_play_state_update_from_dict = SyncPlayStateUpdate.from_dict(sync_play_state_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


