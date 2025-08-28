# PlaybackInfoResponse

Class PlaybackInfoResponse.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media_sources** | [**List[MediaSourceInfo]**](MediaSourceInfo.md) | Gets or sets the media sources. | [optional] 
**play_session_id** | **str** | Gets or sets the play session identifier. | [optional] 
**error_code** | [**PlaybackErrorCode**](PlaybackErrorCode.md) | Gets or sets the error code. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.playback_info_response import PlaybackInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlaybackInfoResponse from a JSON string
playback_info_response_instance = PlaybackInfoResponse.from_json(json)
# print the JSON string representation of the object
print(PlaybackInfoResponse.to_json())

# convert the object into a dict
playback_info_response_dict = playback_info_response_instance.to_dict()
# create an instance of PlaybackInfoResponse from a dict
playback_info_response_from_dict = PlaybackInfoResponse.from_dict(playback_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


