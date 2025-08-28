# ReadyRequestDto

Class ReadyRequest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**when** | **datetime** | Gets or sets when the request has been made by the client. | [optional] 
**position_ticks** | **int** | Gets or sets the position ticks. | [optional] 
**is_playing** | **bool** | Gets or sets a value indicating whether the client playback is unpaused. | [optional] 
**playlist_item_id** | **str** | Gets or sets the playlist item identifier of the playing item. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.ready_request_dto import ReadyRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ReadyRequestDto from a JSON string
ready_request_dto_instance = ReadyRequestDto.from_json(json)
# print the JSON string representation of the object
print(ReadyRequestDto.to_json())

# convert the object into a dict
ready_request_dto_dict = ready_request_dto_instance.to_dict()
# create an instance of ReadyRequestDto from a dict
ready_request_dto_from_dict = ReadyRequestDto.from_dict(ready_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


