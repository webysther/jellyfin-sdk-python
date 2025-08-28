# LibraryOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**enable_photos** | **bool** |  | [optional] 
**enable_realtime_monitor** | **bool** |  | [optional] 
**enable_lufs_scan** | **bool** |  | [optional] 
**enable_chapter_image_extraction** | **bool** |  | [optional] 
**extract_chapter_images_during_library_scan** | **bool** |  | [optional] 
**enable_trickplay_image_extraction** | **bool** |  | [optional] 
**extract_trickplay_images_during_library_scan** | **bool** |  | [optional] 
**path_infos** | [**List[MediaPathInfo]**](MediaPathInfo.md) |  | [optional] 
**save_local_metadata** | **bool** |  | [optional] 
**enable_internet_providers** | **bool** |  | [optional] 
**enable_automatic_series_grouping** | **bool** |  | [optional] 
**enable_embedded_titles** | **bool** |  | [optional] 
**enable_embedded_extras_titles** | **bool** |  | [optional] 
**enable_embedded_episode_infos** | **bool** |  | [optional] 
**automatic_refresh_interval_days** | **int** |  | [optional] 
**preferred_metadata_language** | **str** | Gets or sets the preferred metadata language. | [optional] 
**metadata_country_code** | **str** | Gets or sets the metadata country code. | [optional] 
**season_zero_display_name** | **str** |  | [optional] 
**metadata_savers** | **List[str]** |  | [optional] 
**disabled_local_metadata_readers** | **List[str]** |  | [optional] 
**local_metadata_reader_order** | **List[str]** |  | [optional] 
**disabled_subtitle_fetchers** | **List[str]** |  | [optional] 
**subtitle_fetcher_order** | **List[str]** |  | [optional] 
**disabled_media_segment_providers** | **List[str]** |  | [optional] 
**media_segment_provider_order** | **List[str]** |  | [optional] 
**skip_subtitles_if_embedded_subtitles_present** | **bool** |  | [optional] 
**skip_subtitles_if_audio_track_matches** | **bool** |  | [optional] 
**subtitle_download_languages** | **List[str]** |  | [optional] 
**require_perfect_subtitle_match** | **bool** |  | [optional] 
**save_subtitles_with_media** | **bool** |  | [optional] 
**save_lyrics_with_media** | **bool** |  | [optional] [default to False]
**save_trickplay_with_media** | **bool** |  | [optional] [default to False]
**disabled_lyric_fetchers** | **List[str]** |  | [optional] 
**lyric_fetcher_order** | **List[str]** |  | [optional] 
**prefer_nonstandard_artists_tag** | **bool** |  | [optional] [default to False]
**use_custom_tag_delimiters** | **bool** |  | [optional] [default to False]
**custom_tag_delimiters** | **List[str]** |  | [optional] 
**delimiter_whitelist** | **List[str]** |  | [optional] 
**automatically_add_to_collection** | **bool** |  | [optional] 
**allow_embedded_subtitles** | [**EmbeddedSubtitleOptions**](EmbeddedSubtitleOptions.md) | An enum representing the options to disable embedded subs. | [optional] 
**type_options** | [**List[TypeOptions]**](TypeOptions.md) |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.library_options import LibraryOptions

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryOptions from a JSON string
library_options_instance = LibraryOptions.from_json(json)
# print the JSON string representation of the object
print(LibraryOptions.to_json())

# convert the object into a dict
library_options_dict = library_options_instance.to_dict()
# create an instance of LibraryOptions from a dict
library_options_from_dict = LibraryOptions.from_dict(library_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


