# TimerEventInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**program_id** | **str** |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.timer_event_info import TimerEventInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TimerEventInfo from a JSON string
timer_event_info_instance = TimerEventInfo.from_json(json)
# print the JSON string representation of the object
print(TimerEventInfo.to_json())

# convert the object into a dict
timer_event_info_dict = timer_event_info_instance.to_dict()
# create an instance of TimerEventInfo from a dict
timer_event_info_from_dict = TimerEventInfo.from_dict(timer_event_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


