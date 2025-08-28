# PlaylistUserPermissions

Class to hold data on user permissions for playlists.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | Gets or sets the user id. | [optional] 
**can_edit** | **bool** | Gets or sets a value indicating whether the user has edit permissions. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.playlist_user_permissions import PlaylistUserPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistUserPermissions from a JSON string
playlist_user_permissions_instance = PlaylistUserPermissions.from_json(json)
# print the JSON string representation of the object
print(PlaylistUserPermissions.to_json())

# convert the object into a dict
playlist_user_permissions_dict = playlist_user_permissions_instance.to_dict()
# create an instance of PlaylistUserPermissions from a dict
playlist_user_permissions_from_dict = PlaylistUserPermissions.from_dict(playlist_user_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


