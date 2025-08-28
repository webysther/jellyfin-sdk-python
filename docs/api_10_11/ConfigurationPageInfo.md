# ConfigurationPageInfo

The configuration page info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets the name. | [optional] 
**enable_in_main_menu** | **bool** | Gets or sets a value indicating whether the configurations page is enabled in the main menu. | [optional] 
**menu_section** | **str** | Gets or sets the menu section. | [optional] 
**menu_icon** | **str** | Gets or sets the menu icon. | [optional] 
**display_name** | **str** | Gets or sets the display name. | [optional] 
**plugin_id** | **str** | Gets or sets the plugin id. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.configuration_page_info import ConfigurationPageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationPageInfo from a JSON string
configuration_page_info_instance = ConfigurationPageInfo.from_json(json)
# print the JSON string representation of the object
print(ConfigurationPageInfo.to_json())

# convert the object into a dict
configuration_page_info_dict = configuration_page_info_instance.to_dict()
# create an instance of ConfigurationPageInfo from a dict
configuration_page_info_from_dict = ConfigurationPageInfo.from_dict(configuration_page_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


