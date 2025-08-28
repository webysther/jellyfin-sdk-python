# QueryFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**genres** | [**List[NameGuidPair]**](NameGuidPair.md) |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.query_filters import QueryFilters

# TODO update the JSON string below
json = "{}"
# create an instance of QueryFilters from a JSON string
query_filters_instance = QueryFilters.from_json(json)
# print the JSON string representation of the object
print(QueryFilters.to_json())

# convert the object into a dict
query_filters_dict = query_filters_instance.to_dict()
# create an instance of QueryFilters from a dict
query_filters_from_dict = QueryFilters.from_dict(query_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


