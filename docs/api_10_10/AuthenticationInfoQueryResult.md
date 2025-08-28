# AuthenticationInfoQueryResult

Query result container.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AuthenticationInfo]**](AuthenticationInfo.md) | Gets or sets the items. | [optional] 
**total_record_count** | **int** | Gets or sets the total number of records available. | [optional] 
**start_index** | **int** | Gets or sets the index of the first record in Items. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.authentication_info_query_result import AuthenticationInfoQueryResult

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationInfoQueryResult from a JSON string
authentication_info_query_result_instance = AuthenticationInfoQueryResult.from_json(json)
# print the JSON string representation of the object
print(AuthenticationInfoQueryResult.to_json())

# convert the object into a dict
authentication_info_query_result_dict = authentication_info_query_result_instance.to_dict()
# create an instance of AuthenticationInfoQueryResult from a dict
authentication_info_query_result_from_dict = AuthenticationInfoQueryResult.from_dict(authentication_info_query_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


