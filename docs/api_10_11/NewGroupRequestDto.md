# NewGroupRequestDto

Class NewGroupRequestDto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_name** | **str** | Gets or sets the group name. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.new_group_request_dto import NewGroupRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of NewGroupRequestDto from a JSON string
new_group_request_dto_instance = NewGroupRequestDto.from_json(json)
# print the JSON string representation of the object
print(NewGroupRequestDto.to_json())

# convert the object into a dict
new_group_request_dto_dict = new_group_request_dto_instance.to_dict()
# create an instance of NewGroupRequestDto from a dict
new_group_request_dto_from_dict = NewGroupRequestDto.from_dict(new_group_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


