# SeriesTimerInfoDto

Class SeriesTimerInfoDto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Gets or sets the Id of the recording. | [optional] 
**type** | **str** |  | [optional] 
**server_id** | **str** | Gets or sets the server identifier. | [optional] 
**external_id** | **str** | Gets or sets the external identifier. | [optional] 
**channel_id** | **str** | Gets or sets the channel id of the recording. | [optional] 
**external_channel_id** | **str** | Gets or sets the external channel identifier. | [optional] 
**channel_name** | **str** | Gets or sets the channel name of the recording. | [optional] 
**channel_primary_image_tag** | **str** |  | [optional] 
**program_id** | **str** | Gets or sets the program identifier. | [optional] 
**external_program_id** | **str** | Gets or sets the external program identifier. | [optional] 
**name** | **str** | Gets or sets the name of the recording. | [optional] 
**overview** | **str** | Gets or sets the description of the recording. | [optional] 
**start_date** | **datetime** | Gets or sets the start date of the recording, in UTC. | [optional] 
**end_date** | **datetime** | Gets or sets the end date of the recording, in UTC. | [optional] 
**service_name** | **str** | Gets or sets the name of the service. | [optional] 
**priority** | **int** | Gets or sets the priority. | [optional] 
**pre_padding_seconds** | **int** | Gets or sets the pre padding seconds. | [optional] 
**post_padding_seconds** | **int** | Gets or sets the post padding seconds. | [optional] 
**is_pre_padding_required** | **bool** | Gets or sets a value indicating whether this instance is pre padding required. | [optional] 
**parent_backdrop_item_id** | **str** | Gets or sets the Id of the Parent that has a backdrop if the item does not have one. | [optional] 
**parent_backdrop_image_tags** | **List[str]** | Gets or sets the parent backdrop image tags. | [optional] 
**is_post_padding_required** | **bool** | Gets or sets a value indicating whether this instance is post padding required. | [optional] 
**keep_until** | [**KeepUntil**](KeepUntil.md) |  | [optional] 
**record_any_time** | **bool** | Gets or sets a value indicating whether [record any time]. | [optional] 
**skip_episodes_in_library** | **bool** |  | [optional] 
**record_any_channel** | **bool** | Gets or sets a value indicating whether [record any channel]. | [optional] 
**keep_up_to** | **int** |  | [optional] 
**record_new_only** | **bool** | Gets or sets a value indicating whether [record new only]. | [optional] 
**days** | [**List[DayOfWeek]**](DayOfWeek.md) | Gets or sets the days. | [optional] 
**day_pattern** | [**DayPattern**](DayPattern.md) | Gets or sets the day pattern. | [optional] 
**image_tags** | **Dict[str, str]** | Gets or sets the image tags. | [optional] 
**parent_thumb_item_id** | **str** | Gets or sets the parent thumb item id. | [optional] 
**parent_thumb_image_tag** | **str** | Gets or sets the parent thumb image tag. | [optional] 
**parent_primary_image_item_id** | **str** | Gets or sets the parent primary image item identifier. | [optional] 
**parent_primary_image_tag** | **str** | Gets or sets the parent primary image tag. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.series_timer_info_dto import SeriesTimerInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesTimerInfoDto from a JSON string
series_timer_info_dto_instance = SeriesTimerInfoDto.from_json(json)
# print the JSON string representation of the object
print(SeriesTimerInfoDto.to_json())

# convert the object into a dict
series_timer_info_dto_dict = series_timer_info_dto_instance.to_dict()
# create an instance of SeriesTimerInfoDto from a dict
series_timer_info_dto_from_dict = SeriesTimerInfoDto.from_dict(series_timer_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


