# TypeOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**metadata_fetchers** | **List[str]** |  | [optional] 
**metadata_fetcher_order** | **List[str]** |  | [optional] 
**image_fetchers** | **List[str]** |  | [optional] 
**image_fetcher_order** | **List[str]** |  | [optional] 
**image_options** | [**List[ImageOption]**](ImageOption.md) |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.type_options import TypeOptions

# TODO update the JSON string below
json = "{}"
# create an instance of TypeOptions from a JSON string
type_options_instance = TypeOptions.from_json(json)
# print the JSON string representation of the object
print(TypeOptions.to_json())

# convert the object into a dict
type_options_dict = type_options_instance.to_dict()
# create an instance of TypeOptions from a dict
type_options_from_dict = TypeOptions.from_dict(type_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


