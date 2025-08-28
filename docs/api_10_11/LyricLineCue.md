# LyricLineCue

LyricLineCue model, holds information about the timing of words within a LyricLine.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **int** | Gets the start character index of the cue. | [optional] 
**end_position** | **int** | Gets the end character index of the cue. | [optional] 
**start** | **int** | Gets the timestamp the lyric is synced to in ticks. | [optional] 
**end** | **int** | Gets the end timestamp the lyric is synced to in ticks. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.lyric_line_cue import LyricLineCue

# TODO update the JSON string below
json = "{}"
# create an instance of LyricLineCue from a JSON string
lyric_line_cue_instance = LyricLineCue.from_json(json)
# print the JSON string representation of the object
print(LyricLineCue.to_json())

# convert the object into a dict
lyric_line_cue_dict = lyric_line_cue_instance.to_dict()
# create an instance of LyricLineCue from a dict
lyric_line_cue_from_dict = LyricLineCue.from_dict(lyric_line_cue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


