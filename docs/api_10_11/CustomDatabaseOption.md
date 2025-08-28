# CustomDatabaseOption

The custom value option for custom database providers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Gets or sets the key of the value. | [optional] 
**value** | **str** | Gets or sets the value. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.custom_database_option import CustomDatabaseOption

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDatabaseOption from a JSON string
custom_database_option_instance = CustomDatabaseOption.from_json(json)
# print the JSON string representation of the object
print(CustomDatabaseOption.to_json())

# convert the object into a dict
custom_database_option_dict = custom_database_option_instance.to_dict()
# create an instance of CustomDatabaseOption from a dict
custom_database_option_from_dict = CustomDatabaseOption.from_dict(custom_database_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


