# DatabaseConfigurationOptions

Options to configure jellyfins managed database.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_type** | **str** | Gets or Sets the type of database jellyfin should use. | [optional] 
**custom_provider_options** | [**CustomDatabaseOptions**](CustomDatabaseOptions.md) | Gets or sets the options required to use a custom database provider. | [optional] 
**locking_behavior** | [**DatabaseLockingBehaviorTypes**](DatabaseLockingBehaviorTypes.md) | Gets or Sets the kind of locking behavior jellyfin should perform. Possible options are \&quot;NoLock\&quot;, \&quot;Pessimistic\&quot;, \&quot;Optimistic\&quot;.  Defaults to \&quot;NoLock\&quot;. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.database_configuration_options import DatabaseConfigurationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseConfigurationOptions from a JSON string
database_configuration_options_instance = DatabaseConfigurationOptions.from_json(json)
# print the JSON string representation of the object
print(DatabaseConfigurationOptions.to_json())

# convert the object into a dict
database_configuration_options_dict = database_configuration_options_instance.to_dict()
# create an instance of DatabaseConfigurationOptions from a dict
database_configuration_options_from_dict = DatabaseConfigurationOptions.from_dict(database_configuration_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


