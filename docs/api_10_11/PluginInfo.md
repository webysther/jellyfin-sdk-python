# PluginInfo

This is a serializable stub class that is used by the api to provide information about installed plugins.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets the name. | [optional] 
**version** | **str** | Gets or sets the version. | [optional] 
**configuration_file_name** | **str** | Gets or sets the name of the configuration file. | [optional] 
**description** | **str** | Gets or sets the description. | [optional] 
**id** | **str** | Gets or sets the unique id. | [optional] 
**can_uninstall** | **bool** | Gets or sets a value indicating whether the plugin can be uninstalled. | [optional] 
**has_image** | **bool** | Gets or sets a value indicating whether this plugin has a valid image. | [optional] 
**status** | [**PluginStatus**](PluginStatus.md) | Gets or sets a value indicating the status of the plugin. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.plugin_info import PluginInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PluginInfo from a JSON string
plugin_info_instance = PluginInfo.from_json(json)
# print the JSON string representation of the object
print(PluginInfo.to_json())

# convert the object into a dict
plugin_info_dict = plugin_info_instance.to_dict()
# create an instance of PluginInfo from a dict
plugin_info_from_dict = PluginInfo.from_dict(plugin_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


