# RefreshProgressMessage

Refresh progress message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, Optional[str]]** | Gets or sets the data. | [optional] 
**message_id** | **str** | Gets or sets the message id. | [optional] 
**message_type** | [**SessionMessageType**](SessionMessageType.md) | The different kinds of messages that are used in the WebSocket api. | [optional] [readonly] [default to SessionMessageType.REFRESHPROGRESS]

## Example

```python
from jellyfin.generated.api_10_11.models.refresh_progress_message import RefreshProgressMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshProgressMessage from a JSON string
refresh_progress_message_instance = RefreshProgressMessage.from_json(json)
# print the JSON string representation of the object
print(RefreshProgressMessage.to_json())

# convert the object into a dict
refresh_progress_message_dict = refresh_progress_message_instance.to_dict()
# create an instance of RefreshProgressMessage from a dict
refresh_progress_message_from_dict = RefreshProgressMessage.from_dict(refresh_progress_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


