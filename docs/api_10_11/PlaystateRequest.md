# PlaystateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | [**PlaystateCommand**](PlaystateCommand.md) | Enum PlaystateCommand. | [optional] 
**seek_position_ticks** | **int** |  | [optional] 
**controlling_user_id** | **str** | Gets or sets the controlling user identifier. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.playstate_request import PlaystateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlaystateRequest from a JSON string
playstate_request_instance = PlaystateRequest.from_json(json)
# print the JSON string representation of the object
print(PlaystateRequest.to_json())

# convert the object into a dict
playstate_request_dict = playstate_request_instance.to_dict()
# create an instance of PlaystateRequest from a dict
playstate_request_from_dict = PlaystateRequest.from_dict(playstate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


