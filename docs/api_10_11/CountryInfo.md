# CountryInfo

Class CountryInfo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets the name. | [optional] 
**display_name** | **str** | Gets or sets the display name. | [optional] 
**two_letter_iso_region_name** | **str** | Gets or sets the name of the two letter ISO region. | [optional] 
**three_letter_iso_region_name** | **str** | Gets or sets the name of the three letter ISO region. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.country_info import CountryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CountryInfo from a JSON string
country_info_instance = CountryInfo.from_json(json)
# print the JSON string representation of the object
print(CountryInfo.to_json())

# convert the object into a dict
country_info_dict = country_info_instance.to_dict()
# create an instance of CountryInfo from a dict
country_info_from_dict = CountryInfo.from_dict(country_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


