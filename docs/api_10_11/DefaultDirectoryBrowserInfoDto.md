# DefaultDirectoryBrowserInfoDto

Default directory browser info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Gets or sets the path. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.default_directory_browser_info_dto import DefaultDirectoryBrowserInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultDirectoryBrowserInfoDto from a JSON string
default_directory_browser_info_dto_instance = DefaultDirectoryBrowserInfoDto.from_json(json)
# print the JSON string representation of the object
print(DefaultDirectoryBrowserInfoDto.to_json())

# convert the object into a dict
default_directory_browser_info_dto_dict = default_directory_browser_info_dto_instance.to_dict()
# create an instance of DefaultDirectoryBrowserInfoDto from a dict
default_directory_browser_info_dto_from_dict = DefaultDirectoryBrowserInfoDto.from_dict(default_directory_browser_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


