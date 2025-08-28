# UserUpdatedMessage

User updated message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserDto**](UserDto.md) | Class UserDto. | [optional] 
**message_id** | **str** | Gets or sets the message id. | [optional] 
**message_type** | [**SessionMessageType**](SessionMessageType.md) | The different kinds of messages that are used in the WebSocket api. | [optional] [readonly] [default to SessionMessageType.USERUPDATED]

## Example

```python
from jellyfin.generated.api_10_11.models.user_updated_message import UserUpdatedMessage

# TODO update the JSON string below
json = "{}"
# create an instance of UserUpdatedMessage from a JSON string
user_updated_message_instance = UserUpdatedMessage.from_json(json)
# print the JSON string representation of the object
print(UserUpdatedMessage.to_json())

# convert the object into a dict
user_updated_message_dict = user_updated_message_instance.to_dict()
# create an instance of UserUpdatedMessage from a dict
user_updated_message_from_dict = UserUpdatedMessage.from_dict(user_updated_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


