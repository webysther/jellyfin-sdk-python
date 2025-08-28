# LyricLine

Lyric model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Gets the text of this lyric line. | [optional] 
**start** | **int** | Gets the start time in ticks. | [optional] 
**cues** | [**List[LyricLineCue]**](LyricLineCue.md) | Gets the time-aligned cues for the song&#39;s lyrics. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.lyric_line import LyricLine

# TODO update the JSON string below
json = "{}"
# create an instance of LyricLine from a JSON string
lyric_line_instance = LyricLine.from_json(json)
# print the JSON string representation of the object
print(LyricLine.to_json())

# convert the object into a dict
lyric_line_dict = lyric_line_instance.to_dict()
# create an instance of LyricLine from a dict
lyric_line_from_dict = LyricLine.from_dict(lyric_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


