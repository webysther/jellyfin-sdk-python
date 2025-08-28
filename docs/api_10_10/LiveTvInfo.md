# LiveTvInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**services** | [**List[LiveTvServiceInfo]**](LiveTvServiceInfo.md) | Gets or sets the services. | [optional] 
**is_enabled** | **bool** | Gets or sets a value indicating whether this instance is enabled. | [optional] 
**enabled_users** | **List[str]** | Gets or sets the enabled users. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.live_tv_info import LiveTvInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LiveTvInfo from a JSON string
live_tv_info_instance = LiveTvInfo.from_json(json)
# print the JSON string representation of the object
print(LiveTvInfo.to_json())

# convert the object into a dict
live_tv_info_dict = live_tv_info_instance.to_dict()
# create an instance of LiveTvInfo from a dict
live_tv_info_from_dict = LiveTvInfo.from_dict(live_tv_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


