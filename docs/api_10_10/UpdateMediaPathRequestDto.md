# UpdateMediaPathRequestDto

Update library options dto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets the library name. | 
**path_info** | [**MediaPathInfo**](MediaPathInfo.md) |  | 

## Example

```python
from jellyfin.generated.api_10_10.models.update_media_path_request_dto import UpdateMediaPathRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMediaPathRequestDto from a JSON string
update_media_path_request_dto_instance = UpdateMediaPathRequestDto.from_json(json)
# print the JSON string representation of the object
print(UpdateMediaPathRequestDto.to_json())

# convert the object into a dict
update_media_path_request_dto_dict = update_media_path_request_dto_instance.to_dict()
# create an instance of UpdateMediaPathRequestDto from a dict
update_media_path_request_dto_from_dict = UpdateMediaPathRequestDto.from_dict(update_media_path_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


