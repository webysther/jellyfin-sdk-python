# StartupUserDto

The startup user DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets the username. | [optional] 
**password** | **str** | Gets or sets the user&#39;s password. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.startup_user_dto import StartupUserDto

# TODO update the JSON string below
json = "{}"
# create an instance of StartupUserDto from a JSON string
startup_user_dto_instance = StartupUserDto.from_json(json)
# print the JSON string representation of the object
print(StartupUserDto.to_json())

# convert the object into a dict
startup_user_dto_dict = startup_user_dto_instance.to_dict()
# create an instance of StartupUserDto from a dict
startup_user_dto_from_dict = StartupUserDto.from_dict(startup_user_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


