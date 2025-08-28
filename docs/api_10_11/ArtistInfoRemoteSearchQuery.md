# ArtistInfoRemoteSearchQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_info** | [**ArtistInfo**](ArtistInfo.md) |  | [optional] 
**item_id** | **str** |  | [optional] 
**search_provider_name** | **str** | Gets or sets the provider name to search within if set. | [optional] 
**include_disabled_providers** | **bool** | Gets or sets a value indicating whether disabled providers should be included. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.artist_info_remote_search_query import ArtistInfoRemoteSearchQuery

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistInfoRemoteSearchQuery from a JSON string
artist_info_remote_search_query_instance = ArtistInfoRemoteSearchQuery.from_json(json)
# print the JSON string representation of the object
print(ArtistInfoRemoteSearchQuery.to_json())

# convert the object into a dict
artist_info_remote_search_query_dict = artist_info_remote_search_query_instance.to_dict()
# create an instance of ArtistInfoRemoteSearchQuery from a dict
artist_info_remote_search_query_from_dict = ArtistInfoRemoteSearchQuery.from_dict(artist_info_remote_search_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


