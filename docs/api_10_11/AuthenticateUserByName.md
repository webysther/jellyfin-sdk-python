# AuthenticateUserByName

The authenticate user by name request body.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Gets or sets the username. | [optional] 
**pw** | **str** | Gets or sets the plain text password. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.authenticate_user_by_name import AuthenticateUserByName

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticateUserByName from a JSON string
authenticate_user_by_name_instance = AuthenticateUserByName.from_json(json)
# print the JSON string representation of the object
print(AuthenticateUserByName.to_json())

# convert the object into a dict
authenticate_user_by_name_dict = authenticate_user_by_name_instance.to_dict()
# create an instance of AuthenticateUserByName from a dict
authenticate_user_by_name_from_dict = AuthenticateUserByName.from_dict(authenticate_user_by_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


