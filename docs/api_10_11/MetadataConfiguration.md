# MetadataConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_file_creation_time_for_date_added** | **bool** |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.metadata_configuration import MetadataConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataConfiguration from a JSON string
metadata_configuration_instance = MetadataConfiguration.from_json(json)
# print the JSON string representation of the object
print(MetadataConfiguration.to_json())

# convert the object into a dict
metadata_configuration_dict = metadata_configuration_instance.to_dict()
# create an instance of MetadataConfiguration from a dict
metadata_configuration_from_dict = MetadataConfiguration.from_dict(metadata_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


