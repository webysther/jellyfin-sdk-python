# SystemInfo

Class SystemInfo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_address** | **str** | Gets or sets the local address. | [optional] 
**server_name** | **str** | Gets or sets the name of the server. | [optional] 
**version** | **str** | Gets or sets the server version. | [optional] 
**product_name** | **str** | Gets or sets the product name. This is the AssemblyProduct name. | [optional] 
**operating_system** | **str** | Gets or sets the operating system. | [optional] 
**id** | **str** | Gets or sets the id. | [optional] 
**startup_wizard_completed** | **bool** | Gets or sets a value indicating whether the startup wizard is completed. | [optional] 
**operating_system_display_name** | **str** | Gets or sets the display name of the operating system. | [optional] 
**package_name** | **str** | Gets or sets the package name. | [optional] 
**has_pending_restart** | **bool** | Gets or sets a value indicating whether this instance has pending restart. | [optional] 
**is_shutting_down** | **bool** |  | [optional] 
**supports_library_monitor** | **bool** | Gets or sets a value indicating whether [supports library monitor]. | [optional] 
**web_socket_port_number** | **int** | Gets or sets the web socket port number. | [optional] 
**completed_installations** | [**List[InstallationInfo]**](InstallationInfo.md) | Gets or sets the completed installations. | [optional] 
**can_self_restart** | **bool** | Gets or sets a value indicating whether this instance can self restart. | [optional] [default to True]
**can_launch_web_browser** | **bool** |  | [optional] [default to False]
**program_data_path** | **str** | Gets or sets the program data path. | [optional] 
**web_path** | **str** | Gets or sets the web UI resources path. | [optional] 
**items_by_name_path** | **str** | Gets or sets the items by name path. | [optional] 
**cache_path** | **str** | Gets or sets the cache path. | [optional] 
**log_path** | **str** | Gets or sets the log path. | [optional] 
**internal_metadata_path** | **str** | Gets or sets the internal metadata path. | [optional] 
**transcoding_temp_path** | **str** | Gets or sets the transcode path. | [optional] 
**cast_receiver_applications** | [**List[CastReceiverApplication]**](CastReceiverApplication.md) | Gets or sets the list of cast receiver applications. | [optional] 
**has_update_available** | **bool** | Gets or sets a value indicating whether this instance has update available. | [optional] [default to False]
**encoder_location** | **str** |  | [optional] [default to 'System']
**system_architecture** | **str** |  | [optional] [default to 'X64']

## Example

```python
from jellyfin.generated.api_10_10.models.system_info import SystemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SystemInfo from a JSON string
system_info_instance = SystemInfo.from_json(json)
# print the JSON string representation of the object
print(SystemInfo.to_json())

# convert the object into a dict
system_info_dict = system_info_instance.to_dict()
# create an instance of SystemInfo from a dict
system_info_from_dict = SystemInfo.from_dict(system_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


