# StartupConfigurationDto

The startup configuration DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_name** | **str** | Gets or sets the server name. | [optional] 
**ui_culture** | **str** | Gets or sets UI language culture. | [optional] 
**metadata_country_code** | **str** | Gets or sets the metadata country code. | [optional] 
**preferred_metadata_language** | **str** | Gets or sets the preferred language for the metadata. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.startup_configuration_dto import StartupConfigurationDto

# TODO update the JSON string below
json = "{}"
# create an instance of StartupConfigurationDto from a JSON string
startup_configuration_dto_instance = StartupConfigurationDto.from_json(json)
# print the JSON string representation of the object
print(StartupConfigurationDto.to_json())

# convert the object into a dict
startup_configuration_dto_dict = startup_configuration_dto_instance.to_dict()
# create an instance of StartupConfigurationDto from a dict
startup_configuration_dto_from_dict = StartupConfigurationDto.from_dict(startup_configuration_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


