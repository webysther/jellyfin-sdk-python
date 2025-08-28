# GetProgramsDto

Get programs dto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_ids** | **List[str]** | Gets or sets the channels to return guide information for. | [optional] 
**user_id** | **str** | Gets or sets optional. Filter by user id. | [optional] 
**min_start_date** | **datetime** | Gets or sets the minimum premiere start date. | [optional] 
**has_aired** | **bool** | Gets or sets filter by programs that have completed airing, or not. | [optional] 
**is_airing** | **bool** | Gets or sets filter by programs that are currently airing, or not. | [optional] 
**max_start_date** | **datetime** | Gets or sets the maximum premiere start date. | [optional] 
**min_end_date** | **datetime** | Gets or sets the minimum premiere end date. | [optional] 
**max_end_date** | **datetime** | Gets or sets the maximum premiere end date. | [optional] 
**is_movie** | **bool** | Gets or sets filter for movies. | [optional] 
**is_series** | **bool** | Gets or sets filter for series. | [optional] 
**is_news** | **bool** | Gets or sets filter for news. | [optional] 
**is_kids** | **bool** | Gets or sets filter for kids. | [optional] 
**is_sports** | **bool** | Gets or sets filter for sports. | [optional] 
**start_index** | **int** | Gets or sets the record index to start at. All items with a lower index will be dropped from the results. | [optional] 
**limit** | **int** | Gets or sets the maximum number of records to return. | [optional] 
**sort_by** | [**List[ItemSortBy]**](ItemSortBy.md) | Gets or sets specify one or more sort orders, comma delimited. Options: Name, StartDate. | [optional] 
**sort_order** | [**List[SortOrder]**](SortOrder.md) | Gets or sets sort order. | [optional] 
**genres** | **List[str]** | Gets or sets the genres to return guide information for. | [optional] 
**genre_ids** | **List[str]** | Gets or sets the genre ids to return guide information for. | [optional] 
**enable_images** | **bool** | Gets or sets include image information in output. | [optional] 
**enable_total_record_count** | **bool** | Gets or sets a value indicating whether retrieve total record count. | [optional] [default to True]
**image_type_limit** | **int** | Gets or sets the max number of images to return, per image type. | [optional] 
**enable_image_types** | [**List[ImageType]**](ImageType.md) | Gets or sets the image types to include in the output. | [optional] 
**enable_user_data** | **bool** | Gets or sets include user data. | [optional] 
**series_timer_id** | **str** | Gets or sets filter by series timer id. | [optional] 
**library_series_id** | **str** | Gets or sets filter by library series id. | [optional] 
**fields** | [**List[ItemFields]**](ItemFields.md) | Gets or sets specify additional fields of information to return in the output. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.get_programs_dto import GetProgramsDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetProgramsDto from a JSON string
get_programs_dto_instance = GetProgramsDto.from_json(json)
# print the JSON string representation of the object
print(GetProgramsDto.to_json())

# convert the object into a dict
get_programs_dto_dict = get_programs_dto_instance.to_dict()
# create an instance of GetProgramsDto from a dict
get_programs_dto_from_dict = GetProgramsDto.from_dict(get_programs_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


