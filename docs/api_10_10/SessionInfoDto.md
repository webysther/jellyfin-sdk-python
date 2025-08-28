# SessionInfoDto

Session info DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**play_state** | [**PlayerStateInfo**](PlayerStateInfo.md) |  | [optional] 
**additional_users** | [**List[SessionUserInfo]**](SessionUserInfo.md) | Gets or sets the additional users. | [optional] 
**capabilities** | [**ClientCapabilitiesDto**](ClientCapabilitiesDto.md) |  | [optional] 
**remote_end_point** | **str** | Gets or sets the remote end point. | [optional] 
**playable_media_types** | [**List[MediaType]**](MediaType.md) | Gets or sets the playable media types. | [optional] 
**id** | **str** | Gets or sets the id. | [optional] 
**user_id** | **str** | Gets or sets the user id. | [optional] 
**user_name** | **str** | Gets or sets the username. | [optional] 
**client** | **str** | Gets or sets the type of the client. | [optional] 
**last_activity_date** | **datetime** | Gets or sets the last activity date. | [optional] 
**last_playback_check_in** | **datetime** | Gets or sets the last playback check in. | [optional] 
**last_paused_date** | **datetime** | Gets or sets the last paused date. | [optional] 
**device_name** | **str** | Gets or sets the name of the device. | [optional] 
**device_type** | **str** | Gets or sets the type of the device. | [optional] 
**now_playing_item** | [**BaseItemDto**](BaseItemDto.md) |  | [optional] 
**now_viewing_item** | [**BaseItemDto**](BaseItemDto.md) |  | [optional] 
**device_id** | **str** | Gets or sets the device id. | [optional] 
**application_version** | **str** | Gets or sets the application version. | [optional] 
**transcoding_info** | [**TranscodingInfo**](TranscodingInfo.md) |  | [optional] 
**is_active** | **bool** | Gets or sets a value indicating whether this session is active. | [optional] 
**supports_media_control** | **bool** | Gets or sets a value indicating whether the session supports media control. | [optional] 
**supports_remote_control** | **bool** | Gets or sets a value indicating whether the session supports remote control. | [optional] 
**now_playing_queue** | [**List[QueueItem]**](QueueItem.md) | Gets or sets the now playing queue. | [optional] 
**now_playing_queue_full_items** | [**List[BaseItemDto]**](BaseItemDto.md) | Gets or sets the now playing queue full items. | [optional] 
**has_custom_device_name** | **bool** | Gets or sets a value indicating whether the session has a custom device name. | [optional] 
**playlist_item_id** | **str** | Gets or sets the playlist item id. | [optional] 
**server_id** | **str** | Gets or sets the server id. | [optional] 
**user_primary_image_tag** | **str** | Gets or sets the user primary image tag. | [optional] 
**supported_commands** | [**List[GeneralCommandType]**](GeneralCommandType.md) | Gets or sets the supported commands. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.session_info_dto import SessionInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of SessionInfoDto from a JSON string
session_info_dto_instance = SessionInfoDto.from_json(json)
# print the JSON string representation of the object
print(SessionInfoDto.to_json())

# convert the object into a dict
session_info_dto_dict = session_info_dto_instance.to_dict()
# create an instance of SessionInfoDto from a dict
session_info_dto_from_dict = SessionInfoDto.from_dict(session_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


