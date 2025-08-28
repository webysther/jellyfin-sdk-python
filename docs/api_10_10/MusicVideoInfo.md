# MusicVideoInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets the name. | [optional] 
**original_title** | **str** | Gets or sets the original title. | [optional] 
**path** | **str** | Gets or sets the path. | [optional] 
**metadata_language** | **str** | Gets or sets the metadata language. | [optional] 
**metadata_country_code** | **str** | Gets or sets the metadata country code. | [optional] 
**provider_ids** | **Dict[str, Optional[str]]** | Gets or sets the provider ids. | [optional] 
**year** | **int** | Gets or sets the year. | [optional] 
**index_number** | **int** |  | [optional] 
**parent_index_number** | **int** |  | [optional] 
**premiere_date** | **datetime** |  | [optional] 
**is_automated** | **bool** |  | [optional] 
**artists** | **List[str]** |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.music_video_info import MusicVideoInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MusicVideoInfo from a JSON string
music_video_info_instance = MusicVideoInfo.from_json(json)
# print the JSON string representation of the object
print(MusicVideoInfo.to_json())

# convert the object into a dict
music_video_info_dict = music_video_info_instance.to_dict()
# create an instance of MusicVideoInfo from a dict
music_video_info_from_dict = MusicVideoInfo.from_dict(music_video_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


