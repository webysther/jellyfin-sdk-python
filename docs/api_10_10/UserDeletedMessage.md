# UserDeletedMessage

User deleted message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | Gets or sets the data. | [optional] 
**message_id** | **str** | Gets or sets the message id. | [optional] 
**message_type** | [**SessionMessageType**](SessionMessageType.md) |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.user_deleted_message import UserDeletedMessage

# TODO update the JSON string below
json = "{}"
# create an instance of UserDeletedMessage from a JSON string
user_deleted_message_instance = UserDeletedMessage.from_json(json)
# print the JSON string representation of the object
print(UserDeletedMessage.to_json())

# convert the object into a dict
user_deleted_message_dict = user_deleted_message_instance.to_dict()
# create an instance of UserDeletedMessage from a dict
user_deleted_message_from_dict = UserDeletedMessage.from_dict(user_deleted_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


