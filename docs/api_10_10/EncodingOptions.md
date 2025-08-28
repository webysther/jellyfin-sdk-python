# EncodingOptions

Class EncodingOptions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encoding_thread_count** | **int** | Gets or sets the thread count used for encoding. | [optional] 
**transcoding_temp_path** | **str** | Gets or sets the temporary transcoding path. | [optional] 
**fallback_font_path** | **str** | Gets or sets the path to the fallback font. | [optional] 
**enable_fallback_font** | **bool** | Gets or sets a value indicating whether to use the fallback font. | [optional] 
**enable_audio_vbr** | **bool** | Gets or sets a value indicating whether audio VBR is enabled. | [optional] 
**down_mix_audio_boost** | **float** | Gets or sets the audio boost applied when downmixing audio. | [optional] 
**down_mix_stereo_algorithm** | [**DownMixStereoAlgorithms**](DownMixStereoAlgorithms.md) |  | [optional] 
**max_muxing_queue_size** | **int** | Gets or sets the maximum size of the muxing queue. | [optional] 
**enable_throttling** | **bool** | Gets or sets a value indicating whether throttling is enabled. | [optional] 
**throttle_delay_seconds** | **int** | Gets or sets the delay after which throttling happens. | [optional] 
**enable_segment_deletion** | **bool** | Gets or sets a value indicating whether segment deletion is enabled. | [optional] 
**segment_keep_seconds** | **int** | Gets or sets seconds for which segments should be kept before being deleted. | [optional] 
**hardware_acceleration_type** | [**HardwareAccelerationType**](HardwareAccelerationType.md) |  | [optional] 
**encoder_app_path** | **str** | Gets or sets the FFmpeg path as set by the user via the UI. | [optional] 
**encoder_app_path_display** | **str** | Gets or sets the current FFmpeg path being used by the system and displayed on the transcode page. | [optional] 
**vaapi_device** | **str** | Gets or sets the VA-API device. | [optional] 
**qsv_device** | **str** | Gets or sets the QSV device. | [optional] 
**enable_tonemapping** | **bool** | Gets or sets a value indicating whether tonemapping is enabled. | [optional] 
**enable_vpp_tonemapping** | **bool** | Gets or sets a value indicating whether VPP tonemapping is enabled. | [optional] 
**enable_video_toolbox_tonemapping** | **bool** | Gets or sets a value indicating whether videotoolbox tonemapping is enabled. | [optional] 
**tonemapping_algorithm** | [**TonemappingAlgorithm**](TonemappingAlgorithm.md) |  | [optional] 
**tonemapping_mode** | [**TonemappingMode**](TonemappingMode.md) |  | [optional] 
**tonemapping_range** | [**TonemappingRange**](TonemappingRange.md) |  | [optional] 
**tonemapping_desat** | **float** | Gets or sets the tone-mapping desaturation. | [optional] 
**tonemapping_peak** | **float** | Gets or sets the tone-mapping peak. | [optional] 
**tonemapping_param** | **float** | Gets or sets the tone-mapping parameters. | [optional] 
**vpp_tonemapping_brightness** | **float** | Gets or sets the VPP tone-mapping brightness. | [optional] 
**vpp_tonemapping_contrast** | **float** | Gets or sets the VPP tone-mapping contrast. | [optional] 
**h264_crf** | **int** | Gets or sets the H264 CRF. | [optional] 
**h265_crf** | **int** | Gets or sets the H265 CRF. | [optional] 
**encoder_preset** | [**EncoderPreset**](EncoderPreset.md) |  | [optional] 
**deinterlace_double_rate** | **bool** | Gets or sets a value indicating whether the framerate is doubled when deinterlacing. | [optional] 
**deinterlace_method** | [**DeinterlaceMethod**](DeinterlaceMethod.md) |  | [optional] 
**enable_decoding_color_depth10_hevc** | **bool** | Gets or sets a value indicating whether 10bit HEVC decoding is enabled. | [optional] 
**enable_decoding_color_depth10_vp9** | **bool** | Gets or sets a value indicating whether 10bit VP9 decoding is enabled. | [optional] 
**enable_decoding_color_depth10_hevc_rext** | **bool** | Gets or sets a value indicating whether 8/10bit HEVC RExt decoding is enabled. | [optional] 
**enable_decoding_color_depth12_hevc_rext** | **bool** | Gets or sets a value indicating whether 12bit HEVC RExt decoding is enabled. | [optional] 
**enable_enhanced_nvdec_decoder** | **bool** | Gets or sets a value indicating whether the enhanced NVDEC is enabled. | [optional] 
**prefer_system_native_hw_decoder** | **bool** | Gets or sets a value indicating whether the system native hardware decoder should be used. | [optional] 
**enable_intel_low_power_h264_hw_encoder** | **bool** | Gets or sets a value indicating whether the Intel H264 low-power hardware encoder should be used. | [optional] 
**enable_intel_low_power_hevc_hw_encoder** | **bool** | Gets or sets a value indicating whether the Intel HEVC low-power hardware encoder should be used. | [optional] 
**enable_hardware_encoding** | **bool** | Gets or sets a value indicating whether hardware encoding is enabled. | [optional] 
**allow_hevc_encoding** | **bool** | Gets or sets a value indicating whether HEVC encoding is enabled. | [optional] 
**allow_av1_encoding** | **bool** | Gets or sets a value indicating whether AV1 encoding is enabled. | [optional] 
**enable_subtitle_extraction** | **bool** | Gets or sets a value indicating whether subtitle extraction is enabled. | [optional] 
**hardware_decoding_codecs** | **List[str]** | Gets or sets the codecs hardware encoding is used for. | [optional] 
**allow_on_demand_metadata_based_keyframe_extraction_for_extensions** | **List[str]** | Gets or sets the file extensions on-demand metadata based keyframe extraction is enabled for. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.encoding_options import EncodingOptions

# TODO update the JSON string below
json = "{}"
# create an instance of EncodingOptions from a JSON string
encoding_options_instance = EncodingOptions.from_json(json)
# print the JSON string representation of the object
print(EncodingOptions.to_json())

# convert the object into a dict
encoding_options_dict = encoding_options_instance.to_dict()
# create an instance of EncodingOptions from a dict
encoding_options_from_dict = EncodingOptions.from_dict(encoding_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


