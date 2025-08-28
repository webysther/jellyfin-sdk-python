# PlayRequestDto

Class PlayRequestDto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**playing_queue** | **List[str]** | Gets or sets the playing queue. | [optional] 
**playing_item_position** | **int** | Gets or sets the position of the playing item in the queue. | [optional] 
**start_position_ticks** | **int** | Gets or sets the start position ticks. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.play_request_dto import PlayRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlayRequestDto from a JSON string
play_request_dto_instance = PlayRequestDto.from_json(json)
# print the JSON string representation of the object
print(PlayRequestDto.to_json())

# convert the object into a dict
play_request_dto_dict = play_request_dto_instance.to_dict()
# create an instance of PlayRequestDto from a dict
play_request_dto_from_dict = PlayRequestDto.from_dict(play_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


