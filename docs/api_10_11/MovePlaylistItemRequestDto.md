# MovePlaylistItemRequestDto

Class MovePlaylistItemRequestDto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**playlist_item_id** | **str** | Gets or sets the playlist identifier of the item. | [optional] 
**new_index** | **int** | Gets or sets the new position. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.move_playlist_item_request_dto import MovePlaylistItemRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of MovePlaylistItemRequestDto from a JSON string
move_playlist_item_request_dto_instance = MovePlaylistItemRequestDto.from_json(json)
# print the JSON string representation of the object
print(MovePlaylistItemRequestDto.to_json())

# convert the object into a dict
move_playlist_item_request_dto_dict = move_playlist_item_request_dto_instance.to_dict()
# create an instance of MovePlaylistItemRequestDto from a dict
move_playlist_item_request_dto_from_dict = MovePlaylistItemRequestDto.from_dict(move_playlist_item_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


