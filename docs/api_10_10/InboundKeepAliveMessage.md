# InboundKeepAliveMessage

Keep alive websocket messages.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_type** | [**SessionMessageType**](SessionMessageType.md) |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.inbound_keep_alive_message import InboundKeepAliveMessage

# TODO update the JSON string below
json = "{}"
# create an instance of InboundKeepAliveMessage from a JSON string
inbound_keep_alive_message_instance = InboundKeepAliveMessage.from_json(json)
# print the JSON string representation of the object
print(InboundKeepAliveMessage.to_json())

# convert the object into a dict
inbound_keep_alive_message_dict = inbound_keep_alive_message_instance.to_dict()
# create an instance of InboundKeepAliveMessage from a dict
inbound_keep_alive_message_from_dict = InboundKeepAliveMessage.from_dict(inbound_keep_alive_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


