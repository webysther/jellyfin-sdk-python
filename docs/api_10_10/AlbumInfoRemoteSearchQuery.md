# AlbumInfoRemoteSearchQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_info** | [**AlbumInfo**](AlbumInfo.md) |  | [optional] 
**item_id** | **str** |  | [optional] 
**search_provider_name** | **str** | Gets or sets the provider name to search within if set. | [optional] 
**include_disabled_providers** | **bool** | Gets or sets a value indicating whether disabled providers should be included. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.album_info_remote_search_query import AlbumInfoRemoteSearchQuery

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumInfoRemoteSearchQuery from a JSON string
album_info_remote_search_query_instance = AlbumInfoRemoteSearchQuery.from_json(json)
# print the JSON string representation of the object
print(AlbumInfoRemoteSearchQuery.to_json())

# convert the object into a dict
album_info_remote_search_query_dict = album_info_remote_search_query_instance.to_dict()
# create an instance of AlbumInfoRemoteSearchQuery from a dict
album_info_remote_search_query_from_dict = AlbumInfoRemoteSearchQuery.from_dict(album_info_remote_search_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


