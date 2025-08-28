# ScheduledTasksInfoStopMessage

Scheduled tasks info stop message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_type** | [**SessionMessageType**](SessionMessageType.md) |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.scheduled_tasks_info_stop_message import ScheduledTasksInfoStopMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTasksInfoStopMessage from a JSON string
scheduled_tasks_info_stop_message_instance = ScheduledTasksInfoStopMessage.from_json(json)
# print the JSON string representation of the object
print(ScheduledTasksInfoStopMessage.to_json())

# convert the object into a dict
scheduled_tasks_info_stop_message_dict = scheduled_tasks_info_stop_message_instance.to_dict()
# create an instance of ScheduledTasksInfoStopMessage from a dict
scheduled_tasks_info_stop_message_from_dict = ScheduledTasksInfoStopMessage.from_dict(scheduled_tasks_info_stop_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


