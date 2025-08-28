# GroupInfoDto

Class GroupInfoDto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | Gets the group identifier. | [optional] 
**group_name** | **str** | Gets the group name. | [optional] 
**state** | [**GroupStateType**](GroupStateType.md) |  | [optional] 
**participants** | **List[str]** | Gets the participants. | [optional] 
**last_updated_at** | **datetime** | Gets the date when this DTO has been created. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.group_info_dto import GroupInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of GroupInfoDto from a JSON string
group_info_dto_instance = GroupInfoDto.from_json(json)
# print the JSON string representation of the object
print(GroupInfoDto.to_json())

# convert the object into a dict
group_info_dto_dict = group_info_dto_instance.to_dict()
# create an instance of GroupInfoDto from a dict
group_info_dto_from_dict = GroupInfoDto.from_dict(group_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


