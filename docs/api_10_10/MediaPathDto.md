# MediaPathDto

Media Path dto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets the name of the library. | 
**path** | **str** | Gets or sets the path to add. | [optional] 
**path_info** | [**MediaPathInfo**](MediaPathInfo.md) |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.media_path_dto import MediaPathDto

# TODO update the JSON string below
json = "{}"
# create an instance of MediaPathDto from a JSON string
media_path_dto_instance = MediaPathDto.from_json(json)
# print the JSON string representation of the object
print(MediaPathDto.to_json())

# convert the object into a dict
media_path_dto_dict = media_path_dto_instance.to_dict()
# create an instance of MediaPathDto from a dict
media_path_dto_from_dict = MediaPathDto.from_dict(media_path_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


