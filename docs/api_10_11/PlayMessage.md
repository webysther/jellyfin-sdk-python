# PlayMessage

Play command websocket message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlayRequest**](PlayRequest.md) | Class PlayRequest. | [optional] 
**message_id** | **str** | Gets or sets the message id. | [optional] 
**message_type** | [**SessionMessageType**](SessionMessageType.md) | The different kinds of messages that are used in the WebSocket api. | [optional] [readonly] [default to SessionMessageType.PLAY]

## Example

```python
from jellyfin.generated.api_10_11.models.play_message import PlayMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PlayMessage from a JSON string
play_message_instance = PlayMessage.from_json(json)
# print the JSON string representation of the object
print(PlayMessage.to_json())

# convert the object into a dict
play_message_dict = play_message_instance.to_dict()
# create an instance of PlayMessage from a dict
play_message_from_dict = PlayMessage.from_dict(play_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


