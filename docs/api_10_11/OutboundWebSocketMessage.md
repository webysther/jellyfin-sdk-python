# OutboundWebSocketMessage

Represents the list of possible outbound websocket types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GroupUpdate**](GroupUpdate.md) | Group update data | [optional] 
**message_id** | **str** | Gets or sets the message id. | [optional] 
**message_type** | [**SessionMessageType**](SessionMessageType.md) | The different kinds of messages that are used in the WebSocket api. | [optional] [readonly] [default to SessionMessageType.SYNCPLAYGROUPUPDATE]

## Example

```python
from jellyfin.generated.api_10_11.models.outbound_web_socket_message import OutboundWebSocketMessage

# TODO update the JSON string below
json = "{}"
# create an instance of OutboundWebSocketMessage from a JSON string
outbound_web_socket_message_instance = OutboundWebSocketMessage.from_json(json)
# print the JSON string representation of the object
print(OutboundWebSocketMessage.to_json())

# convert the object into a dict
outbound_web_socket_message_dict = outbound_web_socket_message_instance.to_dict()
# create an instance of OutboundWebSocketMessage from a dict
outbound_web_socket_message_from_dict = OutboundWebSocketMessage.from_dict(outbound_web_socket_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


