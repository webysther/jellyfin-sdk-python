# TunerChannelMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**provider_channel_name** | **str** |  | [optional] 
**provider_channel_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.tuner_channel_mapping import TunerChannelMapping

# TODO update the JSON string below
json = "{}"
# create an instance of TunerChannelMapping from a JSON string
tuner_channel_mapping_instance = TunerChannelMapping.from_json(json)
# print the JSON string representation of the object
print(TunerChannelMapping.to_json())

# convert the object into a dict
tuner_channel_mapping_dict = tuner_channel_mapping_instance.to_dict()
# create an instance of TunerChannelMapping from a dict
tuner_channel_mapping_from_dict = TunerChannelMapping.from_dict(tuner_channel_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


