# PlayRequest

Class PlayRequest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_ids** | **List[str]** | Gets or sets the item ids. | [optional] 
**start_position_ticks** | **int** | Gets or sets the start position ticks that the first item should be played at. | [optional] 
**play_command** | [**PlayCommand**](PlayCommand.md) | Gets or sets the play command. | [optional] 
**controlling_user_id** | **str** | Gets or sets the controlling user identifier. | [optional] 
**subtitle_stream_index** | **int** |  | [optional] 
**audio_stream_index** | **int** |  | [optional] 
**media_source_id** | **str** |  | [optional] 
**start_index** | **int** |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.play_request import PlayRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlayRequest from a JSON string
play_request_instance = PlayRequest.from_json(json)
# print the JSON string representation of the object
print(PlayRequest.to_json())

# convert the object into a dict
play_request_dict = play_request_instance.to_dict()
# create an instance of PlayRequest from a dict
play_request_from_dict = PlayRequest.from_dict(play_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


