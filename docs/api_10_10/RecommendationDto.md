# RecommendationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[BaseItemDto]**](BaseItemDto.md) |  | [optional] 
**recommendation_type** | [**RecommendationType**](RecommendationType.md) |  | [optional] 
**baseline_item_name** | **str** |  | [optional] 
**category_id** | **str** |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.recommendation_dto import RecommendationDto

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendationDto from a JSON string
recommendation_dto_instance = RecommendationDto.from_json(json)
# print the JSON string representation of the object
print(RecommendationDto.to_json())

# convert the object into a dict
recommendation_dto_dict = recommendation_dto_instance.to_dict()
# create an instance of RecommendationDto from a dict
recommendation_dto_from_dict = RecommendationDto.from_dict(recommendation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


