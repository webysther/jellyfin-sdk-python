# ImageOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ImageType**](ImageType.md) | Gets or sets the type. | [optional] 
**limit** | **int** | Gets or sets the limit. | [optional] 
**min_width** | **int** | Gets or sets the minimum width. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.image_option import ImageOption

# TODO update the JSON string below
json = "{}"
# create an instance of ImageOption from a JSON string
image_option_instance = ImageOption.from_json(json)
# print the JSON string representation of the object
print(ImageOption.to_json())

# convert the object into a dict
image_option_dict = image_option_instance.to_dict()
# create an instance of ImageOption from a dict
image_option_from_dict = ImageOption.from_dict(image_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


