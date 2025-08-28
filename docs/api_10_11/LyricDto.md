# LyricDto

LyricResponse model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**LyricMetadata**](LyricMetadata.md) | Gets or sets Metadata for the lyrics. | [optional] 
**lyrics** | [**List[LyricLine]**](LyricLine.md) | Gets or sets a collection of individual lyric lines. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.lyric_dto import LyricDto

# TODO update the JSON string below
json = "{}"
# create an instance of LyricDto from a JSON string
lyric_dto_instance = LyricDto.from_json(json)
# print the JSON string representation of the object
print(LyricDto.to_json())

# convert the object into a dict
lyric_dto_dict = lyric_dto_instance.to_dict()
# create an instance of LyricDto from a dict
lyric_dto_from_dict = LyricDto.from_dict(lyric_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


