# FileSystemEntryInfo

Class FileSystemEntryInfo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets the name. | [optional] 
**path** | **str** | Gets the path. | [optional] 
**type** | [**FileSystemEntryType**](FileSystemEntryType.md) | Gets the type. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.file_system_entry_info import FileSystemEntryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FileSystemEntryInfo from a JSON string
file_system_entry_info_instance = FileSystemEntryInfo.from_json(json)
# print the JSON string representation of the object
print(FileSystemEntryInfo.to_json())

# convert the object into a dict
file_system_entry_info_dict = file_system_entry_info_instance.to_dict()
# create an instance of FileSystemEntryInfo from a dict
file_system_entry_info_from_dict = FileSystemEntryInfo.from_dict(file_system_entry_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


