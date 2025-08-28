# TranscodingInfo

Class holding information on a runnning transcode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audio_codec** | **str** | Gets or sets the thread count used for encoding. | [optional] 
**video_codec** | **str** | Gets or sets the thread count used for encoding. | [optional] 
**container** | **str** | Gets or sets the thread count used for encoding. | [optional] 
**is_video_direct** | **bool** | Gets or sets a value indicating whether the video is passed through. | [optional] 
**is_audio_direct** | **bool** | Gets or sets a value indicating whether the audio is passed through. | [optional] 
**bitrate** | **int** | Gets or sets the bitrate. | [optional] 
**framerate** | **float** | Gets or sets the framerate. | [optional] 
**completion_percentage** | **float** | Gets or sets the completion percentage. | [optional] 
**width** | **int** | Gets or sets the video width. | [optional] 
**height** | **int** | Gets or sets the video height. | [optional] 
**audio_channels** | **int** | Gets or sets the audio channels. | [optional] 
**hardware_acceleration_type** | [**HardwareAccelerationType**](HardwareAccelerationType.md) |  | [optional] 
**transcode_reasons** | [**List[TranscodeReason]**](TranscodeReason.md) | Gets or sets the transcode reasons. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.transcoding_info import TranscodingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TranscodingInfo from a JSON string
transcoding_info_instance = TranscodingInfo.from_json(json)
# print the JSON string representation of the object
print(TranscodingInfo.to_json())

# convert the object into a dict
transcoding_info_dict = transcoding_info_instance.to_dict()
# create an instance of TranscodingInfo from a dict
transcoding_info_from_dict = TranscodingInfo.from_dict(transcoding_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


