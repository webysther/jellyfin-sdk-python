# ConfigImageTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backdrop_sizes** | **List[str]** |  | [optional] 
**base_url** | **str** |  | [optional] 
**logo_sizes** | **List[str]** |  | [optional] 
**poster_sizes** | **List[str]** |  | [optional] 
**profile_sizes** | **List[str]** |  | [optional] 
**secure_base_url** | **str** |  | [optional] 
**still_sizes** | **List[str]** |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.config_image_types import ConfigImageTypes

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigImageTypes from a JSON string
config_image_types_instance = ConfigImageTypes.from_json(json)
# print the JSON string representation of the object
print(ConfigImageTypes.to_json())

# convert the object into a dict
config_image_types_dict = config_image_types_instance.to_dict()
# create an instance of ConfigImageTypes from a dict
config_image_types_from_dict = ConfigImageTypes.from_dict(config_image_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


