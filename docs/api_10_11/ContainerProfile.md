# ContainerProfile

Defines the MediaBrowser.Model.Dlna.ContainerProfile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DlnaProfileType**](DlnaProfileType.md) | Gets or sets the MediaBrowser.Model.Dlna.DlnaProfileType which this container must meet. | [optional] 
**conditions** | [**List[ProfileCondition]**](ProfileCondition.md) | Gets or sets the list of MediaBrowser.Model.Dlna.ProfileCondition which this container will be applied to. | [optional] 
**container** | **str** | Gets or sets the container(s) which this container must meet. | [optional] 
**sub_container** | **str** | Gets or sets the sub container(s) which this container must meet. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.container_profile import ContainerProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerProfile from a JSON string
container_profile_instance = ContainerProfile.from_json(json)
# print the JSON string representation of the object
print(ContainerProfile.to_json())

# convert the object into a dict
container_profile_dict = container_profile_instance.to_dict()
# create an instance of ContainerProfile from a dict
container_profile_from_dict = ContainerProfile.from_dict(container_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


