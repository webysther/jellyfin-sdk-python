# UserDataChangeInfo

Class UserDataChangeInfo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | Gets or sets the user id. | [optional] 
**user_data_list** | [**List[UserItemDataDto]**](UserItemDataDto.md) | Gets or sets the user data list. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.user_data_change_info import UserDataChangeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UserDataChangeInfo from a JSON string
user_data_change_info_instance = UserDataChangeInfo.from_json(json)
# print the JSON string representation of the object
print(UserDataChangeInfo.to_json())

# convert the object into a dict
user_data_change_info_dict = user_data_change_info_instance.to_dict()
# create an instance of UserDataChangeInfo from a dict
user_data_change_info_from_dict = UserDataChangeInfo.from_dict(user_data_change_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


