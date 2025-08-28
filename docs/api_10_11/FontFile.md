# FontFile

Class FontFile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets the name. | [optional] 
**size** | **int** | Gets or sets the size. | [optional] 
**date_created** | **datetime** | Gets or sets the date created. | [optional] 
**date_modified** | **datetime** | Gets or sets the date modified. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.font_file import FontFile

# TODO update the JSON string below
json = "{}"
# create an instance of FontFile from a JSON string
font_file_instance = FontFile.from_json(json)
# print the JSON string representation of the object
print(FontFile.to_json())

# convert the object into a dict
font_file_dict = font_file_instance.to_dict()
# create an instance of FontFile from a dict
font_file_from_dict = FontFile.from_dict(font_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


