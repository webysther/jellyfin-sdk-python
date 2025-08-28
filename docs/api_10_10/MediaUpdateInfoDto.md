# MediaUpdateInfoDto

Media Update Info Dto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updates** | [**List[MediaUpdateInfoPathDto]**](MediaUpdateInfoPathDto.md) | Gets or sets the list of updates. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.media_update_info_dto import MediaUpdateInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of MediaUpdateInfoDto from a JSON string
media_update_info_dto_instance = MediaUpdateInfoDto.from_json(json)
# print the JSON string representation of the object
print(MediaUpdateInfoDto.to_json())

# convert the object into a dict
media_update_info_dto_dict = media_update_info_dto_instance.to_dict()
# create an instance of MediaUpdateInfoDto from a dict
media_update_info_dto_from_dict = MediaUpdateInfoDto.from_dict(media_update_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


