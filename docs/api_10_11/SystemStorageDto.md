# SystemStorageDto

Contains informations about the systems storage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**program_data_folder** | [**FolderStorageDto**](FolderStorageDto.md) | Gets or sets the Storage information of the program data folder. | [optional] 
**web_folder** | [**FolderStorageDto**](FolderStorageDto.md) | Gets or sets the Storage information of the web UI resources folder. | [optional] 
**image_cache_folder** | [**FolderStorageDto**](FolderStorageDto.md) | Gets or sets the Storage information of the folder where images are cached. | [optional] 
**cache_folder** | [**FolderStorageDto**](FolderStorageDto.md) | Gets or sets the Storage information of the cache folder. | [optional] 
**log_folder** | [**FolderStorageDto**](FolderStorageDto.md) | Gets or sets the Storage information of the folder where logfiles are saved to. | [optional] 
**internal_metadata_folder** | [**FolderStorageDto**](FolderStorageDto.md) | Gets or sets the Storage information of the folder where metadata is stored. | [optional] 
**transcoding_temp_folder** | [**FolderStorageDto**](FolderStorageDto.md) | Gets or sets the Storage information of the transcoding cache. | [optional] 
**libraries** | [**List[LibraryStorageDto]**](LibraryStorageDto.md) | Gets or sets the storage informations of all libraries. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.system_storage_dto import SystemStorageDto

# TODO update the JSON string below
json = "{}"
# create an instance of SystemStorageDto from a JSON string
system_storage_dto_instance = SystemStorageDto.from_json(json)
# print the JSON string representation of the object
print(SystemStorageDto.to_json())

# convert the object into a dict
system_storage_dto_dict = system_storage_dto_instance.to_dict()
# create an instance of SystemStorageDto from a dict
system_storage_dto_from_dict = SystemStorageDto.from_dict(system_storage_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


