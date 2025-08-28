# ScheduledTasksInfoStartMessage

Scheduled tasks info start message.  Data is the timing data encoded as \"$initialDelay,$interval\" in ms.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | Gets or sets the data. | [optional] 
**message_type** | [**SessionMessageType**](SessionMessageType.md) |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.scheduled_tasks_info_start_message import ScheduledTasksInfoStartMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTasksInfoStartMessage from a JSON string
scheduled_tasks_info_start_message_instance = ScheduledTasksInfoStartMessage.from_json(json)
# print the JSON string representation of the object
print(ScheduledTasksInfoStartMessage.to_json())

# convert the object into a dict
scheduled_tasks_info_start_message_dict = scheduled_tasks_info_start_message_instance.to_dict()
# create an instance of ScheduledTasksInfoStartMessage from a dict
scheduled_tasks_info_start_message_from_dict = ScheduledTasksInfoStartMessage.from_dict(scheduled_tasks_info_start_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


