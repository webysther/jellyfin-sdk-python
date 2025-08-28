# ActivityLogEntryQueryResult

Query result container.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ActivityLogEntry]**](ActivityLogEntry.md) | Gets or sets the items. | [optional] 
**total_record_count** | **int** | Gets or sets the total number of records available. | [optional] 
**start_index** | **int** | Gets or sets the index of the first record in Items. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.activity_log_entry_query_result import ActivityLogEntryQueryResult

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityLogEntryQueryResult from a JSON string
activity_log_entry_query_result_instance = ActivityLogEntryQueryResult.from_json(json)
# print the JSON string representation of the object
print(ActivityLogEntryQueryResult.to_json())

# convert the object into a dict
activity_log_entry_query_result_dict = activity_log_entry_query_result_instance.to_dict()
# create an instance of ActivityLogEntryQueryResult from a dict
activity_log_entry_query_result_from_dict = ActivityLogEntryQueryResult.from_dict(activity_log_entry_query_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


