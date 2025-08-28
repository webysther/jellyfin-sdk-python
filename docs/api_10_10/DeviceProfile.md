# DeviceProfile

A MediaBrowser.Model.Dlna.DeviceProfile represents a set of metadata which determines which content a certain device is able to play.  <br />  Specifically, it defines the supported <see cref=\"P:MediaBrowser.Model.Dlna.DeviceProfile.ContainerProfiles\">containers</see> and  <see cref=\"P:MediaBrowser.Model.Dlna.DeviceProfile.CodecProfiles\">codecs</see> (video and/or audio, including codec profiles and levels)  the device is able to direct play (without transcoding or remuxing),  as well as which <see cref=\"P:MediaBrowser.Model.Dlna.DeviceProfile.TranscodingProfiles\">containers/codecs to transcode to</see> in case it isn't.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets the name of this device profile. User profiles must have a unique name. | [optional] 
**id** | **str** | Gets or sets the unique internal identifier. | [optional] 
**max_streaming_bitrate** | **int** | Gets or sets the maximum allowed bitrate for all streamed content. | [optional] 
**max_static_bitrate** | **int** | Gets or sets the maximum allowed bitrate for statically streamed content (&#x3D; direct played files). | [optional] 
**music_streaming_transcoding_bitrate** | **int** | Gets or sets the maximum allowed bitrate for transcoded music streams. | [optional] 
**max_static_music_bitrate** | **int** | Gets or sets the maximum allowed bitrate for statically streamed (&#x3D; direct played) music files. | [optional] 
**direct_play_profiles** | [**List[DirectPlayProfile]**](DirectPlayProfile.md) | Gets or sets the direct play profiles. | [optional] 
**transcoding_profiles** | [**List[TranscodingProfile]**](TranscodingProfile.md) | Gets or sets the transcoding profiles. | [optional] 
**container_profiles** | [**List[ContainerProfile]**](ContainerProfile.md) | Gets or sets the container profiles. Failing to meet these optional conditions causes transcoding to occur. | [optional] 
**codec_profiles** | [**List[CodecProfile]**](CodecProfile.md) | Gets or sets the codec profiles. | [optional] 
**subtitle_profiles** | [**List[SubtitleProfile]**](SubtitleProfile.md) | Gets or sets the subtitle profiles. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.device_profile import DeviceProfile

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceProfile from a JSON string
device_profile_instance = DeviceProfile.from_json(json)
# print the JSON string representation of the object
print(DeviceProfile.to_json())

# convert the object into a dict
device_profile_dict = device_profile_instance.to_dict()
# create an instance of DeviceProfile from a dict
device_profile_from_dict = DeviceProfile.from_dict(device_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


