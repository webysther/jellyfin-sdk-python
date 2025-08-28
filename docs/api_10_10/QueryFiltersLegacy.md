# QueryFiltersLegacy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**genres** | **List[str]** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**official_ratings** | **List[str]** |  | [optional] 
**years** | **List[int]** |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.query_filters_legacy import QueryFiltersLegacy

# TODO update the JSON string below
json = "{}"
# create an instance of QueryFiltersLegacy from a JSON string
query_filters_legacy_instance = QueryFiltersLegacy.from_json(json)
# print the JSON string representation of the object
print(QueryFiltersLegacy.to_json())

# convert the object into a dict
query_filters_legacy_dict = query_filters_legacy_instance.to_dict()
# create an instance of QueryFiltersLegacy from a dict
query_filters_legacy_from_dict = QueryFiltersLegacy.from_dict(query_filters_legacy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


