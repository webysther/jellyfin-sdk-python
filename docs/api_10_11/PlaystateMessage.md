# PlaystateMessage

Playstate message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlaystateRequest**](PlaystateRequest.md) | Gets or sets the data. | [optional] 
**message_id** | **str** | Gets or sets the message id. | [optional] 
**message_type** | [**SessionMessageType**](SessionMessageType.md) | The different kinds of messages that are used in the WebSocket api. | [optional] [readonly] [default to SessionMessageType.PLAYSTATE]

## Example

```python
from jellyfin.generated.api_10_11.models.playstate_message import PlaystateMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PlaystateMessage from a JSON string
playstate_message_instance = PlaystateMessage.from_json(json)
# print the JSON string representation of the object
print(PlaystateMessage.to_json())

# convert the object into a dict
playstate_message_dict = playstate_message_instance.to_dict()
# create an instance of PlaystateMessage from a dict
playstate_message_from_dict = PlaystateMessage.from_dict(playstate_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


