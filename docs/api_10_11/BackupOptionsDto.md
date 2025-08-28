# BackupOptionsDto

Defines the optional contents of the backup archive.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **bool** | Gets or sets a value indicating whether the archive contains the Metadata contents. | [optional] 
**trickplay** | **bool** | Gets or sets a value indicating whether the archive contains the Trickplay contents. | [optional] 
**subtitles** | **bool** | Gets or sets a value indicating whether the archive contains the Subtitle contents. | [optional] 
**database** | **bool** | Gets or sets a value indicating whether the archive contains the Database contents. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.backup_options_dto import BackupOptionsDto

# TODO update the JSON string below
json = "{}"
# create an instance of BackupOptionsDto from a JSON string
backup_options_dto_instance = BackupOptionsDto.from_json(json)
# print the JSON string representation of the object
print(BackupOptionsDto.to_json())

# convert the object into a dict
backup_options_dto_dict = backup_options_dto_instance.to_dict()
# create an instance of BackupOptionsDto from a dict
backup_options_dto_from_dict = BackupOptionsDto.from_dict(backup_options_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


