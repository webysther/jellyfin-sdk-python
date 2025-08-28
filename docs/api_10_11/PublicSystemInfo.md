# PublicSystemInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_address** | **str** | Gets or sets the local address. | [optional] 
**server_name** | **str** | Gets or sets the name of the server. | [optional] 
**version** | **str** | Gets or sets the server version. | [optional] 
**product_name** | **str** | Gets or sets the product name. This is the AssemblyProduct name. | [optional] 
**operating_system** | **str** | Gets or sets the operating system. | [optional] 
**id** | **str** | Gets or sets the id. | [optional] 
**startup_wizard_completed** | **bool** | Gets or sets a value indicating whether the startup wizard is completed. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.public_system_info import PublicSystemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PublicSystemInfo from a JSON string
public_system_info_instance = PublicSystemInfo.from_json(json)
# print the JSON string representation of the object
print(PublicSystemInfo.to_json())

# convert the object into a dict
public_system_info_dict = public_system_info_instance.to_dict()
# create an instance of PublicSystemInfo from a dict
public_system_info_from_dict = PublicSystemInfo.from_dict(public_system_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


