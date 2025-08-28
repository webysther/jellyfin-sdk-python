# BookInfoRemoteSearchQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_info** | [**BookInfo**](BookInfo.md) |  | [optional] 
**item_id** | **str** |  | [optional] 
**search_provider_name** | **str** | Gets or sets the provider name to search within if set. | [optional] 
**include_disabled_providers** | **bool** | Gets or sets a value indicating whether disabled providers should be included. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.book_info_remote_search_query import BookInfoRemoteSearchQuery

# TODO update the JSON string below
json = "{}"
# create an instance of BookInfoRemoteSearchQuery from a JSON string
book_info_remote_search_query_instance = BookInfoRemoteSearchQuery.from_json(json)
# print the JSON string representation of the object
print(BookInfoRemoteSearchQuery.to_json())

# convert the object into a dict
book_info_remote_search_query_dict = book_info_remote_search_query_instance.to_dict()
# create an instance of BookInfoRemoteSearchQuery from a dict
book_info_remote_search_query_from_dict = BookInfoRemoteSearchQuery.from_dict(book_info_remote_search_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


