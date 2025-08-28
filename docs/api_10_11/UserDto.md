# UserDto

Class UserDto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets the name. | [optional] 
**server_id** | **str** | Gets or sets the server identifier. | [optional] 
**server_name** | **str** | Gets or sets the name of the server.  This is not used by the server and is for client-side usage only. | [optional] 
**id** | **str** | Gets or sets the id. | [optional] 
**primary_image_tag** | **str** | Gets or sets the primary image tag. | [optional] 
**has_password** | **bool** | Gets or sets a value indicating whether this instance has password. | [optional] 
**has_configured_password** | **bool** | Gets or sets a value indicating whether this instance has configured password. | [optional] 
**has_configured_easy_password** | **bool** | Gets or sets a value indicating whether this instance has configured easy password. | [optional] 
**enable_auto_login** | **bool** | Gets or sets whether async login is enabled or not. | [optional] 
**last_login_date** | **datetime** | Gets or sets the last login date. | [optional] 
**last_activity_date** | **datetime** | Gets or sets the last activity date. | [optional] 
**configuration** | [**UserConfiguration**](UserConfiguration.md) | Gets or sets the configuration. | [optional] 
**policy** | [**UserPolicy**](UserPolicy.md) | Gets or sets the policy. | [optional] 
**primary_image_aspect_ratio** | **float** | Gets or sets the primary image aspect ratio. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.user_dto import UserDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserDto from a JSON string
user_dto_instance = UserDto.from_json(json)
# print the JSON string representation of the object
print(UserDto.to_json())

# convert the object into a dict
user_dto_dict = user_dto_instance.to_dict()
# create an instance of UserDto from a dict
user_dto_from_dict = UserDto.from_dict(user_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


