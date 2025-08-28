# TunerHostInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**device_id** | **str** |  | [optional] 
**friendly_name** | **str** |  | [optional] 
**import_favorites_only** | **bool** |  | [optional] 
**allow_hw_transcoding** | **bool** |  | [optional] 
**allow_fmp4_transcoding_container** | **bool** |  | [optional] 
**allow_stream_sharing** | **bool** |  | [optional] 
**fallback_max_streaming_bitrate** | **int** |  | [optional] 
**enable_stream_looping** | **bool** |  | [optional] 
**source** | **str** |  | [optional] 
**tuner_count** | **int** |  | [optional] 
**user_agent** | **str** |  | [optional] 
**ignore_dts** | **bool** |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.tuner_host_info import TunerHostInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TunerHostInfo from a JSON string
tuner_host_info_instance = TunerHostInfo.from_json(json)
# print the JSON string representation of the object
print(TunerHostInfo.to_json())

# convert the object into a dict
tuner_host_info_dict = tuner_host_info_instance.to_dict()
# create an instance of TunerHostInfo from a dict
tuner_host_info_from_dict = TunerHostInfo.from_dict(tuner_host_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


