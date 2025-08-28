# BrandingOptionsDto

The branding options DTO for API use.  This DTO excludes SplashscreenLocation to prevent it from being updated via API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_disclaimer** | **str** | Gets or sets the login disclaimer. | [optional] 
**custom_css** | **str** | Gets or sets the custom CSS. | [optional] 
**splashscreen_enabled** | **bool** | Gets or sets a value indicating whether to enable the splashscreen. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.branding_options_dto import BrandingOptionsDto

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingOptionsDto from a JSON string
branding_options_dto_instance = BrandingOptionsDto.from_json(json)
# print the JSON string representation of the object
print(BrandingOptionsDto.to_json())

# convert the object into a dict
branding_options_dto_dict = branding_options_dto_instance.to_dict()
# create an instance of BrandingOptionsDto from a dict
branding_options_dto_from_dict = BrandingOptionsDto.from_dict(branding_options_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


