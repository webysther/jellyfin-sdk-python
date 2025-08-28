# SeekRequestDto

Class SeekRequestDto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position_ticks** | **int** | Gets or sets the position ticks. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.seek_request_dto import SeekRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SeekRequestDto from a JSON string
seek_request_dto_instance = SeekRequestDto.from_json(json)
# print the JSON string representation of the object
print(SeekRequestDto.to_json())

# convert the object into a dict
seek_request_dto_dict = seek_request_dto_instance.to_dict()
# create an instance of SeekRequestDto from a dict
seek_request_dto_from_dict = SeekRequestDto.from_dict(seek_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


