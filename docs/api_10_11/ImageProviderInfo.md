# ImageProviderInfo

Class ImageProviderInfo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets the name. | [optional] 
**supported_images** | [**List[ImageType]**](ImageType.md) | Gets the supported image types. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.image_provider_info import ImageProviderInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ImageProviderInfo from a JSON string
image_provider_info_instance = ImageProviderInfo.from_json(json)
# print the JSON string representation of the object
print(ImageProviderInfo.to_json())

# convert the object into a dict
image_provider_info_dict = image_provider_info_instance.to_dict()
# create an instance of ImageProviderInfo from a dict
image_provider_info_from_dict = ImageProviderInfo.from_dict(image_provider_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


