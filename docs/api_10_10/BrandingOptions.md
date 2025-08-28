# BrandingOptions

The branding options.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_disclaimer** | **str** | Gets or sets the login disclaimer. | [optional] 
**custom_css** | **str** | Gets or sets the custom CSS. | [optional] 
**splashscreen_enabled** | **bool** | Gets or sets a value indicating whether to enable the splashscreen. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.branding_options import BrandingOptions

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingOptions from a JSON string
branding_options_instance = BrandingOptions.from_json(json)
# print the JSON string representation of the object
print(BrandingOptions.to_json())

# convert the object into a dict
branding_options_dict = branding_options_instance.to_dict()
# create an instance of BrandingOptions from a dict
branding_options_from_dict = BrandingOptions.from_dict(branding_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


