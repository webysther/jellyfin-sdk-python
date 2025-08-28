# PlaylistDto

DTO for playlists.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**open_access** | **bool** | Gets or sets a value indicating whether the playlist is publicly readable. | [optional] 
**shares** | [**List[PlaylistUserPermissions]**](PlaylistUserPermissions.md) | Gets or sets the share permissions. | [optional] 
**item_ids** | **List[str]** | Gets or sets the item ids. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.playlist_dto import PlaylistDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistDto from a JSON string
playlist_dto_instance = PlaylistDto.from_json(json)
# print the JSON string representation of the object
print(PlaylistDto.to_json())

# convert the object into a dict
playlist_dto_dict = playlist_dto_instance.to_dict()
# create an instance of PlaylistDto from a dict
playlist_dto_from_dict = PlaylistDto.from_dict(playlist_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


