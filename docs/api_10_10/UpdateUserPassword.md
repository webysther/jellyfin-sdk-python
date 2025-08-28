# UpdateUserPassword

The update user password request body.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_password** | **str** | Gets or sets the current sha1-hashed password. | [optional] 
**current_pw** | **str** | Gets or sets the current plain text password. | [optional] 
**new_pw** | **str** | Gets or sets the new plain text password. | [optional] 
**reset_password** | **bool** | Gets or sets a value indicating whether to reset the password. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.update_user_password import UpdateUserPassword

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserPassword from a JSON string
update_user_password_instance = UpdateUserPassword.from_json(json)
# print the JSON string representation of the object
print(UpdateUserPassword.to_json())

# convert the object into a dict
update_user_password_dict = update_user_password_instance.to_dict()
# create an instance of UpdateUserPassword from a dict
update_user_password_from_dict = UpdateUserPassword.from_dict(update_user_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


