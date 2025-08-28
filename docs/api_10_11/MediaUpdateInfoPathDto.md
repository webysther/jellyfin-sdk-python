# MediaUpdateInfoPathDto

The media update info path.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Gets or sets media path. | [optional] 
**update_type** | **str** | Gets or sets media update type.  Created, Modified, Deleted. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.media_update_info_path_dto import MediaUpdateInfoPathDto

# TODO update the JSON string below
json = "{}"
# create an instance of MediaUpdateInfoPathDto from a JSON string
media_update_info_path_dto_instance = MediaUpdateInfoPathDto.from_json(json)
# print the JSON string representation of the object
print(MediaUpdateInfoPathDto.to_json())

# convert the object into a dict
media_update_info_path_dto_dict = media_update_info_path_dto_instance.to_dict()
# create an instance of MediaUpdateInfoPathDto from a dict
media_update_info_path_dto_from_dict = MediaUpdateInfoPathDto.from_dict(media_update_info_path_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


