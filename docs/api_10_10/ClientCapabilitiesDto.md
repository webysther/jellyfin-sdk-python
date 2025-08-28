# ClientCapabilitiesDto

Client capabilities dto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**playable_media_types** | [**List[MediaType]**](MediaType.md) | Gets or sets the list of playable media types. | [optional] 
**supported_commands** | [**List[GeneralCommandType]**](GeneralCommandType.md) | Gets or sets the list of supported commands. | [optional] 
**supports_media_control** | **bool** | Gets or sets a value indicating whether session supports media control. | [optional] 
**supports_persistent_identifier** | **bool** | Gets or sets a value indicating whether session supports a persistent identifier. | [optional] 
**device_profile** | [**DeviceProfile**](DeviceProfile.md) |  | [optional] 
**app_store_url** | **str** | Gets or sets the app store url. | [optional] 
**icon_url** | **str** | Gets or sets the icon url. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.client_capabilities_dto import ClientCapabilitiesDto

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCapabilitiesDto from a JSON string
client_capabilities_dto_instance = ClientCapabilitiesDto.from_json(json)
# print the JSON string representation of the object
print(ClientCapabilitiesDto.to_json())

# convert the object into a dict
client_capabilities_dto_dict = client_capabilities_dto_instance.to_dict()
# create an instance of ClientCapabilitiesDto from a dict
client_capabilities_dto_from_dict = ClientCapabilitiesDto.from_dict(client_capabilities_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


