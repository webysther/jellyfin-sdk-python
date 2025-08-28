# SetPlaylistItemRequestDto

Class SetPlaylistItemRequestDto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**playlist_item_id** | **str** | Gets or sets the playlist identifier of the playing item. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.set_playlist_item_request_dto import SetPlaylistItemRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SetPlaylistItemRequestDto from a JSON string
set_playlist_item_request_dto_instance = SetPlaylistItemRequestDto.from_json(json)
# print the JSON string representation of the object
print(SetPlaylistItemRequestDto.to_json())

# convert the object into a dict
set_playlist_item_request_dto_dict = set_playlist_item_request_dto_instance.to_dict()
# create an instance of SetPlaylistItemRequestDto from a dict
set_playlist_item_request_dto_from_dict = SetPlaylistItemRequestDto.from_dict(set_playlist_item_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


