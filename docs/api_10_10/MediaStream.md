# MediaStream

Class MediaStream.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codec** | **str** | Gets or sets the codec. | [optional] 
**codec_tag** | **str** | Gets or sets the codec tag. | [optional] 
**language** | **str** | Gets or sets the language. | [optional] 
**color_range** | **str** | Gets or sets the color range. | [optional] 
**color_space** | **str** | Gets or sets the color space. | [optional] 
**color_transfer** | **str** | Gets or sets the color transfer. | [optional] 
**color_primaries** | **str** | Gets or sets the color primaries. | [optional] 
**dv_version_major** | **int** | Gets or sets the Dolby Vision version major. | [optional] 
**dv_version_minor** | **int** | Gets or sets the Dolby Vision version minor. | [optional] 
**dv_profile** | **int** | Gets or sets the Dolby Vision profile. | [optional] 
**dv_level** | **int** | Gets or sets the Dolby Vision level. | [optional] 
**rpu_present_flag** | **int** | Gets or sets the Dolby Vision rpu present flag. | [optional] 
**el_present_flag** | **int** | Gets or sets the Dolby Vision el present flag. | [optional] 
**bl_present_flag** | **int** | Gets or sets the Dolby Vision bl present flag. | [optional] 
**dv_bl_signal_compatibility_id** | **int** | Gets or sets the Dolby Vision bl signal compatibility id. | [optional] 
**rotation** | **int** | Gets or sets the Rotation in degrees. | [optional] 
**comment** | **str** | Gets or sets the comment. | [optional] 
**time_base** | **str** | Gets or sets the time base. | [optional] 
**codec_time_base** | **str** | Gets or sets the codec time base. | [optional] 
**title** | **str** | Gets or sets the title. | [optional] 
**video_range** | [**VideoRange**](VideoRange.md) |  | [optional] 
**video_range_type** | [**VideoRangeType**](VideoRangeType.md) |  | [optional] 
**video_do_vi_title** | **str** | Gets the video dovi title. | [optional] [readonly] 
**audio_spatial_format** | [**AudioSpatialFormat**](AudioSpatialFormat.md) |  | [optional] 
**localized_undefined** | **str** |  | [optional] 
**localized_default** | **str** |  | [optional] 
**localized_forced** | **str** |  | [optional] 
**localized_external** | **str** |  | [optional] 
**localized_hearing_impaired** | **str** |  | [optional] 
**display_title** | **str** |  | [optional] [readonly] 
**nal_length_size** | **str** |  | [optional] 
**is_interlaced** | **bool** | Gets or sets a value indicating whether this instance is interlaced. | [optional] 
**is_avc** | **bool** |  | [optional] 
**channel_layout** | **str** | Gets or sets the channel layout. | [optional] 
**bit_rate** | **int** | Gets or sets the bit rate. | [optional] 
**bit_depth** | **int** | Gets or sets the bit depth. | [optional] 
**ref_frames** | **int** | Gets or sets the reference frames. | [optional] 
**packet_length** | **int** | Gets or sets the length of the packet. | [optional] 
**channels** | **int** | Gets or sets the channels. | [optional] 
**sample_rate** | **int** | Gets or sets the sample rate. | [optional] 
**is_default** | **bool** | Gets or sets a value indicating whether this instance is default. | [optional] 
**is_forced** | **bool** | Gets or sets a value indicating whether this instance is forced. | [optional] 
**is_hearing_impaired** | **bool** | Gets or sets a value indicating whether this instance is for the hearing impaired. | [optional] 
**height** | **int** | Gets or sets the height. | [optional] 
**width** | **int** | Gets or sets the width. | [optional] 
**average_frame_rate** | **float** | Gets or sets the average frame rate. | [optional] 
**real_frame_rate** | **float** | Gets or sets the real frame rate. | [optional] 
**reference_frame_rate** | **float** | Gets the framerate used as reference.  Prefer AverageFrameRate, if that is null or an unrealistic value  then fallback to RealFrameRate. | [optional] [readonly] 
**profile** | **str** | Gets or sets the profile. | [optional] 
**type** | [**MediaStreamType**](MediaStreamType.md) |  | [optional] 
**aspect_ratio** | **str** | Gets or sets the aspect ratio. | [optional] 
**index** | **int** | Gets or sets the index. | [optional] 
**score** | **int** | Gets or sets the score. | [optional] 
**is_external** | **bool** | Gets or sets a value indicating whether this instance is external. | [optional] 
**delivery_method** | [**SubtitleDeliveryMethod**](SubtitleDeliveryMethod.md) |  | [optional] 
**delivery_url** | **str** | Gets or sets the delivery URL. | [optional] 
**is_external_url** | **bool** | Gets or sets a value indicating whether this instance is external URL. | [optional] 
**is_text_subtitle_stream** | **bool** |  | [optional] [readonly] 
**supports_external_stream** | **bool** | Gets or sets a value indicating whether [supports external stream]. | [optional] 
**path** | **str** | Gets or sets the filename. | [optional] 
**pixel_format** | **str** | Gets or sets the pixel format. | [optional] 
**level** | **float** | Gets or sets the level. | [optional] 
**is_anamorphic** | **bool** | Gets or sets whether this instance is anamorphic. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.media_stream import MediaStream

# TODO update the JSON string below
json = "{}"
# create an instance of MediaStream from a JSON string
media_stream_instance = MediaStream.from_json(json)
# print the JSON string representation of the object
print(MediaStream.to_json())

# convert the object into a dict
media_stream_dict = media_stream_instance.to_dict()
# create an instance of MediaStream from a dict
media_stream_from_dict = MediaStream.from_dict(media_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


