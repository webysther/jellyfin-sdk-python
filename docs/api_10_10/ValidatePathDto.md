# ValidatePathDto

Validate path object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validate_writable** | **bool** | Gets or sets a value indicating whether validate if path is writable. | [optional] 
**path** | **str** | Gets or sets the path. | [optional] 
**is_file** | **bool** | Gets or sets is path file. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.validate_path_dto import ValidatePathDto

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatePathDto from a JSON string
validate_path_dto_instance = ValidatePathDto.from_json(json)
# print the JSON string representation of the object
print(ValidatePathDto.to_json())

# convert the object into a dict
validate_path_dto_dict = validate_path_dto_instance.to_dict()
# create an instance of ValidatePathDto from a dict
validate_path_dto_from_dict = ValidatePathDto.from_dict(validate_path_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


