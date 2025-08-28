# DeviceInfoDto

A DTO representing device information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets the name. | [optional] 
**custom_name** | **str** | Gets or sets the custom name. | [optional] 
**access_token** | **str** | Gets or sets the access token. | [optional] 
**id** | **str** | Gets or sets the identifier. | [optional] 
**last_user_name** | **str** | Gets or sets the last name of the user. | [optional] 
**app_name** | **str** | Gets or sets the name of the application. | [optional] 
**app_version** | **str** | Gets or sets the application version. | [optional] 
**last_user_id** | **str** | Gets or sets the last user identifier. | [optional] 
**date_last_activity** | **datetime** | Gets or sets the date last modified. | [optional] 
**capabilities** | [**ClientCapabilitiesDto**](ClientCapabilitiesDto.md) |  | [optional] 
**icon_url** | **str** | Gets or sets the icon URL. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.device_info_dto import DeviceInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceInfoDto from a JSON string
device_info_dto_instance = DeviceInfoDto.from_json(json)
# print the JSON string representation of the object
print(DeviceInfoDto.to_json())

# convert the object into a dict
device_info_dto_dict = device_info_dto_instance.to_dict()
# create an instance of DeviceInfoDto from a dict
device_info_dto_from_dict = DeviceInfoDto.from_dict(device_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


