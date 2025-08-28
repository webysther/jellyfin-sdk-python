# CreatePlaylistDto

Create new playlist dto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets the name of the new playlist. | [optional] 
**ids** | **List[str]** | Gets or sets item ids to add to the playlist. | [optional] 
**user_id** | **str** | Gets or sets the user id. | [optional] 
**media_type** | [**MediaType**](MediaType.md) | Gets or sets the media type. | [optional] 
**users** | [**List[PlaylistUserPermissions]**](PlaylistUserPermissions.md) | Gets or sets the playlist users. | [optional] 
**is_public** | **bool** | Gets or sets a value indicating whether the playlist is public. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.create_playlist_dto import CreatePlaylistDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePlaylistDto from a JSON string
create_playlist_dto_instance = CreatePlaylistDto.from_json(json)
# print the JSON string representation of the object
print(CreatePlaylistDto.to_json())

# convert the object into a dict
create_playlist_dto_dict = create_playlist_dto_instance.to_dict()
# create an instance of CreatePlaylistDto from a dict
create_playlist_dto_from_dict = CreatePlaylistDto.from_dict(create_playlist_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


