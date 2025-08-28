# DisplayPreferencesDto

Defines the display preferences for any item that supports them (usually Folders).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Gets or sets the user id. | [optional] 
**view_type** | **str** | Gets or sets the type of the view. | [optional] 
**sort_by** | **str** | Gets or sets the sort by. | [optional] 
**index_by** | **str** | Gets or sets the index by. | [optional] 
**remember_indexing** | **bool** | Gets or sets a value indicating whether [remember indexing]. | [optional] 
**primary_image_height** | **int** | Gets or sets the height of the primary image. | [optional] 
**primary_image_width** | **int** | Gets or sets the width of the primary image. | [optional] 
**custom_prefs** | **Dict[str, Optional[str]]** | Gets or sets the custom prefs. | [optional] 
**scroll_direction** | [**ScrollDirection**](ScrollDirection.md) |  | [optional] 
**show_backdrop** | **bool** | Gets or sets a value indicating whether to show backdrops on this item. | [optional] 
**remember_sorting** | **bool** | Gets or sets a value indicating whether [remember sorting]. | [optional] 
**sort_order** | [**SortOrder**](SortOrder.md) |  | [optional] 
**show_sidebar** | **bool** | Gets or sets a value indicating whether [show sidebar]. | [optional] 
**client** | **str** | Gets or sets the client. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.display_preferences_dto import DisplayPreferencesDto

# TODO update the JSON string below
json = "{}"
# create an instance of DisplayPreferencesDto from a JSON string
display_preferences_dto_instance = DisplayPreferencesDto.from_json(json)
# print the JSON string representation of the object
print(DisplayPreferencesDto.to_json())

# convert the object into a dict
display_preferences_dto_dict = display_preferences_dto_instance.to_dict()
# create an instance of DisplayPreferencesDto from a dict
display_preferences_dto_from_dict = DisplayPreferencesDto.from_dict(display_preferences_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


