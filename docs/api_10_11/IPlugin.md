# IPlugin

Defines the MediaBrowser.Common.Plugins.IPlugin.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets the name of the plugin. | [optional] [readonly] 
**description** | **str** | Gets the Description. | [optional] [readonly] 
**id** | **str** | Gets the unique id. | [optional] [readonly] 
**version** | **str** | Gets the plugin version. | [optional] [readonly] 
**assembly_file_path** | **str** | Gets the path to the assembly file. | [optional] [readonly] 
**can_uninstall** | **bool** | Gets a value indicating whether the plugin can be uninstalled. | [optional] [readonly] 
**data_folder_path** | **str** | Gets the full path to the data folder, where the plugin can store any miscellaneous files needed. | [optional] [readonly] 

## Example

```python
from jellyfin.generated.api_10_11.models.i_plugin import IPlugin

# TODO update the JSON string below
json = "{}"
# create an instance of IPlugin from a JSON string
i_plugin_instance = IPlugin.from_json(json)
# print the JSON string representation of the object
print(IPlugin.to_json())

# convert the object into a dict
i_plugin_dict = i_plugin_instance.to_dict()
# create an instance of IPlugin from a dict
i_plugin_from_dict = IPlugin.from_dict(i_plugin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


