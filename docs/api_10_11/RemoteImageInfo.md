# RemoteImageInfo

Class RemoteImageInfo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_name** | **str** | Gets or sets the name of the provider. | [optional] 
**url** | **str** | Gets or sets the URL. | [optional] 
**thumbnail_url** | **str** | Gets or sets a url used for previewing a smaller version. | [optional] 
**height** | **int** | Gets or sets the height. | [optional] 
**width** | **int** | Gets or sets the width. | [optional] 
**community_rating** | **float** | Gets or sets the community rating. | [optional] 
**vote_count** | **int** | Gets or sets the vote count. | [optional] 
**language** | **str** | Gets or sets the language. | [optional] 
**type** | [**ImageType**](ImageType.md) | Gets or sets the type. | [optional] 
**rating_type** | [**RatingType**](RatingType.md) | Gets or sets the type of the rating. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.remote_image_info import RemoteImageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteImageInfo from a JSON string
remote_image_info_instance = RemoteImageInfo.from_json(json)
# print the JSON string representation of the object
print(RemoteImageInfo.to_json())

# convert the object into a dict
remote_image_info_dict = remote_image_info_instance.to_dict()
# create an instance of RemoteImageInfo from a dict
remote_image_info_from_dict = RemoteImageInfo.from_dict(remote_image_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


