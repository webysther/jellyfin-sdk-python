# BackupManifestDto

Manifest type for backups internal structure.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_version** | **str** | Gets or sets the jellyfin version this backup was created with. | [optional] 
**backup_engine_version** | **str** | Gets or sets the backup engine version this backup was created with. | [optional] 
**date_created** | **datetime** | Gets or sets the date this backup was created with. | [optional] 
**path** | **str** | Gets or sets the path to the backup on the system. | [optional] 
**options** | [**BackupOptionsDto**](BackupOptionsDto.md) | Gets or sets the contents of the backup archive. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.backup_manifest_dto import BackupManifestDto

# TODO update the JSON string below
json = "{}"
# create an instance of BackupManifestDto from a JSON string
backup_manifest_dto_instance = BackupManifestDto.from_json(json)
# print the JSON string representation of the object
print(BackupManifestDto.to_json())

# convert the object into a dict
backup_manifest_dto_dict = backup_manifest_dto_instance.to_dict()
# create an instance of BackupManifestDto from a dict
backup_manifest_dto_from_dict = BackupManifestDto.from_dict(backup_manifest_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


