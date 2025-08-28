# ForceKeepAliveMessage

Force keep alive websocket messages.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **int** | Gets or sets the data. | [optional] 
**message_id** | **str** | Gets or sets the message id. | [optional] 
**message_type** | [**SessionMessageType**](SessionMessageType.md) | The different kinds of messages that are used in the WebSocket api. | [optional] [readonly] [default to SessionMessageType.FORCEKEEPALIVE]

## Example

```python
from jellyfin.generated.api_10_11.models.force_keep_alive_message import ForceKeepAliveMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ForceKeepAliveMessage from a JSON string
force_keep_alive_message_instance = ForceKeepAliveMessage.from_json(json)
# print the JSON string representation of the object
print(ForceKeepAliveMessage.to_json())

# convert the object into a dict
force_keep_alive_message_dict = force_keep_alive_message_instance.to_dict()
# create an instance of ForceKeepAliveMessage from a dict
force_keep_alive_message_from_dict = ForceKeepAliveMessage.from_dict(force_keep_alive_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


