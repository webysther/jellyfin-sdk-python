# TimerInfoDtoQueryResult

Query result container.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[TimerInfoDto]**](TimerInfoDto.md) | Gets or sets the items. | [optional] 
**total_record_count** | **int** | Gets or sets the total number of records available. | [optional] 
**start_index** | **int** | Gets or sets the index of the first record in Items. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.timer_info_dto_query_result import TimerInfoDtoQueryResult

# TODO update the JSON string below
json = "{}"
# create an instance of TimerInfoDtoQueryResult from a JSON string
timer_info_dto_query_result_instance = TimerInfoDtoQueryResult.from_json(json)
# print the JSON string representation of the object
print(TimerInfoDtoQueryResult.to_json())

# convert the object into a dict
timer_info_dto_query_result_dict = timer_info_dto_query_result_instance.to_dict()
# create an instance of TimerInfoDtoQueryResult from a dict
timer_info_dto_query_result_from_dict = TimerInfoDtoQueryResult.from_dict(timer_info_dto_query_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


