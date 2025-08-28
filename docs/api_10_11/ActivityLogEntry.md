# ActivityLogEntry

An activity log entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Gets or sets the identifier. | [optional] 
**name** | **str** | Gets or sets the name. | [optional] 
**overview** | **str** | Gets or sets the overview. | [optional] 
**short_overview** | **str** | Gets or sets the short overview. | [optional] 
**type** | **str** | Gets or sets the type. | [optional] 
**item_id** | **str** | Gets or sets the item identifier. | [optional] 
**var_date** | **datetime** | Gets or sets the date. | [optional] 
**user_id** | **str** | Gets or sets the user identifier. | [optional] 
**user_primary_image_tag** | **str** | Gets or sets the user primary image tag. | [optional] 
**severity** | [**LogLevel**](LogLevel.md) | Gets or sets the log severity. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.activity_log_entry import ActivityLogEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityLogEntry from a JSON string
activity_log_entry_instance = ActivityLogEntry.from_json(json)
# print the JSON string representation of the object
print(ActivityLogEntry.to_json())

# convert the object into a dict
activity_log_entry_dict = activity_log_entry_instance.to_dict()
# create an instance of ActivityLogEntry from a dict
activity_log_entry_from_dict = ActivityLogEntry.from_dict(activity_log_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


