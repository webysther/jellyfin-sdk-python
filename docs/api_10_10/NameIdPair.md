# NameIdPair


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets the name. | [optional] 
**id** | **str** | Gets or sets the identifier. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.name_id_pair import NameIdPair

# TODO update the JSON string below
json = "{}"
# create an instance of NameIdPair from a JSON string
name_id_pair_instance = NameIdPair.from_json(json)
# print the JSON string representation of the object
print(NameIdPair.to_json())

# convert the object into a dict
name_id_pair_dict = name_id_pair_instance.to_dict()
# create an instance of NameIdPair from a dict
name_id_pair_from_dict = NameIdPair.from_dict(name_id_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


