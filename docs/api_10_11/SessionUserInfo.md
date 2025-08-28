# SessionUserInfo

Class SessionUserInfo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | Gets or sets the user identifier. | [optional] 
**user_name** | **str** | Gets or sets the name of the user. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.session_user_info import SessionUserInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SessionUserInfo from a JSON string
session_user_info_instance = SessionUserInfo.from_json(json)
# print the JSON string representation of the object
print(SessionUserInfo.to_json())

# convert the object into a dict
session_user_info_dict = session_user_info_instance.to_dict()
# create an instance of SessionUserInfo from a dict
session_user_info_from_dict = SessionUserInfo.from_dict(session_user_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


