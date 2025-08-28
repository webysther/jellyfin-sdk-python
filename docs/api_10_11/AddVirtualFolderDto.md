# AddVirtualFolderDto

Add virtual folder dto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**library_options** | [**LibraryOptions**](LibraryOptions.md) | Gets or sets library options. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.add_virtual_folder_dto import AddVirtualFolderDto

# TODO update the JSON string below
json = "{}"
# create an instance of AddVirtualFolderDto from a JSON string
add_virtual_folder_dto_instance = AddVirtualFolderDto.from_json(json)
# print the JSON string representation of the object
print(AddVirtualFolderDto.to_json())

# convert the object into a dict
add_virtual_folder_dto_dict = add_virtual_folder_dto_instance.to_dict()
# create an instance of AddVirtualFolderDto from a dict
add_virtual_folder_dto_from_dict = AddVirtualFolderDto.from_dict(add_virtual_folder_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


