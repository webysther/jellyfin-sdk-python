# XbmcMetadataOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**release_date_format** | **str** |  | [optional] 
**save_image_paths_in_nfo** | **bool** |  | [optional] 
**enable_path_substitution** | **bool** |  | [optional] 
**enable_extra_thumbs_duplication** | **bool** |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.xbmc_metadata_options import XbmcMetadataOptions

# TODO update the JSON string below
json = "{}"
# create an instance of XbmcMetadataOptions from a JSON string
xbmc_metadata_options_instance = XbmcMetadataOptions.from_json(json)
# print the JSON string representation of the object
print(XbmcMetadataOptions.to_json())

# convert the object into a dict
xbmc_metadata_options_dict = xbmc_metadata_options_instance.to_dict()
# create an instance of XbmcMetadataOptions from a dict
xbmc_metadata_options_from_dict = XbmcMetadataOptions.from_dict(xbmc_metadata_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


