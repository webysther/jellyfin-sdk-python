# ImageInfo

Class ImageInfo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_type** | [**ImageType**](ImageType.md) |  | [optional] 
**image_index** | **int** | Gets or sets the index of the image. | [optional] 
**image_tag** | **str** | Gets or sets the image tag. | [optional] 
**path** | **str** | Gets or sets the path. | [optional] 
**blur_hash** | **str** | Gets or sets the blurhash. | [optional] 
**height** | **int** | Gets or sets the height. | [optional] 
**width** | **int** | Gets or sets the width. | [optional] 
**size** | **int** | Gets or sets the size. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.image_info import ImageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ImageInfo from a JSON string
image_info_instance = ImageInfo.from_json(json)
# print the JSON string representation of the object
print(ImageInfo.to_json())

# convert the object into a dict
image_info_dict = image_info_instance.to_dict()
# create an instance of ImageInfo from a dict
image_info_from_dict = ImageInfo.from_dict(image_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


