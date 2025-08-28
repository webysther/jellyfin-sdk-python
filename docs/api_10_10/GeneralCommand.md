# GeneralCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**GeneralCommandType**](GeneralCommandType.md) |  | [optional] 
**controlling_user_id** | **str** |  | [optional] 
**arguments** | **Dict[str, Optional[str]]** |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.general_command import GeneralCommand

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralCommand from a JSON string
general_command_instance = GeneralCommand.from_json(json)
# print the JSON string representation of the object
print(GeneralCommand.to_json())

# convert the object into a dict
general_command_dict = general_command_instance.to_dict()
# create an instance of GeneralCommand from a dict
general_command_from_dict = GeneralCommand.from_dict(general_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


