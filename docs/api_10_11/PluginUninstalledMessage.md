# PluginUninstalledMessage

Plugin uninstalled message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PluginInfo**](PluginInfo.md) | This is a serializable stub class that is used by the api to provide information about installed plugins. | [optional] 
**message_id** | **str** | Gets or sets the message id. | [optional] 
**message_type** | [**SessionMessageType**](SessionMessageType.md) | The different kinds of messages that are used in the WebSocket api. | [optional] [readonly] [default to SessionMessageType.PACKAGEUNINSTALLED]

## Example

```python
from jellyfin.generated.api_10_11.models.plugin_uninstalled_message import PluginUninstalledMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PluginUninstalledMessage from a JSON string
plugin_uninstalled_message_instance = PluginUninstalledMessage.from_json(json)
# print the JSON string representation of the object
print(PluginUninstalledMessage.to_json())

# convert the object into a dict
plugin_uninstalled_message_dict = plugin_uninstalled_message_instance.to_dict()
# create an instance of PluginUninstalledMessage from a dict
plugin_uninstalled_message_from_dict = PluginUninstalledMessage.from_dict(plugin_uninstalled_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


