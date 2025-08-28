# RemoteLyricInfoDto

The remote lyric info dto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Gets or sets the id for the lyric. | [optional] 
**provider_name** | **str** | Gets the provider name. | [optional] 
**lyrics** | [**LyricDto**](LyricDto.md) |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.remote_lyric_info_dto import RemoteLyricInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteLyricInfoDto from a JSON string
remote_lyric_info_dto_instance = RemoteLyricInfoDto.from_json(json)
# print the JSON string representation of the object
print(RemoteLyricInfoDto.to_json())

# convert the object into a dict
remote_lyric_info_dto_dict = remote_lyric_info_dto_instance.to_dict()
# create an instance of RemoteLyricInfoDto from a dict
remote_lyric_info_dto_from_dict = RemoteLyricInfoDto.from_dict(remote_lyric_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


