# BaseItemPersonImageBlurHashes

Gets or sets the primary image blurhash.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary** | **Dict[str, str]** |  | [optional] 
**art** | **Dict[str, str]** |  | [optional] 
**backdrop** | **Dict[str, str]** |  | [optional] 
**banner** | **Dict[str, str]** |  | [optional] 
**logo** | **Dict[str, str]** |  | [optional] 
**thumb** | **Dict[str, str]** |  | [optional] 
**disc** | **Dict[str, str]** |  | [optional] 
**box** | **Dict[str, str]** |  | [optional] 
**screenshot** | **Dict[str, str]** |  | [optional] 
**menu** | **Dict[str, str]** |  | [optional] 
**chapter** | **Dict[str, str]** |  | [optional] 
**box_rear** | **Dict[str, str]** |  | [optional] 
**profile** | **Dict[str, str]** |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.base_item_person_image_blur_hashes import BaseItemPersonImageBlurHashes

# TODO update the JSON string below
json = "{}"
# create an instance of BaseItemPersonImageBlurHashes from a JSON string
base_item_person_image_blur_hashes_instance = BaseItemPersonImageBlurHashes.from_json(json)
# print the JSON string representation of the object
print(BaseItemPersonImageBlurHashes.to_json())

# convert the object into a dict
base_item_person_image_blur_hashes_dict = base_item_person_image_blur_hashes_instance.to_dict()
# create an instance of BaseItemPersonImageBlurHashes from a dict
base_item_person_image_blur_hashes_from_dict = BaseItemPersonImageBlurHashes.from_dict(base_item_person_image_blur_hashes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


