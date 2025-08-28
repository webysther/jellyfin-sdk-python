# AllThemeMediaResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**theme_videos_result** | [**ThemeMediaResult**](ThemeMediaResult.md) |  | [optional] 
**theme_songs_result** | [**ThemeMediaResult**](ThemeMediaResult.md) |  | [optional] 
**soundtrack_songs_result** | [**ThemeMediaResult**](ThemeMediaResult.md) |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.all_theme_media_result import AllThemeMediaResult

# TODO update the JSON string below
json = "{}"
# create an instance of AllThemeMediaResult from a JSON string
all_theme_media_result_instance = AllThemeMediaResult.from_json(json)
# print the JSON string representation of the object
print(AllThemeMediaResult.to_json())

# convert the object into a dict
all_theme_media_result_dict = all_theme_media_result_instance.to_dict()
# create an instance of AllThemeMediaResult from a dict
all_theme_media_result_from_dict = AllThemeMediaResult.from_dict(all_theme_media_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


