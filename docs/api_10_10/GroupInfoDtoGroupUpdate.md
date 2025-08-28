# GroupInfoDtoGroupUpdate

Class GroupUpdate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | Gets the group identifier. | [optional] [readonly] 
**type** | [**GroupUpdateType**](GroupUpdateType.md) |  | [optional] 
**data** | [**GroupInfoDto**](GroupInfoDto.md) |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.group_info_dto_group_update import GroupInfoDtoGroupUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of GroupInfoDtoGroupUpdate from a JSON string
group_info_dto_group_update_instance = GroupInfoDtoGroupUpdate.from_json(json)
# print the JSON string representation of the object
print(GroupInfoDtoGroupUpdate.to_json())

# convert the object into a dict
group_info_dto_group_update_dict = group_info_dto_group_update_instance.to_dict()
# create an instance of GroupInfoDtoGroupUpdate from a dict
group_info_dto_group_update_from_dict = GroupInfoDtoGroupUpdate.from_dict(group_info_dto_group_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


