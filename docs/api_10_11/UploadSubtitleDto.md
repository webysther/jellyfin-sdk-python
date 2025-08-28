# UploadSubtitleDto

Upload subtitles dto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | Gets or sets the subtitle language. | 
**format** | **str** | Gets or sets the subtitle format. | 
**is_forced** | **bool** | Gets or sets a value indicating whether the subtitle is forced. | 
**is_hearing_impaired** | **bool** | Gets or sets a value indicating whether the subtitle is for hearing impaired. | 
**data** | **str** | Gets or sets the subtitle data. | 

## Example

```python
from jellyfin.generated.api_10_11.models.upload_subtitle_dto import UploadSubtitleDto

# TODO update the JSON string below
json = "{}"
# create an instance of UploadSubtitleDto from a JSON string
upload_subtitle_dto_instance = UploadSubtitleDto.from_json(json)
# print the JSON string representation of the object
print(UploadSubtitleDto.to_json())

# convert the object into a dict
upload_subtitle_dto_dict = upload_subtitle_dto_instance.to_dict()
# create an instance of UploadSubtitleDto from a dict
upload_subtitle_dto_from_dict = UploadSubtitleDto.from_dict(upload_subtitle_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


