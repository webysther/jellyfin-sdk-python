# TrickplayInfo

An entity representing the metadata for a group of trickplay tiles.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**width** | **int** | Gets or sets width of an individual thumbnail. | [optional] 
**height** | **int** | Gets or sets height of an individual thumbnail. | [optional] 
**tile_width** | **int** | Gets or sets amount of thumbnails per row. | [optional] 
**tile_height** | **int** | Gets or sets amount of thumbnails per column. | [optional] 
**thumbnail_count** | **int** | Gets or sets total amount of non-black thumbnails. | [optional] 
**interval** | **int** | Gets or sets interval in milliseconds between each trickplay thumbnail. | [optional] 
**bandwidth** | **int** | Gets or sets peak bandwith usage in bits per second. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.trickplay_info import TrickplayInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TrickplayInfo from a JSON string
trickplay_info_instance = TrickplayInfo.from_json(json)
# print the JSON string representation of the object
print(TrickplayInfo.to_json())

# convert the object into a dict
trickplay_info_dict = trickplay_info_instance.to_dict()
# create an instance of TrickplayInfo from a dict
trickplay_info_from_dict = TrickplayInfo.from_dict(trickplay_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


