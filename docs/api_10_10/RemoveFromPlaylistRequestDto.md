# RemoveFromPlaylistRequestDto

Class RemoveFromPlaylistRequestDto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**playlist_item_ids** | **List[str]** | Gets or sets the playlist identifiers of the items. Ignored when clearing the playlist. | [optional] 
**clear_playlist** | **bool** | Gets or sets a value indicating whether the entire playlist should be cleared. | [optional] 
**clear_playing_item** | **bool** | Gets or sets a value indicating whether the playing item should be removed as well. Used only when clearing the playlist. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.remove_from_playlist_request_dto import RemoveFromPlaylistRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveFromPlaylistRequestDto from a JSON string
remove_from_playlist_request_dto_instance = RemoveFromPlaylistRequestDto.from_json(json)
# print the JSON string representation of the object
print(RemoveFromPlaylistRequestDto.to_json())

# convert the object into a dict
remove_from_playlist_request_dto_dict = remove_from_playlist_request_dto_instance.to_dict()
# create an instance of RemoveFromPlaylistRequestDto from a dict
remove_from_playlist_request_dto_from_dict = RemoveFromPlaylistRequestDto.from_dict(remove_from_playlist_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


