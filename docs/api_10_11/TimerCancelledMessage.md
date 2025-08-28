# TimerCancelledMessage

Timer cancelled message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TimerEventInfo**](TimerEventInfo.md) | Gets or sets the data. | [optional] 
**message_id** | **str** | Gets or sets the message id. | [optional] 
**message_type** | [**SessionMessageType**](SessionMessageType.md) | The different kinds of messages that are used in the WebSocket api. | [optional] [readonly] [default to SessionMessageType.TIMERCANCELLED]

## Example

```python
from jellyfin.generated.api_10_11.models.timer_cancelled_message import TimerCancelledMessage

# TODO update the JSON string below
json = "{}"
# create an instance of TimerCancelledMessage from a JSON string
timer_cancelled_message_instance = TimerCancelledMessage.from_json(json)
# print the JSON string representation of the object
print(TimerCancelledMessage.to_json())

# convert the object into a dict
timer_cancelled_message_dict = timer_cancelled_message_instance.to_dict()
# create an instance of TimerCancelledMessage from a dict
timer_cancelled_message_from_dict = TimerCancelledMessage.from_dict(timer_cancelled_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


