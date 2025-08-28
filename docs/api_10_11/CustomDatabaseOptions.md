# CustomDatabaseOptions

Defines the options for a custom database connector.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plugin_name** | **str** | Gets or sets the Plugin name to search for database providers. | [optional] 
**plugin_assembly** | **str** | Gets or sets the plugin assembly to search for providers. | [optional] 
**connection_string** | **str** | Gets or sets the connection string for the custom database provider. | [optional] 
**options** | [**List[CustomDatabaseOption]**](CustomDatabaseOption.md) | Gets or sets the list of extra options for the custom provider. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.custom_database_options import CustomDatabaseOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDatabaseOptions from a JSON string
custom_database_options_instance = CustomDatabaseOptions.from_json(json)
# print the JSON string representation of the object
print(CustomDatabaseOptions.to_json())

# convert the object into a dict
custom_database_options_dict = custom_database_options_instance.to_dict()
# create an instance of CustomDatabaseOptions from a dict
custom_database_options_from_dict = CustomDatabaseOptions.from_dict(custom_database_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


