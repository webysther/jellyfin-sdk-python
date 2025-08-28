# ForgotPasswordDto

Forgot Password request body DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entered_username** | **str** | Gets or sets the entered username to have its password reset. | 

## Example

```python
from jellyfin.generated.api_10_10.models.forgot_password_dto import ForgotPasswordDto

# TODO update the JSON string below
json = "{}"
# create an instance of ForgotPasswordDto from a JSON string
forgot_password_dto_instance = ForgotPasswordDto.from_json(json)
# print the JSON string representation of the object
print(ForgotPasswordDto.to_json())

# convert the object into a dict
forgot_password_dto_dict = forgot_password_dto_instance.to_dict()
# create an instance of ForgotPasswordDto from a dict
forgot_password_dto_from_dict = ForgotPasswordDto.from_dict(forgot_password_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


