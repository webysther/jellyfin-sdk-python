# StartupRemoteAccessDto

Startup remote access dto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_remote_access** | **bool** | Gets or sets a value indicating whether enable remote access. | 
**enable_automatic_port_mapping** | **bool** | Gets or sets a value indicating whether enable automatic port mapping. | 

## Example

```python
from jellyfin.generated.api_10_10.models.startup_remote_access_dto import StartupRemoteAccessDto

# TODO update the JSON string below
json = "{}"
# create an instance of StartupRemoteAccessDto from a JSON string
startup_remote_access_dto_instance = StartupRemoteAccessDto.from_json(json)
# print the JSON string representation of the object
print(StartupRemoteAccessDto.to_json())

# convert the object into a dict
startup_remote_access_dto_dict = startup_remote_access_dto_instance.to_dict()
# create an instance of StartupRemoteAccessDto from a dict
startup_remote_access_dto_from_dict = StartupRemoteAccessDto.from_dict(startup_remote_access_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


