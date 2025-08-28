# PlaybackStopInfo

Class PlaybackStopInfo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item** | [**BaseItemDto**](BaseItemDto.md) |  | [optional] 
**item_id** | **str** | Gets or sets the item identifier. | [optional] 
**session_id** | **str** | Gets or sets the session id. | [optional] 
**media_source_id** | **str** | Gets or sets the media version identifier. | [optional] 
**position_ticks** | **int** | Gets or sets the position ticks. | [optional] 
**live_stream_id** | **str** | Gets or sets the live stream identifier. | [optional] 
**play_session_id** | **str** | Gets or sets the play session identifier. | [optional] 
**failed** | **bool** | Gets or sets a value indicating whether this MediaBrowser.Model.Session.PlaybackStopInfo is failed. | [optional] 
**next_media_type** | **str** |  | [optional] 
**playlist_item_id** | **str** |  | [optional] 
**now_playing_queue** | [**List[QueueItem]**](QueueItem.md) |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.playback_stop_info import PlaybackStopInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PlaybackStopInfo from a JSON string
playback_stop_info_instance = PlaybackStopInfo.from_json(json)
# print the JSON string representation of the object
print(PlaybackStopInfo.to_json())

# convert the object into a dict
playback_stop_info_dict = playback_stop_info_instance.to_dict()
# create an instance of PlaybackStopInfo from a dict
playback_stop_info_from_dict = PlaybackStopInfo.from_dict(playback_stop_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


