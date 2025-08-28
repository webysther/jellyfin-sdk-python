# PingRequestDto

Class PingRequestDto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ping** | **int** | Gets or sets the ping time. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.ping_request_dto import PingRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of PingRequestDto from a JSON string
ping_request_dto_instance = PingRequestDto.from_json(json)
# print the JSON string representation of the object
print(PingRequestDto.to_json())

# convert the object into a dict
ping_request_dto_dict = ping_request_dto_instance.to_dict()
# create an instance of PingRequestDto from a dict
ping_request_dto_from_dict = PingRequestDto.from_dict(ping_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


