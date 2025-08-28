# ChannelFeatures


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets the name. | [optional] 
**id** | **str** | Gets or sets the identifier. | [optional] 
**can_search** | **bool** | Gets or sets a value indicating whether this instance can search. | [optional] 
**media_types** | [**List[ChannelMediaType]**](ChannelMediaType.md) | Gets or sets the media types. | [optional] 
**content_types** | [**List[ChannelMediaContentType]**](ChannelMediaContentType.md) | Gets or sets the content types. | [optional] 
**max_page_size** | **int** | Gets or sets the maximum number of records the channel allows retrieving at a time. | [optional] 
**auto_refresh_levels** | **int** | Gets or sets the automatic refresh levels. | [optional] 
**default_sort_fields** | [**List[ChannelItemSortField]**](ChannelItemSortField.md) | Gets or sets the default sort orders. | [optional] 
**supports_sort_order_toggle** | **bool** | Gets or sets a value indicating whether a sort ascending/descending toggle is supported. | [optional] 
**supports_latest_media** | **bool** | Gets or sets a value indicating whether [supports latest media]. | [optional] 
**can_filter** | **bool** | Gets or sets a value indicating whether this instance can filter. | [optional] 
**supports_content_downloading** | **bool** | Gets or sets a value indicating whether [supports content downloading]. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.channel_features import ChannelFeatures

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelFeatures from a JSON string
channel_features_instance = ChannelFeatures.from_json(json)
# print the JSON string representation of the object
print(ChannelFeatures.to_json())

# convert the object into a dict
channel_features_dict = channel_features_instance.to_dict()
# create an instance of ChannelFeatures from a dict
channel_features_from_dict = ChannelFeatures.from_dict(channel_features_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


