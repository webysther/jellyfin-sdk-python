# JoinGroupRequestDto

Class JoinGroupRequestDto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | Gets or sets the group identifier. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.join_group_request_dto import JoinGroupRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of JoinGroupRequestDto from a JSON string
join_group_request_dto_instance = JoinGroupRequestDto.from_json(json)
# print the JSON string representation of the object
print(JoinGroupRequestDto.to_json())

# convert the object into a dict
join_group_request_dto_dict = join_group_request_dto_instance.to_dict()
# create an instance of JoinGroupRequestDto from a dict
join_group_request_dto_from_dict = JoinGroupRequestDto.from_dict(join_group_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


