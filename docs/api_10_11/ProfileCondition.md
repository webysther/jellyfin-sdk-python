# ProfileCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition** | [**ProfileConditionType**](ProfileConditionType.md) |  | [optional] 
**var_property** | [**ProfileConditionValue**](ProfileConditionValue.md) |  | [optional] 
**value** | **str** |  | [optional] 
**is_required** | **bool** |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.profile_condition import ProfileCondition

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileCondition from a JSON string
profile_condition_instance = ProfileCondition.from_json(json)
# print the JSON string representation of the object
print(ProfileCondition.to_json())

# convert the object into a dict
profile_condition_dict = profile_condition_instance.to_dict()
# create an instance of ProfileCondition from a dict
profile_condition_from_dict = ProfileCondition.from_dict(profile_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


