# SearchHint

Class SearchHintResult.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | Gets or sets the item id. | [optional] 
**id** | **str** | Gets or sets the item id. | [optional] 
**name** | **str** | Gets or sets the name. | [optional] 
**matched_term** | **str** | Gets or sets the matched term. | [optional] 
**index_number** | **int** | Gets or sets the index number. | [optional] 
**production_year** | **int** | Gets or sets the production year. | [optional] 
**parent_index_number** | **int** | Gets or sets the parent index number. | [optional] 
**primary_image_tag** | **str** | Gets or sets the image tag. | [optional] 
**thumb_image_tag** | **str** | Gets or sets the thumb image tag. | [optional] 
**thumb_image_item_id** | **str** | Gets or sets the thumb image item identifier. | [optional] 
**backdrop_image_tag** | **str** | Gets or sets the backdrop image tag. | [optional] 
**backdrop_image_item_id** | **str** | Gets or sets the backdrop image item identifier. | [optional] 
**type** | [**BaseItemKind**](BaseItemKind.md) | The base item kind. | [optional] 
**is_folder** | **bool** | Gets or sets a value indicating whether this instance is folder. | [optional] 
**run_time_ticks** | **int** | Gets or sets the run time ticks. | [optional] 
**media_type** | [**MediaType**](MediaType.md) | Media types. | [optional] [default to MediaType.UNKNOWN]
**start_date** | **datetime** | Gets or sets the start date. | [optional] 
**end_date** | **datetime** | Gets or sets the end date. | [optional] 
**series** | **str** | Gets or sets the series. | [optional] 
**status** | **str** | Gets or sets the status. | [optional] 
**album** | **str** | Gets or sets the album. | [optional] 
**album_id** | **str** | Gets or sets the album id. | [optional] 
**album_artist** | **str** | Gets or sets the album artist. | [optional] 
**artists** | **List[str]** | Gets or sets the artists. | [optional] 
**song_count** | **int** | Gets or sets the song count. | [optional] 
**episode_count** | **int** | Gets or sets the episode count. | [optional] 
**channel_id** | **str** | Gets or sets the channel identifier. | [optional] 
**channel_name** | **str** | Gets or sets the name of the channel. | [optional] 
**primary_image_aspect_ratio** | **float** | Gets or sets the primary image aspect ratio. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.search_hint import SearchHint

# TODO update the JSON string below
json = "{}"
# create an instance of SearchHint from a JSON string
search_hint_instance = SearchHint.from_json(json)
# print the JSON string representation of the object
print(SearchHint.to_json())

# convert the object into a dict
search_hint_dict = search_hint_instance.to_dict()
# create an instance of SearchHint from a dict
search_hint_from_dict = SearchHint.from_dict(search_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


