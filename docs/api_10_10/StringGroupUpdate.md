# StringGroupUpdate

Class GroupUpdate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | Gets the group identifier. | [optional] [readonly] 
**type** | [**GroupUpdateType**](GroupUpdateType.md) |  | [optional] 
**data** | **str** | Gets the update data. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.string_group_update import StringGroupUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of StringGroupUpdate from a JSON string
string_group_update_instance = StringGroupUpdate.from_json(json)
# print the JSON string representation of the object
print(StringGroupUpdate.to_json())

# convert the object into a dict
string_group_update_dict = string_group_update_instance.to_dict()
# create an instance of StringGroupUpdate from a dict
string_group_update_from_dict = StringGroupUpdate.from_dict(string_group_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


