# LibraryTypeOptionsDto

Library type options dto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Gets or sets the type. | [optional] 
**metadata_fetchers** | [**List[LibraryOptionInfoDto]**](LibraryOptionInfoDto.md) | Gets or sets the metadata fetchers. | [optional] 
**image_fetchers** | [**List[LibraryOptionInfoDto]**](LibraryOptionInfoDto.md) | Gets or sets the image fetchers. | [optional] 
**supported_image_types** | [**List[ImageType]**](ImageType.md) | Gets or sets the supported image types. | [optional] 
**default_image_options** | [**List[ImageOption]**](ImageOption.md) | Gets or sets the default image options. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.library_type_options_dto import LibraryTypeOptionsDto

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryTypeOptionsDto from a JSON string
library_type_options_dto_instance = LibraryTypeOptionsDto.from_json(json)
# print the JSON string representation of the object
print(LibraryTypeOptionsDto.to_json())

# convert the object into a dict
library_type_options_dto_dict = library_type_options_dto_instance.to_dict()
# create an instance of LibraryTypeOptionsDto from a dict
library_type_options_dto_from_dict = LibraryTypeOptionsDto.from_dict(library_type_options_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


