# InboundWebSocketMessage

Represents the list of possible inbound websocket types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | Gets or sets the data. | [optional] 
**message_type** | [**SessionMessageType**](SessionMessageType.md) | The different kinds of messages that are used in the WebSocket api. | [optional] [readonly] [default to SessionMessageType.SESSIONSSTOP]

## Example

```python
from jellyfin.generated.api_10_11.models.inbound_web_socket_message import InboundWebSocketMessage

# TODO update the JSON string below
json = "{}"
# create an instance of InboundWebSocketMessage from a JSON string
inbound_web_socket_message_instance = InboundWebSocketMessage.from_json(json)
# print the JSON string representation of the object
print(InboundWebSocketMessage.to_json())

# convert the object into a dict
inbound_web_socket_message_dict = inbound_web_socket_message_instance.to_dict()
# create an instance of InboundWebSocketMessage from a dict
inbound_web_socket_message_from_dict = InboundWebSocketMessage.from_dict(inbound_web_socket_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


