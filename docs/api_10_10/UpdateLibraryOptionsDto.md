# UpdateLibraryOptionsDto

Update library options dto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Gets or sets the library item id. | [optional] 
**library_options** | [**LibraryOptions**](LibraryOptions.md) |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.update_library_options_dto import UpdateLibraryOptionsDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateLibraryOptionsDto from a JSON string
update_library_options_dto_instance = UpdateLibraryOptionsDto.from_json(json)
# print the JSON string representation of the object
print(UpdateLibraryOptionsDto.to_json())

# convert the object into a dict
update_library_options_dto_dict = update_library_options_dto_instance.to_dict()
# create an instance of UpdateLibraryOptionsDto from a dict
update_library_options_dto_from_dict = UpdateLibraryOptionsDto.from_dict(update_library_options_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


