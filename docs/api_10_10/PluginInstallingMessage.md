# PluginInstallingMessage

Package installing message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**InstallationInfo**](InstallationInfo.md) |  | [optional] 
**message_id** | **str** | Gets or sets the message id. | [optional] 
**message_type** | [**SessionMessageType**](SessionMessageType.md) |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.plugin_installing_message import PluginInstallingMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PluginInstallingMessage from a JSON string
plugin_installing_message_instance = PluginInstallingMessage.from_json(json)
# print the JSON string representation of the object
print(PluginInstallingMessage.to_json())

# convert the object into a dict
plugin_installing_message_dict = plugin_installing_message_instance.to_dict()
# create an instance of PluginInstallingMessage from a dict
plugin_installing_message_from_dict = PluginInstallingMessage.from_dict(plugin_installing_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


