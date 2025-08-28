# TrickplayInfoDto

The trickplay api model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**width** | **int** | Gets the width of an individual thumbnail. | [optional] 
**height** | **int** | Gets the height of an individual thumbnail. | [optional] 
**tile_width** | **int** | Gets the amount of thumbnails per row. | [optional] 
**tile_height** | **int** | Gets the amount of thumbnails per column. | [optional] 
**thumbnail_count** | **int** | Gets the total amount of non-black thumbnails. | [optional] 
**interval** | **int** | Gets the interval in milliseconds between each trickplay thumbnail. | [optional] 
**bandwidth** | **int** | Gets the peak bandwidth usage in bits per second. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.trickplay_info_dto import TrickplayInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of TrickplayInfoDto from a JSON string
trickplay_info_dto_instance = TrickplayInfoDto.from_json(json)
# print the JSON string representation of the object
print(TrickplayInfoDto.to_json())

# convert the object into a dict
trickplay_info_dto_dict = trickplay_info_dto_instance.to_dict()
# create an instance of TrickplayInfoDto from a dict
trickplay_info_dto_from_dict = TrickplayInfoDto.from_dict(trickplay_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


