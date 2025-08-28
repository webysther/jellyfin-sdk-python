# MediaAttachment

Class MediaAttachment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codec** | **str** | Gets or sets the codec. | [optional] 
**codec_tag** | **str** | Gets or sets the codec tag. | [optional] 
**comment** | **str** | Gets or sets the comment. | [optional] 
**index** | **int** | Gets or sets the index. | [optional] 
**file_name** | **str** | Gets or sets the filename. | [optional] 
**mime_type** | **str** | Gets or sets the MIME type. | [optional] 
**delivery_url** | **str** | Gets or sets the delivery URL. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.media_attachment import MediaAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of MediaAttachment from a JSON string
media_attachment_instance = MediaAttachment.from_json(json)
# print the JSON string representation of the object
print(MediaAttachment.to_json())

# convert the object into a dict
media_attachment_dict = media_attachment_instance.to_dict()
# create an instance of MediaAttachment from a dict
media_attachment_from_dict = MediaAttachment.from_dict(media_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


