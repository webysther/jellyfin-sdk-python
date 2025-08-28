# jellyfin.generated.api_10_11.BackupApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_backup**](BackupApi.md#create_backup) | **POST** /Backup/Create | Creates a new Backup.
[**get_backup**](BackupApi.md#get_backup) | **GET** /Backup/Manifest | Gets the descriptor from an existing archive is present.
[**list_backups**](BackupApi.md#list_backups) | **GET** /Backup | Gets a list of all currently present backups in the backup directory.
[**start_restore_backup**](BackupApi.md#start_restore_backup) | **POST** /Backup/Restore | Restores to a backup by restarting the server and applying the backup.


# **create_backup**
> BackupManifestDto create_backup(backup_options_dto=backup_options_dto)

Creates a new Backup.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.backup_manifest_dto import BackupManifestDto
from jellyfin.generated.api_10_11.models.backup_options_dto import BackupOptionsDto
from jellyfin.generated.api_10_11.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jellyfin.generated.api_10_11.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: CustomAuthentication
configuration.api_key['CustomAuthentication'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CustomAuthentication'] = 'Bearer'

# Enter a context with an instance of the API client
with jellyfin.generated.api_10_11.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jellyfin.generated.api_10_11.BackupApi(api_client)
    backup_options_dto = jellyfin.generated.api_10_11.BackupOptionsDto() # BackupOptionsDto | The backup options. (optional)

    try:
        # Creates a new Backup.
        api_response = api_instance.create_backup(backup_options_dto=backup_options_dto)
        print("The response of BackupApi->create_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupApi->create_backup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup_options_dto** | [**BackupOptionsDto**](BackupOptionsDto.md)| The backup options. | [optional] 

### Return type

[**BackupManifestDto**](BackupManifestDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Backup created. |  -  |
**403** | User does not have permission to retrieve information. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backup**
> BackupManifestDto get_backup(path)

Gets the descriptor from an existing archive is present.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.backup_manifest_dto import BackupManifestDto
from jellyfin.generated.api_10_11.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jellyfin.generated.api_10_11.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: CustomAuthentication
configuration.api_key['CustomAuthentication'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CustomAuthentication'] = 'Bearer'

# Enter a context with an instance of the API client
with jellyfin.generated.api_10_11.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jellyfin.generated.api_10_11.BackupApi(api_client)
    path = 'path_example' # str | The data to start a restore process.

    try:
        # Gets the descriptor from an existing archive is present.
        api_response = api_instance.get_backup(path)
        print("The response of BackupApi->get_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupApi->get_backup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The data to start a restore process. | 

### Return type

[**BackupManifestDto**](BackupManifestDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Backup archive manifest. |  -  |
**204** | Not a valid jellyfin Archive. |  -  |
**404** | Not a valid path. |  -  |
**403** | User does not have permission to retrieve information. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_backups**
> List[BackupManifestDto] list_backups()

Gets a list of all currently present backups in the backup directory.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.backup_manifest_dto import BackupManifestDto
from jellyfin.generated.api_10_11.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jellyfin.generated.api_10_11.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: CustomAuthentication
configuration.api_key['CustomAuthentication'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CustomAuthentication'] = 'Bearer'

# Enter a context with an instance of the API client
with jellyfin.generated.api_10_11.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jellyfin.generated.api_10_11.BackupApi(api_client)

    try:
        # Gets a list of all currently present backups in the backup directory.
        api_response = api_instance.list_backups()
        print("The response of BackupApi->list_backups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupApi->list_backups: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[BackupManifestDto]**](BackupManifestDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Backups available. |  -  |
**403** | User does not have permission to retrieve information. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_restore_backup**
> start_restore_backup(backup_restore_request_dto)

Restores to a backup by restarting the server and applying the backup.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.backup_restore_request_dto import BackupRestoreRequestDto
from jellyfin.generated.api_10_11.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jellyfin.generated.api_10_11.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: CustomAuthentication
configuration.api_key['CustomAuthentication'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CustomAuthentication'] = 'Bearer'

# Enter a context with an instance of the API client
with jellyfin.generated.api_10_11.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jellyfin.generated.api_10_11.BackupApi(api_client)
    backup_restore_request_dto = jellyfin.generated.api_10_11.BackupRestoreRequestDto() # BackupRestoreRequestDto | The data to start a restore process.

    try:
        # Restores to a backup by restarting the server and applying the backup.
        api_instance.start_restore_backup(backup_restore_request_dto)
    except Exception as e:
        print("Exception when calling BackupApi->start_restore_backup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup_restore_request_dto** | [**BackupRestoreRequestDto**](BackupRestoreRequestDto.md)| The data to start a restore process. | 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Backup restore started. |  -  |
**404** | Not Found |  -  |
**403** | User does not have permission to retrieve information. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

