# GroupStateUpdateGroupUpdate

Class GroupUpdate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | Gets the group identifier. | [optional] [readonly] 
**type** | [**GroupUpdateType**](GroupUpdateType.md) |  | [optional] 
**data** | [**GroupStateUpdate**](GroupStateUpdate.md) |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.group_state_update_group_update import GroupStateUpdateGroupUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of GroupStateUpdateGroupUpdate from a JSON string
group_state_update_group_update_instance = GroupStateUpdateGroupUpdate.from_json(json)
# print the JSON string representation of the object
print(GroupStateUpdateGroupUpdate.to_json())

# convert the object into a dict
group_state_update_group_update_dict = group_state_update_group_update_instance.to_dict()
# create an instance of GroupStateUpdateGroupUpdate from a dict
group_state_update_group_update_from_dict = GroupStateUpdateGroupUpdate.from_dict(group_state_update_group_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


