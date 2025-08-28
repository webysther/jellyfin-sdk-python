# ExternalIdInfo

Represents the external id information for serialization to the client.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Gets or sets the display name of the external id provider (IE: IMDB, MusicBrainz, etc). | [optional] 
**key** | **str** | Gets or sets the unique key for this id. This key should be unique across all providers. | [optional] 
**type** | [**ExternalIdMediaType**](ExternalIdMediaType.md) |  | [optional] 
**url_format_string** | **str** | Gets or sets the URL format string. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.external_id_info import ExternalIdInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalIdInfo from a JSON string
external_id_info_instance = ExternalIdInfo.from_json(json)
# print the JSON string representation of the object
print(ExternalIdInfo.to_json())

# convert the object into a dict
external_id_info_dict = external_id_info_instance.to_dict()
# create an instance of ExternalIdInfo from a dict
external_id_info_from_dict = ExternalIdInfo.from_dict(external_id_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


