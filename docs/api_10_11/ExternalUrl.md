# ExternalUrl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets the name. | [optional] 
**url** | **str** | Gets or sets the type of the item. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.external_url import ExternalUrl

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalUrl from a JSON string
external_url_instance = ExternalUrl.from_json(json)
# print the JSON string representation of the object
print(ExternalUrl.to_json())

# convert the object into a dict
external_url_dict = external_url_instance.to_dict()
# create an instance of ExternalUrl from a dict
external_url_from_dict = ExternalUrl.from_dict(external_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


