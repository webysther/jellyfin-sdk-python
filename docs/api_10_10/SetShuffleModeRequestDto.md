# SetShuffleModeRequestDto

Class SetShuffleModeRequestDto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | [**GroupShuffleMode**](GroupShuffleMode.md) |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.set_shuffle_mode_request_dto import SetShuffleModeRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SetShuffleModeRequestDto from a JSON string
set_shuffle_mode_request_dto_instance = SetShuffleModeRequestDto.from_json(json)
# print the JSON string representation of the object
print(SetShuffleModeRequestDto.to_json())

# convert the object into a dict
set_shuffle_mode_request_dto_dict = set_shuffle_mode_request_dto_instance.to_dict()
# create an instance of SetShuffleModeRequestDto from a dict
set_shuffle_mode_request_dto_from_dict = SetShuffleModeRequestDto.from_dict(set_shuffle_mode_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


