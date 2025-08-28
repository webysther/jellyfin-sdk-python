# BoxSetInfoRemoteSearchQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_info** | [**BoxSetInfo**](BoxSetInfo.md) |  | [optional] 
**item_id** | **str** |  | [optional] 
**search_provider_name** | **str** | Gets or sets the provider name to search within if set. | [optional] 
**include_disabled_providers** | **bool** | Gets or sets a value indicating whether disabled providers should be included. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.box_set_info_remote_search_query import BoxSetInfoRemoteSearchQuery

# TODO update the JSON string below
json = "{}"
# create an instance of BoxSetInfoRemoteSearchQuery from a JSON string
box_set_info_remote_search_query_instance = BoxSetInfoRemoteSearchQuery.from_json(json)
# print the JSON string representation of the object
print(BoxSetInfoRemoteSearchQuery.to_json())

# convert the object into a dict
box_set_info_remote_search_query_dict = box_set_info_remote_search_query_instance.to_dict()
# create an instance of BoxSetInfoRemoteSearchQuery from a dict
box_set_info_remote_search_query_from_dict = BoxSetInfoRemoteSearchQuery.from_dict(box_set_info_remote_search_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


