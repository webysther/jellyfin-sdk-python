# PluginInstallationCompletedMessage

Plugin installation completed message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**InstallationInfo**](InstallationInfo.md) | Class InstallationInfo. | [optional] 
**message_id** | **str** | Gets or sets the message id. | [optional] 
**message_type** | [**SessionMessageType**](SessionMessageType.md) | The different kinds of messages that are used in the WebSocket api. | [optional] [readonly] [default to SessionMessageType.PACKAGEINSTALLATIONCOMPLETED]

## Example

```python
from jellyfin.generated.api_10_11.models.plugin_installation_completed_message import PluginInstallationCompletedMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PluginInstallationCompletedMessage from a JSON string
plugin_installation_completed_message_instance = PluginInstallationCompletedMessage.from_json(json)
# print the JSON string representation of the object
print(PluginInstallationCompletedMessage.to_json())

# convert the object into a dict
plugin_installation_completed_message_dict = plugin_installation_completed_message_instance.to_dict()
# create an instance of PluginInstallationCompletedMessage from a dict
plugin_installation_completed_message_from_dict = PluginInstallationCompletedMessage.from_dict(plugin_installation_completed_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


