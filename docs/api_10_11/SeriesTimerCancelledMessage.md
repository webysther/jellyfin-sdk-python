# SeriesTimerCancelledMessage

Series timer cancelled message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TimerEventInfo**](TimerEventInfo.md) | Gets or sets the data. | [optional] 
**message_id** | **str** | Gets or sets the message id. | [optional] 
**message_type** | [**SessionMessageType**](SessionMessageType.md) | The different kinds of messages that are used in the WebSocket api. | [optional] [readonly] [default to SessionMessageType.SERIESTIMERCANCELLED]

## Example

```python
from jellyfin.generated.api_10_11.models.series_timer_cancelled_message import SeriesTimerCancelledMessage

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesTimerCancelledMessage from a JSON string
series_timer_cancelled_message_instance = SeriesTimerCancelledMessage.from_json(json)
# print the JSON string representation of the object
print(SeriesTimerCancelledMessage.to_json())

# convert the object into a dict
series_timer_cancelled_message_dict = series_timer_cancelled_message_instance.to_dict()
# create an instance of SeriesTimerCancelledMessage from a dict
series_timer_cancelled_message_from_dict = SeriesTimerCancelledMessage.from_dict(series_timer_cancelled_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


