# AuthenticationResult

A class representing an authentication result.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**UserDto**](UserDto.md) | Class UserDto. | [optional] 
**session_info** | [**SessionInfoDto**](SessionInfoDto.md) | Session info DTO. | [optional] 
**access_token** | **str** | Gets or sets the access token. | [optional] 
**server_id** | **str** | Gets or sets the server id. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.authentication_result import AuthenticationResult

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationResult from a JSON string
authentication_result_instance = AuthenticationResult.from_json(json)
# print the JSON string representation of the object
print(AuthenticationResult.to_json())

# convert the object into a dict
authentication_result_dict = authentication_result_instance.to_dict()
# create an instance of AuthenticationResult from a dict
authentication_result_from_dict = AuthenticationResult.from_dict(authentication_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


