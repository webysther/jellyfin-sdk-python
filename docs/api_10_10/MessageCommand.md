# MessageCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header** | **str** |  | [optional] 
**text** | **str** |  | 
**timeout_ms** | **int** |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.message_command import MessageCommand

# TODO update the JSON string below
json = "{}"
# create an instance of MessageCommand from a JSON string
message_command_instance = MessageCommand.from_json(json)
# print the JSON string representation of the object
print(MessageCommand.to_json())

# convert the object into a dict
message_command_dict = message_command_instance.to_dict()
# create an instance of MessageCommand from a dict
message_command_from_dict = MessageCommand.from_dict(message_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


