# RemoteSearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets the name. | [optional] 
**provider_ids** | **Dict[str, Optional[str]]** | Gets or sets the provider ids. | [optional] 
**production_year** | **int** | Gets or sets the year. | [optional] 
**index_number** | **int** |  | [optional] 
**index_number_end** | **int** |  | [optional] 
**parent_index_number** | **int** |  | [optional] 
**premiere_date** | **datetime** |  | [optional] 
**image_url** | **str** |  | [optional] 
**search_provider_name** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**album_artist** | [**RemoteSearchResult**](RemoteSearchResult.md) |  | [optional] 
**artists** | [**List[RemoteSearchResult]**](RemoteSearchResult.md) |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.remote_search_result import RemoteSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteSearchResult from a JSON string
remote_search_result_instance = RemoteSearchResult.from_json(json)
# print the JSON string representation of the object
print(RemoteSearchResult.to_json())

# convert the object into a dict
remote_search_result_dict = remote_search_result_instance.to_dict()
# create an instance of RemoteSearchResult from a dict
remote_search_result_from_dict = RemoteSearchResult.from_dict(remote_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


