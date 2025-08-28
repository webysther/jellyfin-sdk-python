# MetadataOptions

Class MetadataOptions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_type** | **str** |  | [optional] 
**disabled_metadata_savers** | **List[str]** |  | [optional] 
**local_metadata_reader_order** | **List[str]** |  | [optional] 
**disabled_metadata_fetchers** | **List[str]** |  | [optional] 
**metadata_fetcher_order** | **List[str]** |  | [optional] 
**disabled_image_fetchers** | **List[str]** |  | [optional] 
**image_fetcher_order** | **List[str]** |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.metadata_options import MetadataOptions

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataOptions from a JSON string
metadata_options_instance = MetadataOptions.from_json(json)
# print the JSON string representation of the object
print(MetadataOptions.to_json())

# convert the object into a dict
metadata_options_dict = metadata_options_instance.to_dict()
# create an instance of MetadataOptions from a dict
metadata_options_from_dict = MetadataOptions.from_dict(metadata_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


