# AccessSchedule

An entity representing a user's access schedule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Gets the id of this instance. | [optional] [readonly] 
**user_id** | **str** | Gets the id of the associated user. | [optional] 
**day_of_week** | [**DynamicDayOfWeek**](DynamicDayOfWeek.md) | Gets or sets the day of week. | [optional] 
**start_hour** | **float** | Gets or sets the start hour. | [optional] 
**end_hour** | **float** | Gets or sets the end hour. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.access_schedule import AccessSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of AccessSchedule from a JSON string
access_schedule_instance = AccessSchedule.from_json(json)
# print the JSON string representation of the object
print(AccessSchedule.to_json())

# convert the object into a dict
access_schedule_dict = access_schedule_instance.to_dict()
# create an instance of AccessSchedule from a dict
access_schedule_from_dict = AccessSchedule.from_dict(access_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


