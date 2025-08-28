# UserDataChangedMessage

User data changed message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserDataChangeInfo**](UserDataChangeInfo.md) | Class UserDataChangeInfo. | [optional] 
**message_id** | **str** | Gets or sets the message id. | [optional] 
**message_type** | [**SessionMessageType**](SessionMessageType.md) | The different kinds of messages that are used in the WebSocket api. | [optional] [readonly] [default to SessionMessageType.USERDATACHANGED]

## Example

```python
from jellyfin.generated.api_10_11.models.user_data_changed_message import UserDataChangedMessage

# TODO update the JSON string below
json = "{}"
# create an instance of UserDataChangedMessage from a JSON string
user_data_changed_message_instance = UserDataChangedMessage.from_json(json)
# print the JSON string representation of the object
print(UserDataChangedMessage.to_json())

# convert the object into a dict
user_data_changed_message_dict = user_data_changed_message_instance.to_dict()
# create an instance of UserDataChangedMessage from a dict
user_data_changed_message_from_dict = UserDataChangedMessage.from_dict(user_data_changed_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


