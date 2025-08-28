# PreviousItemRequestDto

Class PreviousItemRequestDto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**playlist_item_id** | **str** | Gets or sets the playing item identifier. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.previous_item_request_dto import PreviousItemRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of PreviousItemRequestDto from a JSON string
previous_item_request_dto_instance = PreviousItemRequestDto.from_json(json)
# print the JSON string representation of the object
print(PreviousItemRequestDto.to_json())

# convert the object into a dict
previous_item_request_dto_dict = previous_item_request_dto_instance.to_dict()
# create an instance of PreviousItemRequestDto from a dict
previous_item_request_dto_from_dict = PreviousItemRequestDto.from_dict(previous_item_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


