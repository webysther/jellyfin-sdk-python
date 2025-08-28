# SearchHintResult

Class SearchHintResult.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_hints** | [**List[SearchHint]**](SearchHint.md) | Gets the search hints. | [optional] 
**total_record_count** | **int** | Gets the total record count. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.search_hint_result import SearchHintResult

# TODO update the JSON string below
json = "{}"
# create an instance of SearchHintResult from a JSON string
search_hint_result_instance = SearchHintResult.from_json(json)
# print the JSON string representation of the object
print(SearchHintResult.to_json())

# convert the object into a dict
search_hint_result_dict = search_hint_result_instance.to_dict()
# create an instance of SearchHintResult from a dict
search_hint_result_from_dict = SearchHintResult.from_dict(search_hint_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


