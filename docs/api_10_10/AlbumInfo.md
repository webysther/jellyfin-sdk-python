# AlbumInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets the name. | [optional] 
**original_title** | **str** | Gets or sets the original title. | [optional] 
**path** | **str** | Gets or sets the path. | [optional] 
**metadata_language** | **str** | Gets or sets the metadata language. | [optional] 
**metadata_country_code** | **str** | Gets or sets the metadata country code. | [optional] 
**provider_ids** | **Dict[str, Optional[str]]** | Gets or sets the provider ids. | [optional] 
**year** | **int** | Gets or sets the year. | [optional] 
**index_number** | **int** |  | [optional] 
**parent_index_number** | **int** |  | [optional] 
**premiere_date** | **datetime** |  | [optional] 
**is_automated** | **bool** |  | [optional] 
**album_artists** | **List[str]** | Gets or sets the album artist. | [optional] 
**artist_provider_ids** | **Dict[str, Optional[str]]** | Gets or sets the artist provider ids. | [optional] 
**song_infos** | [**List[SongInfo]**](SongInfo.md) |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.album_info import AlbumInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumInfo from a JSON string
album_info_instance = AlbumInfo.from_json(json)
# print the JSON string representation of the object
print(AlbumInfo.to_json())

# convert the object into a dict
album_info_dict = album_info_instance.to_dict()
# create an instance of AlbumInfo from a dict
album_info_from_dict = AlbumInfo.from_dict(album_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


