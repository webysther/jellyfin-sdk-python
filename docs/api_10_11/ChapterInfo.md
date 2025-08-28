# ChapterInfo

Class ChapterInfo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_position_ticks** | **int** | Gets or sets the start position ticks. | [optional] 
**name** | **str** | Gets or sets the name. | [optional] 
**image_path** | **str** | Gets or sets the image path. | [optional] 
**image_date_modified** | **datetime** |  | [optional] 
**image_tag** | **str** |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.chapter_info import ChapterInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ChapterInfo from a JSON string
chapter_info_instance = ChapterInfo.from_json(json)
# print the JSON string representation of the object
print(ChapterInfo.to_json())

# convert the object into a dict
chapter_info_dict = chapter_info_instance.to_dict()
# create an instance of ChapterInfo from a dict
chapter_info_from_dict = ChapterInfo.from_dict(chapter_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


