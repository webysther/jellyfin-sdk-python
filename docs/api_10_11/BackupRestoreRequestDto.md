# BackupRestoreRequestDto

Defines properties used to start a restore process.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive_file_name** | **str** | Gets or Sets the name of the backup archive to restore from. Must be present in MediaBrowser.Common.Configuration.IApplicationPaths.BackupPath. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.backup_restore_request_dto import BackupRestoreRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of BackupRestoreRequestDto from a JSON string
backup_restore_request_dto_instance = BackupRestoreRequestDto.from_json(json)
# print the JSON string representation of the object
print(BackupRestoreRequestDto.to_json())

# convert the object into a dict
backup_restore_request_dto_dict = backup_restore_request_dto_instance.to_dict()
# create an instance of BackupRestoreRequestDto from a dict
backup_restore_request_dto_from_dict = BackupRestoreRequestDto.from_dict(backup_restore_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


