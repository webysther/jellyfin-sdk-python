# QuickConnectResult

Stores the state of an quick connect request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticated** | **bool** | Gets or sets a value indicating whether this request is authorized. | [optional] 
**secret** | **str** | Gets the secret value used to uniquely identify this request. Can be used to retrieve authentication information. | [optional] 
**code** | **str** | Gets the user facing code used so the user can quickly differentiate this request from others. | [optional] 
**device_id** | **str** | Gets the requesting device id. | [optional] 
**device_name** | **str** | Gets the requesting device name. | [optional] 
**app_name** | **str** | Gets the requesting app name. | [optional] 
**app_version** | **str** | Gets the requesting app version. | [optional] 
**date_added** | **datetime** | Gets or sets the DateTime that this request was created. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.quick_connect_result import QuickConnectResult

# TODO update the JSON string below
json = "{}"
# create an instance of QuickConnectResult from a JSON string
quick_connect_result_instance = QuickConnectResult.from_json(json)
# print the JSON string representation of the object
print(QuickConnectResult.to_json())

# convert the object into a dict
quick_connect_result_dict = quick_connect_result_instance.to_dict()
# create an instance of QuickConnectResult from a dict
quick_connect_result_from_dict = QuickConnectResult.from_dict(quick_connect_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


