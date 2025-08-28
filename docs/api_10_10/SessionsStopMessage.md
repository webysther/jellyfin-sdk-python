# SessionsStopMessage

Sessions stop message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_type** | [**SessionMessageType**](SessionMessageType.md) |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.sessions_stop_message import SessionsStopMessage

# TODO update the JSON string below
json = "{}"
# create an instance of SessionsStopMessage from a JSON string
sessions_stop_message_instance = SessionsStopMessage.from_json(json)
# print the JSON string representation of the object
print(SessionsStopMessage.to_json())

# convert the object into a dict
sessions_stop_message_dict = sessions_stop_message_instance.to_dict()
# create an instance of SessionsStopMessage from a dict
sessions_stop_message_from_dict = SessionsStopMessage.from_dict(sessions_stop_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


