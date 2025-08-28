# PathSubstitution

Defines the MediaBrowser.Model.Configuration.PathSubstitution.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | Gets or sets the value to substitute. | [optional] 
**to** | **str** | Gets or sets the value to substitution with. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.path_substitution import PathSubstitution

# TODO update the JSON string below
json = "{}"
# create an instance of PathSubstitution from a JSON string
path_substitution_instance = PathSubstitution.from_json(json)
# print the JSON string representation of the object
print(PathSubstitution.to_json())

# convert the object into a dict
path_substitution_dict = path_substitution_instance.to_dict()
# create an instance of PathSubstitution from a dict
path_substitution_from_dict = PathSubstitution.from_dict(path_substitution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


