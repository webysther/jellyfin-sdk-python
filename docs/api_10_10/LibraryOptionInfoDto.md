# LibraryOptionInfoDto

Library option info dto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets name. | [optional] 
**default_enabled** | **bool** | Gets or sets a value indicating whether default enabled. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.library_option_info_dto import LibraryOptionInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryOptionInfoDto from a JSON string
library_option_info_dto_instance = LibraryOptionInfoDto.from_json(json)
# print the JSON string representation of the object
print(LibraryOptionInfoDto.to_json())

# convert the object into a dict
library_option_info_dto_dict = library_option_info_dto_instance.to_dict()
# create an instance of LibraryOptionInfoDto from a dict
library_option_info_dto_from_dict = LibraryOptionInfoDto.from_dict(library_option_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


