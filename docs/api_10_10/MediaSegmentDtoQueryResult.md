# MediaSegmentDtoQueryResult

Query result container.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[MediaSegmentDto]**](MediaSegmentDto.md) | Gets or sets the items. | [optional] 
**total_record_count** | **int** | Gets or sets the total number of records available. | [optional] 
**start_index** | **int** | Gets or sets the index of the first record in Items. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.media_segment_dto_query_result import MediaSegmentDtoQueryResult

# TODO update the JSON string below
json = "{}"
# create an instance of MediaSegmentDtoQueryResult from a JSON string
media_segment_dto_query_result_instance = MediaSegmentDtoQueryResult.from_json(json)
# print the JSON string representation of the object
print(MediaSegmentDtoQueryResult.to_json())

# convert the object into a dict
media_segment_dto_query_result_dict = media_segment_dto_query_result_instance.to_dict()
# create an instance of MediaSegmentDtoQueryResult from a dict
media_segment_dto_query_result_from_dict = MediaSegmentDtoQueryResult.from_dict(media_segment_dto_query_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


