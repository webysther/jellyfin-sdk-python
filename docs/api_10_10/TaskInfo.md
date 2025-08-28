# TaskInfo

Class TaskInfo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets the name. | [optional] 
**state** | [**TaskState**](TaskState.md) |  | [optional] 
**current_progress_percentage** | **float** | Gets or sets the progress. | [optional] 
**id** | **str** | Gets or sets the id. | [optional] 
**last_execution_result** | [**TaskResult**](TaskResult.md) |  | [optional] 
**triggers** | [**List[TaskTriggerInfo]**](TaskTriggerInfo.md) | Gets or sets the triggers. | [optional] 
**description** | **str** | Gets or sets the description. | [optional] 
**category** | **str** | Gets or sets the category. | [optional] 
**is_hidden** | **bool** | Gets or sets a value indicating whether this instance is hidden. | [optional] 
**key** | **str** | Gets or sets the key. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.task_info import TaskInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TaskInfo from a JSON string
task_info_instance = TaskInfo.from_json(json)
# print the JSON string representation of the object
print(TaskInfo.to_json())

# convert the object into a dict
task_info_dict = task_info_instance.to_dict()
# create an instance of TaskInfo from a dict
task_info_from_dict = TaskInfo.from_dict(task_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


