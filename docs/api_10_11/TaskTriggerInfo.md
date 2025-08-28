# TaskTriggerInfo

Class TaskTriggerInfo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TaskTriggerInfoType**](TaskTriggerInfoType.md) | Gets or sets the type. | [optional] 
**time_of_day_ticks** | **int** | Gets or sets the time of day. | [optional] 
**interval_ticks** | **int** | Gets or sets the interval. | [optional] 
**day_of_week** | [**DayOfWeek**](DayOfWeek.md) | Gets or sets the day of week. | [optional] 
**max_runtime_ticks** | **int** | Gets or sets the maximum runtime ticks. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.task_trigger_info import TaskTriggerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTriggerInfo from a JSON string
task_trigger_info_instance = TaskTriggerInfo.from_json(json)
# print the JSON string representation of the object
print(TaskTriggerInfo.to_json())

# convert the object into a dict
task_trigger_info_dict = task_trigger_info_instance.to_dict()
# create an instance of TaskTriggerInfo from a dict
task_trigger_info_from_dict = TaskTriggerInfo.from_dict(task_trigger_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


