# LiveTvOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guide_days** | **int** |  | [optional] 
**recording_path** | **str** |  | [optional] 
**movie_recording_path** | **str** |  | [optional] 
**series_recording_path** | **str** |  | [optional] 
**enable_recording_subfolders** | **bool** |  | [optional] 
**enable_original_audio_with_encoded_recordings** | **bool** |  | [optional] 
**tuner_hosts** | [**List[TunerHostInfo]**](TunerHostInfo.md) |  | [optional] 
**listing_providers** | [**List[ListingsProviderInfo]**](ListingsProviderInfo.md) |  | [optional] 
**pre_padding_seconds** | **int** |  | [optional] 
**post_padding_seconds** | **int** |  | [optional] 
**media_locations_created** | **List[str]** |  | [optional] 
**recording_post_processor** | **str** |  | [optional] 
**recording_post_processor_arguments** | **str** |  | [optional] 
**save_recording_nfo** | **bool** |  | [optional] 
**save_recording_images** | **bool** |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.live_tv_options import LiveTvOptions

# TODO update the JSON string below
json = "{}"
# create an instance of LiveTvOptions from a JSON string
live_tv_options_instance = LiveTvOptions.from_json(json)
# print the JSON string representation of the object
print(LiveTvOptions.to_json())

# convert the object into a dict
live_tv_options_dict = live_tv_options_instance.to_dict()
# create an instance of LiveTvOptions from a dict
live_tv_options_from_dict = LiveTvOptions.from_dict(live_tv_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


