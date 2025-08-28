# ScheduledTaskEndedMessage

Scheduled task ended message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TaskResult**](TaskResult.md) |  | [optional] 
**message_id** | **str** | Gets or sets the message id. | [optional] 
**message_type** | [**SessionMessageType**](SessionMessageType.md) |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.scheduled_task_ended_message import ScheduledTaskEndedMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTaskEndedMessage from a JSON string
scheduled_task_ended_message_instance = ScheduledTaskEndedMessage.from_json(json)
# print the JSON string representation of the object
print(ScheduledTaskEndedMessage.to_json())

# convert the object into a dict
scheduled_task_ended_message_dict = scheduled_task_ended_message_instance.to_dict()
# create an instance of ScheduledTaskEndedMessage from a dict
scheduled_task_ended_message_from_dict = ScheduledTaskEndedMessage.from_dict(scheduled_task_ended_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


