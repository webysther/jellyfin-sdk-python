# LibraryOptionsResultDto

Library options result dto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_savers** | [**List[LibraryOptionInfoDto]**](LibraryOptionInfoDto.md) | Gets or sets the metadata savers. | [optional] 
**metadata_readers** | [**List[LibraryOptionInfoDto]**](LibraryOptionInfoDto.md) | Gets or sets the metadata readers. | [optional] 
**subtitle_fetchers** | [**List[LibraryOptionInfoDto]**](LibraryOptionInfoDto.md) | Gets or sets the subtitle fetchers. | [optional] 
**lyric_fetchers** | [**List[LibraryOptionInfoDto]**](LibraryOptionInfoDto.md) | Gets or sets the list of lyric fetchers. | [optional] 
**type_options** | [**List[LibraryTypeOptionsDto]**](LibraryTypeOptionsDto.md) | Gets or sets the type options. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.library_options_result_dto import LibraryOptionsResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryOptionsResultDto from a JSON string
library_options_result_dto_instance = LibraryOptionsResultDto.from_json(json)
# print the JSON string representation of the object
print(LibraryOptionsResultDto.to_json())

# convert the object into a dict
library_options_result_dto_dict = library_options_result_dto_instance.to_dict()
# create an instance of LibraryOptionsResultDto from a dict
library_options_result_dto_from_dict = LibraryOptionsResultDto.from_dict(library_options_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


