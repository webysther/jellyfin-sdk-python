# SyncPlayCommandMessage

Sync play command.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SendCommand**](SendCommand.md) | Class SendCommand. | [optional] 
**message_id** | **str** | Gets or sets the message id. | [optional] 
**message_type** | [**SessionMessageType**](SessionMessageType.md) | The different kinds of messages that are used in the WebSocket api. | [optional] [readonly] [default to SessionMessageType.SYNCPLAYCOMMAND]

## Example

```python
from jellyfin.generated.api_10_11.models.sync_play_command_message import SyncPlayCommandMessage

# TODO update the JSON string below
json = "{}"
# create an instance of SyncPlayCommandMessage from a JSON string
sync_play_command_message_instance = SyncPlayCommandMessage.from_json(json)
# print the JSON string representation of the object
print(SyncPlayCommandMessage.to_json())

# convert the object into a dict
sync_play_command_message_dict = sync_play_command_message_instance.to_dict()
# create an instance of SyncPlayCommandMessage from a dict
sync_play_command_message_from_dict = SyncPlayCommandMessage.from_dict(sync_play_command_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


