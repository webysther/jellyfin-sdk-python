# CollectionCreationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.collection_creation_result import CollectionCreationResult

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionCreationResult from a JSON string
collection_creation_result_instance = CollectionCreationResult.from_json(json)
# print the JSON string representation of the object
print(CollectionCreationResult.to_json())

# convert the object into a dict
collection_creation_result_dict = collection_creation_result_instance.to_dict()
# create an instance of CollectionCreationResult from a dict
collection_creation_result_from_dict = CollectionCreationResult.from_dict(collection_creation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


