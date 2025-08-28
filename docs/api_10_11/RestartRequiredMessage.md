# RestartRequiredMessage

Restart required.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | Gets or sets the message id. | [optional] 
**message_type** | [**SessionMessageType**](SessionMessageType.md) | The different kinds of messages that are used in the WebSocket api. | [optional] [readonly] [default to SessionMessageType.RESTARTREQUIRED]

## Example

```python
from jellyfin.generated.api_10_11.models.restart_required_message import RestartRequiredMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RestartRequiredMessage from a JSON string
restart_required_message_instance = RestartRequiredMessage.from_json(json)
# print the JSON string representation of the object
print(RestartRequiredMessage.to_json())

# convert the object into a dict
restart_required_message_dict = restart_required_message_instance.to_dict()
# create an instance of RestartRequiredMessage from a dict
restart_required_message_from_dict = RestartRequiredMessage.from_dict(restart_required_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


