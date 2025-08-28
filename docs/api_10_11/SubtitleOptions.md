# SubtitleOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip_if_embedded_subtitles_present** | **bool** |  | [optional] 
**skip_if_audio_track_matches** | **bool** |  | [optional] 
**download_languages** | **List[str]** |  | [optional] 
**download_movie_subtitles** | **bool** |  | [optional] 
**download_episode_subtitles** | **bool** |  | [optional] 
**open_subtitles_username** | **str** |  | [optional] 
**open_subtitles_password_hash** | **str** |  | [optional] 
**is_open_subtitle_vip_account** | **bool** |  | [optional] 
**require_perfect_match** | **bool** |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.subtitle_options import SubtitleOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SubtitleOptions from a JSON string
subtitle_options_instance = SubtitleOptions.from_json(json)
# print the JSON string representation of the object
print(SubtitleOptions.to_json())

# convert the object into a dict
subtitle_options_dict = subtitle_options_instance.to_dict()
# create an instance of SubtitleOptions from a dict
subtitle_options_from_dict = SubtitleOptions.from_dict(subtitle_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


