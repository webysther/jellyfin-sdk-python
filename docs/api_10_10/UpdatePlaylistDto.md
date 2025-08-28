# UpdatePlaylistDto

Update existing playlist dto. Fields set to `null` will not be updated and keep their current values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets the name of the new playlist. | [optional] 
**ids** | **List[str]** | Gets or sets item ids of the playlist. | [optional] 
**users** | [**List[PlaylistUserPermissions]**](PlaylistUserPermissions.md) | Gets or sets the playlist users. | [optional] 
**is_public** | **bool** | Gets or sets a value indicating whether the playlist is public. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.update_playlist_dto import UpdatePlaylistDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePlaylistDto from a JSON string
update_playlist_dto_instance = UpdatePlaylistDto.from_json(json)
# print the JSON string representation of the object
print(UpdatePlaylistDto.to_json())

# convert the object into a dict
update_playlist_dto_dict = update_playlist_dto_instance.to_dict()
# create an instance of UpdatePlaylistDto from a dict
update_playlist_dto_from_dict = UpdatePlaylistDto.from_dict(update_playlist_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


