# EndPointInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_local** | **bool** |  | [optional] 
**is_in_network** | **bool** |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.end_point_info import EndPointInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EndPointInfo from a JSON string
end_point_info_instance = EndPointInfo.from_json(json)
# print the JSON string representation of the object
print(EndPointInfo.to_json())

# convert the object into a dict
end_point_info_dict = end_point_info_instance.to_dict()
# create an instance of EndPointInfo from a dict
end_point_info_from_dict = EndPointInfo.from_dict(end_point_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


