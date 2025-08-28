# SetRepeatModeRequestDto

Class SetRepeatModeRequestDto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | [**GroupRepeatMode**](GroupRepeatMode.md) |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.set_repeat_mode_request_dto import SetRepeatModeRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SetRepeatModeRequestDto from a JSON string
set_repeat_mode_request_dto_instance = SetRepeatModeRequestDto.from_json(json)
# print the JSON string representation of the object
print(SetRepeatModeRequestDto.to_json())

# convert the object into a dict
set_repeat_mode_request_dto_dict = set_repeat_mode_request_dto_instance.to_dict()
# create an instance of SetRepeatModeRequestDto from a dict
set_repeat_mode_request_dto_from_dict = SetRepeatModeRequestDto.from_dict(set_repeat_mode_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


