# NameValuePair


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets the name. | [optional] 
**value** | **str** | Gets or sets the value. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.name_value_pair import NameValuePair

# TODO update the JSON string below
json = "{}"
# create an instance of NameValuePair from a JSON string
name_value_pair_instance = NameValuePair.from_json(json)
# print the JSON string representation of the object
print(NameValuePair.to_json())

# convert the object into a dict
name_value_pair_dict = name_value_pair_instance.to_dict()
# create an instance of NameValuePair from a dict
name_value_pair_from_dict = NameValuePair.from_dict(name_value_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


