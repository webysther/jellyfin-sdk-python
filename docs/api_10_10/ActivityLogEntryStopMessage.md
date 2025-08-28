# ActivityLogEntryStopMessage

Activity log entry stop message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_type** | [**SessionMessageType**](SessionMessageType.md) |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.activity_log_entry_stop_message import ActivityLogEntryStopMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityLogEntryStopMessage from a JSON string
activity_log_entry_stop_message_instance = ActivityLogEntryStopMessage.from_json(json)
# print the JSON string representation of the object
print(ActivityLogEntryStopMessage.to_json())

# convert the object into a dict
activity_log_entry_stop_message_dict = activity_log_entry_stop_message_instance.to_dict()
# create an instance of ActivityLogEntryStopMessage from a dict
activity_log_entry_stop_message_from_dict = ActivityLogEntryStopMessage.from_dict(activity_log_entry_stop_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


