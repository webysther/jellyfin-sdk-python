# ActivityLogEntryMessage

Activity log created message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ActivityLogEntry]**](ActivityLogEntry.md) | Gets or sets the data. | [optional] 
**message_id** | **str** | Gets or sets the message id. | [optional] 
**message_type** | [**SessionMessageType**](SessionMessageType.md) | The different kinds of messages that are used in the WebSocket api. | [optional] [readonly] [default to SessionMessageType.ACTIVITYLOGENTRY]

## Example

```python
from jellyfin.generated.api_10_11.models.activity_log_entry_message import ActivityLogEntryMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityLogEntryMessage from a JSON string
activity_log_entry_message_instance = ActivityLogEntryMessage.from_json(json)
# print the JSON string representation of the object
print(ActivityLogEntryMessage.to_json())

# convert the object into a dict
activity_log_entry_message_dict = activity_log_entry_message_instance.to_dict()
# create an instance of ActivityLogEntryMessage from a dict
activity_log_entry_message_from_dict = ActivityLogEntryMessage.from_dict(activity_log_entry_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


