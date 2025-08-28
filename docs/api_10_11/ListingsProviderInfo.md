# ListingsProviderInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**listings_id** | **str** |  | [optional] 
**zip_code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**enabled_tuners** | **List[str]** |  | [optional] 
**enable_all_tuners** | **bool** |  | [optional] 
**news_categories** | **List[str]** |  | [optional] 
**sports_categories** | **List[str]** |  | [optional] 
**kids_categories** | **List[str]** |  | [optional] 
**movie_categories** | **List[str]** |  | [optional] 
**channel_mappings** | [**List[NameValuePair]**](NameValuePair.md) |  | [optional] 
**movie_prefix** | **str** |  | [optional] 
**preferred_language** | **str** |  | [optional] 
**user_agent** | **str** |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.listings_provider_info import ListingsProviderInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ListingsProviderInfo from a JSON string
listings_provider_info_instance = ListingsProviderInfo.from_json(json)
# print the JSON string representation of the object
print(ListingsProviderInfo.to_json())

# convert the object into a dict
listings_provider_info_dict = listings_provider_info_instance.to_dict()
# create an instance of ListingsProviderInfo from a dict
listings_provider_info_from_dict = ListingsProviderInfo.from_dict(listings_provider_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


