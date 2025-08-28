# CultureDto

Class CultureDto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets the name. | [optional] 
**display_name** | **str** | Gets the display name. | [optional] 
**two_letter_iso_language_name** | **str** | Gets the name of the two letter ISO language. | [optional] 
**three_letter_iso_language_name** | **str** | Gets the name of the three letter ISO language. | [optional] [readonly] 
**three_letter_iso_language_names** | **List[str]** |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.culture_dto import CultureDto

# TODO update the JSON string below
json = "{}"
# create an instance of CultureDto from a JSON string
culture_dto_instance = CultureDto.from_json(json)
# print the JSON string representation of the object
print(CultureDto.to_json())

# convert the object into a dict
culture_dto_dict = culture_dto_instance.to_dict()
# create an instance of CultureDto from a dict
culture_dto_from_dict = CultureDto.from_dict(culture_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


