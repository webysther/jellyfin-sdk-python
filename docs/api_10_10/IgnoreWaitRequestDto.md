# IgnoreWaitRequestDto

Class IgnoreWaitRequestDto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ignore_wait** | **bool** | Gets or sets a value indicating whether the client should be ignored. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.ignore_wait_request_dto import IgnoreWaitRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of IgnoreWaitRequestDto from a JSON string
ignore_wait_request_dto_instance = IgnoreWaitRequestDto.from_json(json)
# print the JSON string representation of the object
print(IgnoreWaitRequestDto.to_json())

# convert the object into a dict
ignore_wait_request_dto_dict = ignore_wait_request_dto_instance.to_dict()
# create an instance of IgnoreWaitRequestDto from a dict
ignore_wait_request_dto_from_dict = IgnoreWaitRequestDto.from_dict(ignore_wait_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


