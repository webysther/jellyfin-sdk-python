# CastReceiverApplication

The cast receiver application model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Gets or sets the cast receiver application id. | [optional] 
**name** | **str** | Gets or sets the cast receiver application name. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.cast_receiver_application import CastReceiverApplication

# TODO update the JSON string below
json = "{}"
# create an instance of CastReceiverApplication from a JSON string
cast_receiver_application_instance = CastReceiverApplication.from_json(json)
# print the JSON string representation of the object
print(CastReceiverApplication.to_json())

# convert the object into a dict
cast_receiver_application_dict = cast_receiver_application_instance.to_dict()
# create an instance of CastReceiverApplication from a dict
cast_receiver_application_from_dict = CastReceiverApplication.from_dict(cast_receiver_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


