# SpecialViewOptionDto

Special view option dto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets view option name. | [optional] 
**id** | **str** | Gets or sets view option id. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.special_view_option_dto import SpecialViewOptionDto

# TODO update the JSON string below
json = "{}"
# create an instance of SpecialViewOptionDto from a JSON string
special_view_option_dto_instance = SpecialViewOptionDto.from_json(json)
# print the JSON string representation of the object
print(SpecialViewOptionDto.to_json())

# convert the object into a dict
special_view_option_dto_dict = special_view_option_dto_instance.to_dict()
# create an instance of SpecialViewOptionDto from a dict
special_view_option_dto_from_dict = SpecialViewOptionDto.from_dict(special_view_option_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


