# LyricMetadata

LyricMetadata model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artist** | **str** | Gets or sets the song artist. | [optional] 
**album** | **str** | Gets or sets the album this song is on. | [optional] 
**title** | **str** | Gets or sets the title of the song. | [optional] 
**author** | **str** | Gets or sets the author of the lyric data. | [optional] 
**length** | **int** | Gets or sets the length of the song in ticks. | [optional] 
**by** | **str** | Gets or sets who the LRC file was created by. | [optional] 
**offset** | **int** | Gets or sets the lyric offset compared to audio in ticks. | [optional] 
**creator** | **str** | Gets or sets the software used to create the LRC file. | [optional] 
**version** | **str** | Gets or sets the version of the creator used. | [optional] 
**is_synced** | **bool** | Gets or sets a value indicating whether this lyric is synced. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.lyric_metadata import LyricMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of LyricMetadata from a JSON string
lyric_metadata_instance = LyricMetadata.from_json(json)
# print the JSON string representation of the object
print(LyricMetadata.to_json())

# convert the object into a dict
lyric_metadata_dict = lyric_metadata_instance.to_dict()
# create an instance of LyricMetadata from a dict
lyric_metadata_from_dict = LyricMetadata.from_dict(lyric_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


