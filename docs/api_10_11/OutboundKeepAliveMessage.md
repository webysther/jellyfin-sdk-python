# OutboundKeepAliveMessage

Keep alive websocket messages.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | Gets or sets the message id. | [optional] 
**message_type** | [**SessionMessageType**](SessionMessageType.md) | The different kinds of messages that are used in the WebSocket api. | [optional] [readonly] [default to SessionMessageType.KEEPALIVE]

## Example

```python
from jellyfin.generated.api_10_11.models.outbound_keep_alive_message import OutboundKeepAliveMessage

# TODO update the JSON string below
json = "{}"
# create an instance of OutboundKeepAliveMessage from a JSON string
outbound_keep_alive_message_instance = OutboundKeepAliveMessage.from_json(json)
# print the JSON string representation of the object
print(OutboundKeepAliveMessage.to_json())

# convert the object into a dict
outbound_keep_alive_message_dict = outbound_keep_alive_message_instance.to_dict()
# create an instance of OutboundKeepAliveMessage from a dict
outbound_keep_alive_message_from_dict = OutboundKeepAliveMessage.from_dict(outbound_keep_alive_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


