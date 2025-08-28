# ForgotPasswordPinDto

Forgot Password Pin enter request body DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pin** | **str** | Gets or sets the entered pin to have the password reset. | 

## Example

```python
from jellyfin.generated.api_10_10.models.forgot_password_pin_dto import ForgotPasswordPinDto

# TODO update the JSON string below
json = "{}"
# create an instance of ForgotPasswordPinDto from a JSON string
forgot_password_pin_dto_instance = ForgotPasswordPinDto.from_json(json)
# print the JSON string representation of the object
print(ForgotPasswordPinDto.to_json())

# convert the object into a dict
forgot_password_pin_dto_dict = forgot_password_pin_dto_instance.to_dict()
# create an instance of ForgotPasswordPinDto from a dict
forgot_password_pin_dto_from_dict = ForgotPasswordPinDto.from_dict(forgot_password_pin_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


