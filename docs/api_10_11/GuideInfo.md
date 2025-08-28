# GuideInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | Gets or sets the start date. | [optional] 
**end_date** | **datetime** | Gets or sets the end date. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.guide_info import GuideInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GuideInfo from a JSON string
guide_info_instance = GuideInfo.from_json(json)
# print the JSON string representation of the object
print(GuideInfo.to_json())

# convert the object into a dict
guide_info_dict = guide_info_instance.to_dict()
# create an instance of GuideInfo from a dict
guide_info_from_dict = GuideInfo.from_dict(guide_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


