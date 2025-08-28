# TrickplayOptions

Class TrickplayOptions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_hw_acceleration** | **bool** | Gets or sets a value indicating whether or not to use HW acceleration. | [optional] 
**enable_hw_encoding** | **bool** | Gets or sets a value indicating whether or not to use HW accelerated MJPEG encoding. | [optional] 
**enable_key_frame_only_extraction** | **bool** | Gets or sets a value indicating whether to only extract key frames.  Significantly faster, but is not compatible with all decoders and/or video files. | [optional] 
**scan_behavior** | [**TrickplayScanBehavior**](TrickplayScanBehavior.md) |  | [optional] 
**process_priority** | [**ProcessPriorityClass**](ProcessPriorityClass.md) |  | [optional] 
**interval** | **int** | Gets or sets the interval, in ms, between each new trickplay image. | [optional] 
**width_resolutions** | **List[int]** | Gets or sets the target width resolutions, in px, to generates preview images for. | [optional] 
**tile_width** | **int** | Gets or sets number of tile images to allow in X dimension. | [optional] 
**tile_height** | **int** | Gets or sets number of tile images to allow in Y dimension. | [optional] 
**qscale** | **int** | Gets or sets the ffmpeg output quality level. | [optional] 
**jpeg_quality** | **int** | Gets or sets the jpeg quality to use for image tiles. | [optional] 
**process_threads** | **int** | Gets or sets the number of threads to be used by ffmpeg. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.trickplay_options import TrickplayOptions

# TODO update the JSON string below
json = "{}"
# create an instance of TrickplayOptions from a JSON string
trickplay_options_instance = TrickplayOptions.from_json(json)
# print the JSON string representation of the object
print(TrickplayOptions.to_json())

# convert the object into a dict
trickplay_options_dict = trickplay_options_instance.to_dict()
# create an instance of TrickplayOptions from a dict
trickplay_options_from_dict = TrickplayOptions.from_dict(trickplay_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


