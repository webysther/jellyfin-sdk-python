# ChannelMappingOptionsDto

Channel mapping options dto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tuner_channels** | [**List[TunerChannelMapping]**](TunerChannelMapping.md) | Gets or sets list of tuner channels. | [optional] 
**provider_channels** | [**List[NameIdPair]**](NameIdPair.md) | Gets or sets list of provider channels. | [optional] 
**mappings** | [**List[NameValuePair]**](NameValuePair.md) | Gets or sets list of mappings. | [optional] 
**provider_name** | **str** | Gets or sets provider name. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.channel_mapping_options_dto import ChannelMappingOptionsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelMappingOptionsDto from a JSON string
channel_mapping_options_dto_instance = ChannelMappingOptionsDto.from_json(json)
# print the JSON string representation of the object
print(ChannelMappingOptionsDto.to_json())

# convert the object into a dict
channel_mapping_options_dto_dict = channel_mapping_options_dto_instance.to_dict()
# create an instance of ChannelMappingOptionsDto from a dict
channel_mapping_options_dto_from_dict = ChannelMappingOptionsDto.from_dict(channel_mapping_options_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


