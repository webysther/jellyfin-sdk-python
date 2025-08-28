# ForgotPasswordResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**ForgotPasswordAction**](ForgotPasswordAction.md) | Gets or sets the action. | [optional] 
**pin_file** | **str** | Gets or sets the pin file. | [optional] 
**pin_expiration_date** | **datetime** | Gets or sets the pin expiration date. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.forgot_password_result import ForgotPasswordResult

# TODO update the JSON string below
json = "{}"
# create an instance of ForgotPasswordResult from a JSON string
forgot_password_result_instance = ForgotPasswordResult.from_json(json)
# print the JSON string representation of the object
print(ForgotPasswordResult.to_json())

# convert the object into a dict
forgot_password_result_dict = forgot_password_result_instance.to_dict()
# create an instance of ForgotPasswordResult from a dict
forgot_password_result_from_dict = ForgotPasswordResult.from_dict(forgot_password_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


