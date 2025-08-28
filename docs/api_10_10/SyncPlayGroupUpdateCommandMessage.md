# SyncPlayGroupUpdateCommandMessage

Untyped sync play command.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GroupUpdate**](GroupUpdate.md) |  | [optional] 
**message_id** | **str** | Gets or sets the message id. | [optional] 
**message_type** | [**SessionMessageType**](SessionMessageType.md) |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.sync_play_group_update_command_message import SyncPlayGroupUpdateCommandMessage

# TODO update the JSON string below
json = "{}"
# create an instance of SyncPlayGroupUpdateCommandMessage from a JSON string
sync_play_group_update_command_message_instance = SyncPlayGroupUpdateCommandMessage.from_json(json)
# print the JSON string representation of the object
print(SyncPlayGroupUpdateCommandMessage.to_json())

# convert the object into a dict
sync_play_group_update_command_message_dict = sync_play_group_update_command_message_instance.to_dict()
# create an instance of SyncPlayGroupUpdateCommandMessage from a dict
sync_play_group_update_command_message_from_dict = SyncPlayGroupUpdateCommandMessage.from_dict(sync_play_group_update_command_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


