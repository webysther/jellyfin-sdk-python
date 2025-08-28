# GeneralCommandMessage

General command websocket message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GeneralCommand**](GeneralCommand.md) |  | [optional] 
**message_id** | **str** | Gets or sets the message id. | [optional] 
**message_type** | [**SessionMessageType**](SessionMessageType.md) |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.general_command_message import GeneralCommandMessage

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralCommandMessage from a JSON string
general_command_message_instance = GeneralCommandMessage.from_json(json)
# print the JSON string representation of the object
print(GeneralCommandMessage.to_json())

# convert the object into a dict
general_command_message_dict = general_command_message_instance.to_dict()
# create an instance of GeneralCommandMessage from a dict
general_command_message_from_dict = GeneralCommandMessage.from_dict(general_command_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


