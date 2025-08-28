# PluginInstallationFailedMessage

Plugin installation failed message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**InstallationInfo**](InstallationInfo.md) | Class InstallationInfo. | [optional] 
**message_id** | **str** | Gets or sets the message id. | [optional] 
**message_type** | [**SessionMessageType**](SessionMessageType.md) | The different kinds of messages that are used in the WebSocket api. | [optional] [readonly] [default to SessionMessageType.PACKAGEINSTALLATIONFAILED]

## Example

```python
from jellyfin.generated.api_10_11.models.plugin_installation_failed_message import PluginInstallationFailedMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PluginInstallationFailedMessage from a JSON string
plugin_installation_failed_message_instance = PluginInstallationFailedMessage.from_json(json)
# print the JSON string representation of the object
print(PluginInstallationFailedMessage.to_json())

# convert the object into a dict
plugin_installation_failed_message_dict = plugin_installation_failed_message_instance.to_dict()
# create an instance of PluginInstallationFailedMessage from a dict
plugin_installation_failed_message_from_dict = PluginInstallationFailedMessage.from_dict(plugin_installation_failed_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


