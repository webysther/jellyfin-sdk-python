# UpdatePlaylistUserDto

Update existing playlist user dto. Fields set to `null` will not be updated and keep their current values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_edit** | **bool** | Gets or sets a value indicating whether the user can edit the playlist. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.update_playlist_user_dto import UpdatePlaylistUserDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePlaylistUserDto from a JSON string
update_playlist_user_dto_instance = UpdatePlaylistUserDto.from_json(json)
# print the JSON string representation of the object
print(UpdatePlaylistUserDto.to_json())

# convert the object into a dict
update_playlist_user_dto_dict = update_playlist_user_dto_instance.to_dict()
# create an instance of UpdatePlaylistUserDto from a dict
update_playlist_user_dto_from_dict = UpdatePlaylistUserDto.from_dict(update_playlist_user_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


