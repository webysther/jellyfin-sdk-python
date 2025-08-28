# UtcTimeResponse

Class UtcTimeResponse.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_reception_time** | **datetime** | Gets the UTC time when request has been received. | [optional] 
**response_transmission_time** | **datetime** | Gets the UTC time when response has been sent. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.utc_time_response import UtcTimeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UtcTimeResponse from a JSON string
utc_time_response_instance = UtcTimeResponse.from_json(json)
# print the JSON string representation of the object
print(UtcTimeResponse.to_json())

# convert the object into a dict
utc_time_response_dict = utc_time_response_instance.to_dict()
# create an instance of UtcTimeResponse from a dict
utc_time_response_from_dict = UtcTimeResponse.from_dict(utc_time_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


