# TimerInfoDto


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
**status** | [**RecordingStatus**](RecordingStatus.md) |  | [optional] 
**series_timer_id** | **str** | Gets or sets the series timer identifier. | [optional] 
**external_series_timer_id** | **str** | Gets or sets the external series timer identifier. | [optional] 
**run_time_ticks** | **int** | Gets or sets the run time ticks. | [optional] 
**program_info** | [**BaseItemDto**](BaseItemDto.md) |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.timer_info_dto import TimerInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of TimerInfoDto from a JSON string
timer_info_dto_instance = TimerInfoDto.from_json(json)
# print the JSON string representation of the object
print(TimerInfoDto.to_json())

# convert the object into a dict
timer_info_dto_dict = timer_info_dto_instance.to_dict()
# create an instance of TimerInfoDto from a dict
timer_info_dto_from_dict = TimerInfoDto.from_dict(timer_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


