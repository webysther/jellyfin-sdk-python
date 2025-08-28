# MediaPathInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.media_path_info import MediaPathInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MediaPathInfo from a JSON string
media_path_info_instance = MediaPathInfo.from_json(json)
# print the JSON string representation of the object
print(MediaPathInfo.to_json())

# convert the object into a dict
media_path_info_dict = media_path_info_instance.to_dict()
# create an instance of MediaPathInfo from a dict
media_path_info_from_dict = MediaPathInfo.from_dict(media_path_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


