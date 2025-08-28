# LibraryStorageDto

Contains informations about a libraries storage informations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Gets or sets the Library Id. | [optional] 
**name** | **str** | Gets or sets the name of the library. | [optional] 
**folders** | [**List[FolderStorageDto]**](FolderStorageDto.md) | Gets or sets the storage informations about the folders used in a library. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.library_storage_dto import LibraryStorageDto

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryStorageDto from a JSON string
library_storage_dto_instance = LibraryStorageDto.from_json(json)
# print the JSON string representation of the object
print(LibraryStorageDto.to_json())

# convert the object into a dict
library_storage_dto_dict = library_storage_dto_instance.to_dict()
# create an instance of LibraryStorageDto from a dict
library_storage_dto_from_dict = LibraryStorageDto.from_dict(library_storage_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


