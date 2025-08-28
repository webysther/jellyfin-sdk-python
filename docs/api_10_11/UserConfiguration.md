# UserConfiguration

Class UserConfiguration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audio_language_preference** | **str** | Gets or sets the audio language preference. | [optional] 
**play_default_audio_track** | **bool** | Gets or sets a value indicating whether [play default audio track]. | [optional] 
**subtitle_language_preference** | **str** | Gets or sets the subtitle language preference. | [optional] 
**display_missing_episodes** | **bool** |  | [optional] 
**grouped_folders** | **List[str]** |  | [optional] 
**subtitle_mode** | [**SubtitlePlaybackMode**](SubtitlePlaybackMode.md) | An enum representing a subtitle playback mode. | [optional] 
**display_collections_view** | **bool** |  | [optional] 
**enable_local_password** | **bool** |  | [optional] 
**ordered_views** | **List[str]** |  | [optional] 
**latest_items_excludes** | **List[str]** |  | [optional] 
**my_media_excludes** | **List[str]** |  | [optional] 
**hide_played_in_latest** | **bool** |  | [optional] 
**remember_audio_selections** | **bool** |  | [optional] 
**remember_subtitle_selections** | **bool** |  | [optional] 
**enable_next_episode_auto_play** | **bool** |  | [optional] 
**cast_receiver_id** | **str** | Gets or sets the id of the selected cast receiver. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.user_configuration import UserConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of UserConfiguration from a JSON string
user_configuration_instance = UserConfiguration.from_json(json)
# print the JSON string representation of the object
print(UserConfiguration.to_json())

# convert the object into a dict
user_configuration_dict = user_configuration_instance.to_dict()
# create an instance of UserConfiguration from a dict
user_configuration_from_dict = UserConfiguration.from_dict(user_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


