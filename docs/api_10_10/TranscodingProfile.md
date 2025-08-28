# TranscodingProfile

A class for transcoding profile information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container** | **str** | Gets or sets the container. | [optional] 
**type** | [**DlnaProfileType**](DlnaProfileType.md) |  | [optional] 
**video_codec** | **str** | Gets or sets the video codec. | [optional] 
**audio_codec** | **str** | Gets or sets the audio codec. | [optional] 
**protocol** | [**MediaStreamProtocol**](MediaStreamProtocol.md) |  | [optional] 
**estimate_content_length** | **bool** | Gets or sets a value indicating whether the content length should be estimated. | [optional] [default to False]
**enable_mpegts_m2_ts_mode** | **bool** | Gets or sets a value indicating whether M2TS mode is enabled. | [optional] [default to False]
**transcode_seek_info** | [**TranscodeSeekInfo**](TranscodeSeekInfo.md) |  | [optional] 
**copy_timestamps** | **bool** | Gets or sets a value indicating whether timestamps should be copied. | [optional] [default to False]
**context** | [**EncodingContext**](EncodingContext.md) |  | [optional] 
**enable_subtitles_in_manifest** | **bool** | Gets or sets a value indicating whether subtitles are allowed in the manifest. | [optional] [default to False]
**max_audio_channels** | **str** | Gets or sets the maximum audio channels. | [optional] 
**min_segments** | **int** | Gets or sets the minimum amount of segments. | [optional] [default to 0]
**segment_length** | **int** | Gets or sets the segment length. | [optional] [default to 0]
**break_on_non_key_frames** | **bool** | Gets or sets a value indicating whether breaking the video stream on non-keyframes is supported. | [optional] [default to False]
**conditions** | [**List[ProfileCondition]**](ProfileCondition.md) | Gets or sets the profile conditions. | [optional] 
**enable_audio_vbr_encoding** | **bool** | Gets or sets a value indicating whether variable bitrate encoding is supported. | [optional] [default to True]

## Example

```python
from jellyfin.generated.api_10_10.models.transcoding_profile import TranscodingProfile

# TODO update the JSON string below
json = "{}"
# create an instance of TranscodingProfile from a JSON string
transcoding_profile_instance = TranscodingProfile.from_json(json)
# print the JSON string representation of the object
print(TranscodingProfile.to_json())

# convert the object into a dict
transcoding_profile_dict = transcoding_profile_instance.to_dict()
# create an instance of TranscodingProfile from a dict
transcoding_profile_from_dict = TranscodingProfile.from_dict(transcoding_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


