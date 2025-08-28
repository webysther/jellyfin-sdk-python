# SessionsMessage

Sessions message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SessionInfoDto]**](SessionInfoDto.md) | Gets or sets the data. | [optional] 
**message_id** | **str** | Gets or sets the message id. | [optional] 
**message_type** | [**SessionMessageType**](SessionMessageType.md) |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.sessions_message import SessionsMessage

# TODO update the JSON string below
json = "{}"
# create an instance of SessionsMessage from a JSON string
sessions_message_instance = SessionsMessage.from_json(json)
# print the JSON string representation of the object
print(SessionsMessage.to_json())

# convert the object into a dict
sessions_message_dict = sessions_message_instance.to_dict()
# create an instance of SessionsMessage from a dict
sessions_message_from_dict = SessionsMessage.from_dict(sessions_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


