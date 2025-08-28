# SyncPlayGroupJoinedUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | Gets the group identifier. | [optional] [readonly] 
**data** | [**GroupInfoDto**](GroupInfoDto.md) | Gets the update data. | [optional] [readonly] 
**type** | [**GroupUpdateType**](GroupUpdateType.md) | Enum GroupUpdateType. | [optional] [readonly] [default to GroupUpdateType.GROUPJOINED]

## Example

```python
from jellyfin.generated.api_10_11.models.sync_play_group_joined_update import SyncPlayGroupJoinedUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SyncPlayGroupJoinedUpdate from a JSON string
sync_play_group_joined_update_instance = SyncPlayGroupJoinedUpdate.from_json(json)
# print the JSON string representation of the object
print(SyncPlayGroupJoinedUpdate.to_json())

# convert the object into a dict
sync_play_group_joined_update_dict = sync_play_group_joined_update_instance.to_dict()
# create an instance of SyncPlayGroupJoinedUpdate from a dict
sync_play_group_joined_update_from_dict = SyncPlayGroupJoinedUpdate.from_dict(sync_play_group_joined_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


