# NextItemRequestDto

Class NextItemRequestDto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**playlist_item_id** | **str** | Gets or sets the playing item identifier. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.next_item_request_dto import NextItemRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of NextItemRequestDto from a JSON string
next_item_request_dto_instance = NextItemRequestDto.from_json(json)
# print the JSON string representation of the object
print(NextItemRequestDto.to_json())

# convert the object into a dict
next_item_request_dto_dict = next_item_request_dto_instance.to_dict()
# create an instance of NextItemRequestDto from a dict
next_item_request_dto_from_dict = NextItemRequestDto.from_dict(next_item_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


