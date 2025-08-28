# NameGuidPair


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.name_guid_pair import NameGuidPair

# TODO update the JSON string below
json = "{}"
# create an instance of NameGuidPair from a JSON string
name_guid_pair_instance = NameGuidPair.from_json(json)
# print the JSON string representation of the object
print(NameGuidPair.to_json())

# convert the object into a dict
name_guid_pair_dict = name_guid_pair_instance.to_dict()
# create an instance of NameGuidPair from a dict
name_guid_pair_from_dict = NameGuidPair.from_dict(name_guid_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


