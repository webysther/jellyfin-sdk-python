# ServerShuttingDownMessage

Server shutting down message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | Gets or sets the message id. | [optional] 
**message_type** | [**SessionMessageType**](SessionMessageType.md) | The different kinds of messages that are used in the WebSocket api. | [optional] [readonly] [default to SessionMessageType.SERVERSHUTTINGDOWN]

## Example

```python
from jellyfin.generated.api_10_11.models.server_shutting_down_message import ServerShuttingDownMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ServerShuttingDownMessage from a JSON string
server_shutting_down_message_instance = ServerShuttingDownMessage.from_json(json)
# print the JSON string representation of the object
print(ServerShuttingDownMessage.to_json())

# convert the object into a dict
server_shutting_down_message_dict = server_shutting_down_message_instance.to_dict()
# create an instance of ServerShuttingDownMessage from a dict
server_shutting_down_message_from_dict = ServerShuttingDownMessage.from_dict(server_shutting_down_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


