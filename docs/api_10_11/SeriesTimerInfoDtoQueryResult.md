# SeriesTimerInfoDtoQueryResult

Query result container.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SeriesTimerInfoDto]**](SeriesTimerInfoDto.md) | Gets or sets the items. | [optional] 
**total_record_count** | **int** | Gets or sets the total number of records available. | [optional] 
**start_index** | **int** | Gets or sets the index of the first record in Items. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.series_timer_info_dto_query_result import SeriesTimerInfoDtoQueryResult

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesTimerInfoDtoQueryResult from a JSON string
series_timer_info_dto_query_result_instance = SeriesTimerInfoDtoQueryResult.from_json(json)
# print the JSON string representation of the object
print(SeriesTimerInfoDtoQueryResult.to_json())

# convert the object into a dict
series_timer_info_dto_query_result_dict = series_timer_info_dto_query_result_instance.to_dict()
# create an instance of SeriesTimerInfoDtoQueryResult from a dict
series_timer_info_dto_query_result_from_dict = SeriesTimerInfoDtoQueryResult.from_dict(series_timer_info_dto_query_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


