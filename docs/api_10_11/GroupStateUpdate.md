# GroupStateUpdate

Class GroupStateUpdate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**GroupStateType**](GroupStateType.md) | Gets the state of the group. | [optional] 
**reason** | [**PlaybackRequestType**](PlaybackRequestType.md) | Gets the reason of the state change. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.group_state_update import GroupStateUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of GroupStateUpdate from a JSON string
group_state_update_instance = GroupStateUpdate.from_json(json)
# print the JSON string representation of the object
print(GroupStateUpdate.to_json())

# convert the object into a dict
group_state_update_dict = group_state_update_instance.to_dict()
# create an instance of GroupStateUpdate from a dict
group_state_update_from_dict = GroupStateUpdate.from_dict(group_state_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


