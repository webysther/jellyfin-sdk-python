# LiveStreamResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media_source** | [**MediaSourceInfo**](MediaSourceInfo.md) |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.live_stream_response import LiveStreamResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LiveStreamResponse from a JSON string
live_stream_response_instance = LiveStreamResponse.from_json(json)
# print the JSON string representation of the object
print(LiveStreamResponse.to_json())

# convert the object into a dict
live_stream_response_dict = live_stream_response_instance.to_dict()
# create an instance of LiveStreamResponse from a dict
live_stream_response_from_dict = LiveStreamResponse.from_dict(live_stream_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


