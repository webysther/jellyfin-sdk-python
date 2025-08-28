# FolderStorageDto

Contains information about a specific folder.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Gets the path of the folder in question. | [optional] 
**free_space** | **int** | Gets the free space of the underlying storage device of the Jellyfin.Api.Models.SystemInfoDtos.FolderStorageDto.Path. | [optional] 
**used_space** | **int** | Gets the used space of the underlying storage device of the Jellyfin.Api.Models.SystemInfoDtos.FolderStorageDto.Path. | [optional] 
**storage_type** | **str** | Gets the kind of storage device of the Jellyfin.Api.Models.SystemInfoDtos.FolderStorageDto.Path. | [optional] 
**device_id** | **str** | Gets the Device Identifier. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.folder_storage_dto import FolderStorageDto

# TODO update the JSON string below
json = "{}"
# create an instance of FolderStorageDto from a JSON string
folder_storage_dto_instance = FolderStorageDto.from_json(json)
# print the JSON string representation of the object
print(FolderStorageDto.to_json())

# convert the object into a dict
folder_storage_dto_dict = folder_storage_dto_instance.to_dict()
# create an instance of FolderStorageDto from a dict
folder_storage_dto_from_dict = FolderStorageDto.from_dict(folder_storage_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


