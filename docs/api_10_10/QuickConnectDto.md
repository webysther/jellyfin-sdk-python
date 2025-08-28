# QuickConnectDto

The quick connect request body.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret** | **str** | Gets or sets the quick connect secret. | 

## Example

```python
from jellyfin.generated.api_10_10.models.quick_connect_dto import QuickConnectDto

# TODO update the JSON string below
json = "{}"
# create an instance of QuickConnectDto from a JSON string
quick_connect_dto_instance = QuickConnectDto.from_json(json)
# print the JSON string representation of the object
print(QuickConnectDto.to_json())

# convert the object into a dict
quick_connect_dto_dict = quick_connect_dto_instance.to_dict()
# create an instance of QuickConnectDto from a dict
quick_connect_dto_from_dict = QuickConnectDto.from_dict(quick_connect_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


