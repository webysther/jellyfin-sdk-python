# BaseItemDtoQueryResult

Query result container.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[BaseItemDto]**](BaseItemDto.md) | Gets or sets the items. | [optional] 
**total_record_count** | **int** | Gets or sets the total number of records available. | [optional] 
**start_index** | **int** | Gets or sets the index of the first record in Items. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.base_item_dto_query_result import BaseItemDtoQueryResult

# TODO update the JSON string below
json = "{}"
# create an instance of BaseItemDtoQueryResult from a JSON string
base_item_dto_query_result_instance = BaseItemDtoQueryResult.from_json(json)
# print the JSON string representation of the object
print(BaseItemDtoQueryResult.to_json())

# convert the object into a dict
base_item_dto_query_result_dict = base_item_dto_query_result_instance.to_dict()
# create an instance of BaseItemDtoQueryResult from a dict
base_item_dto_query_result_from_dict = BaseItemDtoQueryResult.from_dict(base_item_dto_query_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


