# LibraryUpdateInfo

Class LibraryUpdateInfo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folders_added_to** | **List[str]** | Gets or sets the folders added to. | [optional] 
**folders_removed_from** | **List[str]** | Gets or sets the folders removed from. | [optional] 
**items_added** | **List[str]** | Gets or sets the items added. | [optional] 
**items_removed** | **List[str]** | Gets or sets the items removed. | [optional] 
**items_updated** | **List[str]** | Gets or sets the items updated. | [optional] 
**collection_folders** | **List[str]** |  | [optional] 
**is_empty** | **bool** |  | [optional] [readonly] 

## Example

```python
from jellyfin.generated.api_10_11.models.library_update_info import LibraryUpdateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryUpdateInfo from a JSON string
library_update_info_instance = LibraryUpdateInfo.from_json(json)
# print the JSON string representation of the object
print(LibraryUpdateInfo.to_json())

# convert the object into a dict
library_update_info_dict = library_update_info_instance.to_dict()
# create an instance of LibraryUpdateInfo from a dict
library_update_info_from_dict = LibraryUpdateInfo.from_dict(library_update_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


