# ServerRestartingMessage

Server restarting down message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | Gets or sets the message id. | [optional] 
**message_type** | [**SessionMessageType**](SessionMessageType.md) | The different kinds of messages that are used in the WebSocket api. | [optional] [readonly] [default to SessionMessageType.SERVERRESTARTING]

## Example

```python
from jellyfin.generated.api_10_11.models.server_restarting_message import ServerRestartingMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ServerRestartingMessage from a JSON string
server_restarting_message_instance = ServerRestartingMessage.from_json(json)
# print the JSON string representation of the object
print(ServerRestartingMessage.to_json())

# convert the object into a dict
server_restarting_message_dict = server_restarting_message_instance.to_dict()
# create an instance of ServerRestartingMessage from a dict
server_restarting_message_from_dict = ServerRestartingMessage.from_dict(server_restarting_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


