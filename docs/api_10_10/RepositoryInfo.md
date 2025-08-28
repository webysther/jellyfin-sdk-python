# RepositoryInfo

Class RepositoryInfo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets the name. | [optional] 
**url** | **str** | Gets or sets the URL. | [optional] 
**enabled** | **bool** | Gets or sets a value indicating whether the repository is enabled. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.repository_info import RepositoryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryInfo from a JSON string
repository_info_instance = RepositoryInfo.from_json(json)
# print the JSON string representation of the object
print(RepositoryInfo.to_json())

# convert the object into a dict
repository_info_dict = repository_info_instance.to_dict()
# create an instance of RepositoryInfo from a dict
repository_info_from_dict = RepositoryInfo.from_dict(repository_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


