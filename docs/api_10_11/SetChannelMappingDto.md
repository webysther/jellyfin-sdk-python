# SetChannelMappingDto

Set channel mapping dto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | Gets or sets the provider id. | 
**tuner_channel_id** | **str** | Gets or sets the tuner channel id. | 
**provider_channel_id** | **str** | Gets or sets the provider channel id. | 

## Example

```python
from jellyfin.generated.api_10_11.models.set_channel_mapping_dto import SetChannelMappingDto

# TODO update the JSON string below
json = "{}"
# create an instance of SetChannelMappingDto from a JSON string
set_channel_mapping_dto_instance = SetChannelMappingDto.from_json(json)
# print the JSON string representation of the object
print(SetChannelMappingDto.to_json())

# convert the object into a dict
set_channel_mapping_dto_dict = set_channel_mapping_dto_instance.to_dict()
# create an instance of SetChannelMappingDto from a dict
set_channel_mapping_dto_from_dict = SetChannelMappingDto.from_dict(set_channel_mapping_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


