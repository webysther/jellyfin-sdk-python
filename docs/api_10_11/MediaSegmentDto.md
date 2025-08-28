# MediaSegmentDto

Api model for MediaSegment's.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Gets or sets the id of the media segment. | [optional] 
**item_id** | **str** | Gets or sets the id of the associated item. | [optional] 
**type** | [**MediaSegmentType**](MediaSegmentType.md) | Gets or sets the type of content this segment defines. | [optional] [default to MediaSegmentType.UNKNOWN]
**start_ticks** | **int** | Gets or sets the start of the segment. | [optional] 
**end_ticks** | **int** | Gets or sets the end of the segment. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.media_segment_dto import MediaSegmentDto

# TODO update the JSON string below
json = "{}"
# create an instance of MediaSegmentDto from a JSON string
media_segment_dto_instance = MediaSegmentDto.from_json(json)
# print the JSON string representation of the object
print(MediaSegmentDto.to_json())

# convert the object into a dict
media_segment_dto_dict = media_segment_dto_instance.to_dict()
# create an instance of MediaSegmentDto from a dict
media_segment_dto_from_dict = MediaSegmentDto.from_dict(media_segment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


