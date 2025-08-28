# MediaUrl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.media_url import MediaUrl

# TODO update the JSON string below
json = "{}"
# create an instance of MediaUrl from a JSON string
media_url_instance = MediaUrl.from_json(json)
# print the JSON string representation of the object
print(MediaUrl.to_json())

# convert the object into a dict
media_url_dict = media_url_instance.to_dict()
# create an instance of MediaUrl from a dict
media_url_from_dict = MediaUrl.from_dict(media_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


