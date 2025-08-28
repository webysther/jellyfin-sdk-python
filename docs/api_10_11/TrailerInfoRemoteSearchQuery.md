# TrailerInfoRemoteSearchQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_info** | [**TrailerInfo**](TrailerInfo.md) |  | [optional] 
**item_id** | **str** |  | [optional] 
**search_provider_name** | **str** | Gets or sets the provider name to search within if set. | [optional] 
**include_disabled_providers** | **bool** | Gets or sets a value indicating whether disabled providers should be included. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.trailer_info_remote_search_query import TrailerInfoRemoteSearchQuery

# TODO update the JSON string below
json = "{}"
# create an instance of TrailerInfoRemoteSearchQuery from a JSON string
trailer_info_remote_search_query_instance = TrailerInfoRemoteSearchQuery.from_json(json)
# print the JSON string representation of the object
print(TrailerInfoRemoteSearchQuery.to_json())

# convert the object into a dict
trailer_info_remote_search_query_dict = trailer_info_remote_search_query_instance.to_dict()
# create an instance of TrailerInfoRemoteSearchQuery from a dict
trailer_info_remote_search_query_from_dict = TrailerInfoRemoteSearchQuery.from_dict(trailer_info_remote_search_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


