# ScheduledTasksInfoMessage

Scheduled tasks info message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TaskInfo]**](TaskInfo.md) | Gets or sets the data. | [optional] 
**message_id** | **str** | Gets or sets the message id. | [optional] 
**message_type** | [**SessionMessageType**](SessionMessageType.md) |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.scheduled_tasks_info_message import ScheduledTasksInfoMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTasksInfoMessage from a JSON string
scheduled_tasks_info_message_instance = ScheduledTasksInfoMessage.from_json(json)
# print the JSON string representation of the object
print(ScheduledTasksInfoMessage.to_json())

# convert the object into a dict
scheduled_tasks_info_message_dict = scheduled_tasks_info_message_instance.to_dict()
# create an instance of ScheduledTasksInfoMessage from a dict
scheduled_tasks_info_message_from_dict = ScheduledTasksInfoMessage.from_dict(scheduled_tasks_info_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


