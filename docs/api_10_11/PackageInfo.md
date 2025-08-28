# PackageInfo

Class PackageInfo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets the name. | [optional] 
**description** | **str** | Gets or sets a long description of the plugin containing features or helpful explanations. | [optional] 
**overview** | **str** | Gets or sets a short overview of what the plugin does. | [optional] 
**owner** | **str** | Gets or sets the owner. | [optional] 
**category** | **str** | Gets or sets the category. | [optional] 
**guid** | **str** | Gets or sets the guid of the assembly associated with this plugin.  This is used to identify the proper item for automatic updates. | [optional] 
**versions** | [**List[VersionInfo]**](VersionInfo.md) | Gets or sets the versions. | [optional] 
**image_url** | **str** | Gets or sets the image url for the package. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.package_info import PackageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PackageInfo from a JSON string
package_info_instance = PackageInfo.from_json(json)
# print the JSON string representation of the object
print(PackageInfo.to_json())

# convert the object into a dict
package_info_dict = package_info_instance.to_dict()
# create an instance of PackageInfo from a dict
package_info_from_dict = PackageInfo.from_dict(package_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


