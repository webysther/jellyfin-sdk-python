# DeviceOptionsDto

A dto representing custom options for a device.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Gets or sets the id. | [optional] 
**device_id** | **str** | Gets or sets the device id. | [optional] 
**custom_name** | **str** | Gets or sets the custom name. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.device_options_dto import DeviceOptionsDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceOptionsDto from a JSON string
device_options_dto_instance = DeviceOptionsDto.from_json(json)
# print the JSON string representation of the object
print(DeviceOptionsDto.to_json())

# convert the object into a dict
device_options_dto_dict = device_options_dto_instance.to_dict()
# create an instance of DeviceOptionsDto from a dict
device_options_dto_from_dict = DeviceOptionsDto.from_dict(device_options_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


