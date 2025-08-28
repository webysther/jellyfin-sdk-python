# CodecProfile

Defines the MediaBrowser.Model.Dlna.CodecProfile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**CodecType**](CodecType.md) | Gets or sets the MediaBrowser.Model.Dlna.CodecType which this container must meet. | [optional] 
**conditions** | [**List[ProfileCondition]**](ProfileCondition.md) | Gets or sets the list of MediaBrowser.Model.Dlna.ProfileCondition which this profile must meet. | [optional] 
**apply_conditions** | [**List[ProfileCondition]**](ProfileCondition.md) | Gets or sets the list of MediaBrowser.Model.Dlna.ProfileCondition to apply if this profile is met. | [optional] 
**codec** | **str** | Gets or sets the codec(s) that this profile applies to. | [optional] 
**container** | **str** | Gets or sets the container(s) which this profile will be applied to. | [optional] 
**sub_container** | **str** | Gets or sets the sub-container(s) which this profile will be applied to. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.codec_profile import CodecProfile

# TODO update the JSON string below
json = "{}"
# create an instance of CodecProfile from a JSON string
codec_profile_instance = CodecProfile.from_json(json)
# print the JSON string representation of the object
print(CodecProfile.to_json())

# convert the object into a dict
codec_profile_dict = codec_profile_instance.to_dict()
# create an instance of CodecProfile from a dict
codec_profile_from_dict = CodecProfile.from_dict(codec_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


