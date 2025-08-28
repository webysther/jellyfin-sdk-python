# PlaylistCreationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.playlist_creation_result import PlaylistCreationResult

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistCreationResult from a JSON string
playlist_creation_result_instance = PlaylistCreationResult.from_json(json)
# print the JSON string representation of the object
print(PlaylistCreationResult.to_json())

# convert the object into a dict
playlist_creation_result_dict = playlist_creation_result_instance.to_dict()
# create an instance of PlaylistCreationResult from a dict
playlist_creation_result_from_dict = PlaylistCreationResult.from_dict(playlist_creation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


