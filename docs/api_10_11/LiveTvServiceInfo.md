# LiveTvServiceInfo

Class ServiceInfo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets the name. | [optional] 
**home_page_url** | **str** | Gets or sets the home page URL. | [optional] 
**status** | [**LiveTvServiceStatus**](LiveTvServiceStatus.md) | Gets or sets the status. | [optional] 
**status_message** | **str** | Gets or sets the status message. | [optional] 
**version** | **str** | Gets or sets the version. | [optional] 
**has_update_available** | **bool** | Gets or sets a value indicating whether this instance has update available. | [optional] 
**is_visible** | **bool** | Gets or sets a value indicating whether this instance is visible. | [optional] 
**tuners** | **List[str]** |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.live_tv_service_info import LiveTvServiceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LiveTvServiceInfo from a JSON string
live_tv_service_info_instance = LiveTvServiceInfo.from_json(json)
# print the JSON string representation of the object
print(LiveTvServiceInfo.to_json())

# convert the object into a dict
live_tv_service_info_dict = live_tv_service_info_instance.to_dict()
# create an instance of LiveTvServiceInfo from a dict
live_tv_service_info_from_dict = LiveTvServiceInfo.from_dict(live_tv_service_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


