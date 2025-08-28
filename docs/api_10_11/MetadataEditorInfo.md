# MetadataEditorInfo

A class representing metadata editor information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parental_rating_options** | [**List[ParentalRating]**](ParentalRating.md) | Gets or sets the parental rating options. | [optional] 
**countries** | [**List[CountryInfo]**](CountryInfo.md) | Gets or sets the countries. | [optional] 
**cultures** | [**List[CultureDto]**](CultureDto.md) | Gets or sets the cultures. | [optional] 
**external_id_infos** | [**List[ExternalIdInfo]**](ExternalIdInfo.md) | Gets or sets the external id infos. | [optional] 
**content_type** | [**CollectionType**](CollectionType.md) | Gets or sets the content type. | [optional] 
**content_type_options** | [**List[NameValuePair]**](NameValuePair.md) | Gets or sets the content type options. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.metadata_editor_info import MetadataEditorInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataEditorInfo from a JSON string
metadata_editor_info_instance = MetadataEditorInfo.from_json(json)
# print the JSON string representation of the object
print(MetadataEditorInfo.to_json())

# convert the object into a dict
metadata_editor_info_dict = metadata_editor_info_instance.to_dict()
# create an instance of MetadataEditorInfo from a dict
metadata_editor_info_from_dict = MetadataEditorInfo.from_dict(metadata_editor_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


