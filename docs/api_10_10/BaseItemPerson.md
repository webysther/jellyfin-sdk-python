# BaseItemPerson

This is used by the api to get information about a Person within a BaseItem.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets the name. | [optional] 
**id** | **str** | Gets or sets the identifier. | [optional] 
**role** | **str** | Gets or sets the role. | [optional] 
**type** | [**PersonKind**](PersonKind.md) |  | [optional] 
**primary_image_tag** | **str** | Gets or sets the primary image tag. | [optional] 
**image_blur_hashes** | [**BaseItemPersonImageBlurHashes**](BaseItemPersonImageBlurHashes.md) |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.base_item_person import BaseItemPerson

# TODO update the JSON string below
json = "{}"
# create an instance of BaseItemPerson from a JSON string
base_item_person_instance = BaseItemPerson.from_json(json)
# print the JSON string representation of the object
print(BaseItemPerson.to_json())

# convert the object into a dict
base_item_person_dict = base_item_person_instance.to_dict()
# create an instance of BaseItemPerson from a dict
base_item_person_from_dict = BaseItemPerson.from_dict(base_item_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


