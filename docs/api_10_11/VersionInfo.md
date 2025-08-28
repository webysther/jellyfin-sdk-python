# VersionInfo

Defines the MediaBrowser.Model.Updates.VersionInfo class.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | Gets or sets the version. | [optional] 
**version_number** | **str** | Gets the version as a System.Version. | [optional] [readonly] 
**changelog** | **str** | Gets or sets the changelog for this version. | [optional] 
**target_abi** | **str** | Gets or sets the ABI that this version was built against. | [optional] 
**source_url** | **str** | Gets or sets the source URL. | [optional] 
**checksum** | **str** | Gets or sets a checksum for the binary. | [optional] 
**timestamp** | **str** | Gets or sets a timestamp of when the binary was built. | [optional] 
**repository_name** | **str** | Gets or sets the repository name. | [optional] 
**repository_url** | **str** | Gets or sets the repository url. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.version_info import VersionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VersionInfo from a JSON string
version_info_instance = VersionInfo.from_json(json)
# print the JSON string representation of the object
print(VersionInfo.to_json())

# convert the object into a dict
version_info_dict = version_info_instance.to_dict()
# create an instance of VersionInfo from a dict
version_info_from_dict = VersionInfo.from_dict(version_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


