# AuthenticationInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Gets or sets the identifier. | [optional] 
**access_token** | **str** | Gets or sets the access token. | [optional] 
**device_id** | **str** | Gets or sets the device identifier. | [optional] 
**app_name** | **str** | Gets or sets the name of the application. | [optional] 
**app_version** | **str** | Gets or sets the application version. | [optional] 
**device_name** | **str** | Gets or sets the name of the device. | [optional] 
**user_id** | **str** | Gets or sets the user identifier. | [optional] 
**is_active** | **bool** | Gets or sets a value indicating whether this instance is active. | [optional] 
**date_created** | **datetime** | Gets or sets the date created. | [optional] 
**date_revoked** | **datetime** | Gets or sets the date revoked. | [optional] 
**date_last_activity** | **datetime** |  | [optional] 
**user_name** | **str** |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.authentication_info import AuthenticationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationInfo from a JSON string
authentication_info_instance = AuthenticationInfo.from_json(json)
# print the JSON string representation of the object
print(AuthenticationInfo.to_json())

# convert the object into a dict
authentication_info_dict = authentication_info_instance.to_dict()
# create an instance of AuthenticationInfo from a dict
authentication_info_from_dict = AuthenticationInfo.from_dict(authentication_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


