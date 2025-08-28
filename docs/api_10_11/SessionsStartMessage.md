# SessionsStartMessage

Sessions start message.  Data is the timing data encoded as \"$initialDelay,$interval\" in ms.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | Gets or sets the data. | [optional] 
**message_type** | [**SessionMessageType**](SessionMessageType.md) | The different kinds of messages that are used in the WebSocket api. | [optional] [readonly] [default to SessionMessageType.SESSIONSSTART]

## Example

```python
from jellyfin.generated.api_10_11.models.sessions_start_message import SessionsStartMessage

# TODO update the JSON string below
json = "{}"
# create an instance of SessionsStartMessage from a JSON string
sessions_start_message_instance = SessionsStartMessage.from_json(json)
# print the JSON string representation of the object
print(SessionsStartMessage.to_json())

# convert the object into a dict
sessions_start_message_dict = sessions_start_message_instance.to_dict()
# create an instance of SessionsStartMessage from a dict
sessions_start_message_from_dict = SessionsStartMessage.from_dict(sessions_start_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


