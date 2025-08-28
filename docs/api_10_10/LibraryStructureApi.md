# jellyfin.generated.api_10_10.LibraryStructureApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_media_path**](LibraryStructureApi.md#add_media_path) | **POST** /Library/VirtualFolders/Paths | Add a media path to a library.
[**add_virtual_folder**](LibraryStructureApi.md#add_virtual_folder) | **POST** /Library/VirtualFolders | Adds a virtual folder.
[**get_virtual_folders**](LibraryStructureApi.md#get_virtual_folders) | **GET** /Library/VirtualFolders | Gets all virtual folders.
[**remove_media_path**](LibraryStructureApi.md#remove_media_path) | **DELETE** /Library/VirtualFolders/Paths | Remove a media path.
[**remove_virtual_folder**](LibraryStructureApi.md#remove_virtual_folder) | **DELETE** /Library/VirtualFolders | Removes a virtual folder.
[**rename_virtual_folder**](LibraryStructureApi.md#rename_virtual_folder) | **POST** /Library/VirtualFolders/Name | Renames a virtual folder.
[**update_library_options**](LibraryStructureApi.md#update_library_options) | **POST** /Library/VirtualFolders/LibraryOptions | Update library options.
[**update_media_path**](LibraryStructureApi.md#update_media_path) | **POST** /Library/VirtualFolders/Paths/Update | Updates a media path.


# **add_media_path**
> add_media_path(media_path_dto, refresh_library=refresh_library)

Add a media path to a library.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.media_path_dto import MediaPathDto
from jellyfin.generated.api_10_10.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jellyfin.generated.api_10_10.Configuration(
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
with jellyfin.generated.api_10_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jellyfin.generated.api_10_10.LibraryStructureApi(api_client)
    media_path_dto = jellyfin.generated.api_10_10.MediaPathDto() # MediaPathDto | The media path dto.
    refresh_library = False # bool | Whether to refresh the library. (optional) (default to False)

    try:
        # Add a media path to a library.
        api_instance.add_media_path(media_path_dto, refresh_library=refresh_library)
    except Exception as e:
        print("Exception when calling LibraryStructureApi->add_media_path: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_path_dto** | [**MediaPathDto**](MediaPathDto.md)| The media path dto. | 
 **refresh_library** | **bool**| Whether to refresh the library. | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Media path added. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_virtual_folder**
> add_virtual_folder(name=name, collection_type=collection_type, paths=paths, refresh_library=refresh_library, add_virtual_folder_dto=add_virtual_folder_dto)

Adds a virtual folder.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.add_virtual_folder_dto import AddVirtualFolderDto
from jellyfin.generated.api_10_10.models.collection_type_options import CollectionTypeOptions
from jellyfin.generated.api_10_10.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jellyfin.generated.api_10_10.Configuration(
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
with jellyfin.generated.api_10_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jellyfin.generated.api_10_10.LibraryStructureApi(api_client)
    name = 'name_example' # str | The name of the virtual folder. (optional)
    collection_type = jellyfin.generated.api_10_10.CollectionTypeOptions() # CollectionTypeOptions | The type of the collection. (optional)
    paths = ['paths_example'] # List[str] | The paths of the virtual folder. (optional)
    refresh_library = False # bool | Whether to refresh the library. (optional) (default to False)
    add_virtual_folder_dto = jellyfin.generated.api_10_10.AddVirtualFolderDto() # AddVirtualFolderDto | The library options. (optional)

    try:
        # Adds a virtual folder.
        api_instance.add_virtual_folder(name=name, collection_type=collection_type, paths=paths, refresh_library=refresh_library, add_virtual_folder_dto=add_virtual_folder_dto)
    except Exception as e:
        print("Exception when calling LibraryStructureApi->add_virtual_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the virtual folder. | [optional] 
 **collection_type** | [**CollectionTypeOptions**](.md)| The type of the collection. | [optional] 
 **paths** | [**List[str]**](str.md)| The paths of the virtual folder. | [optional] 
 **refresh_library** | **bool**| Whether to refresh the library. | [optional] [default to False]
 **add_virtual_folder_dto** | [**AddVirtualFolderDto**](AddVirtualFolderDto.md)| The library options. | [optional] 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Folder added. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_folders**
> List[VirtualFolderInfo] get_virtual_folders()

Gets all virtual folders.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.virtual_folder_info import VirtualFolderInfo
from jellyfin.generated.api_10_10.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jellyfin.generated.api_10_10.Configuration(
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
with jellyfin.generated.api_10_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jellyfin.generated.api_10_10.LibraryStructureApi(api_client)

    try:
        # Gets all virtual folders.
        api_response = api_instance.get_virtual_folders()
        print("The response of LibraryStructureApi->get_virtual_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibraryStructureApi->get_virtual_folders: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[VirtualFolderInfo]**](VirtualFolderInfo.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Virtual folders retrieved. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_media_path**
> remove_media_path(name=name, path=path, refresh_library=refresh_library)

Remove a media path.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jellyfin.generated.api_10_10.Configuration(
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
with jellyfin.generated.api_10_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jellyfin.generated.api_10_10.LibraryStructureApi(api_client)
    name = 'name_example' # str | The name of the library. (optional)
    path = 'path_example' # str | The path to remove. (optional)
    refresh_library = False # bool | Whether to refresh the library. (optional) (default to False)

    try:
        # Remove a media path.
        api_instance.remove_media_path(name=name, path=path, refresh_library=refresh_library)
    except Exception as e:
        print("Exception when calling LibraryStructureApi->remove_media_path: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the library. | [optional] 
 **path** | **str**| The path to remove. | [optional] 
 **refresh_library** | **bool**| Whether to refresh the library. | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Media path removed. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_virtual_folder**
> remove_virtual_folder(name=name, refresh_library=refresh_library)

Removes a virtual folder.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jellyfin.generated.api_10_10.Configuration(
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
with jellyfin.generated.api_10_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jellyfin.generated.api_10_10.LibraryStructureApi(api_client)
    name = 'name_example' # str | The name of the folder. (optional)
    refresh_library = False # bool | Whether to refresh the library. (optional) (default to False)

    try:
        # Removes a virtual folder.
        api_instance.remove_virtual_folder(name=name, refresh_library=refresh_library)
    except Exception as e:
        print("Exception when calling LibraryStructureApi->remove_virtual_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the folder. | [optional] 
 **refresh_library** | **bool**| Whether to refresh the library. | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Folder removed. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_virtual_folder**
> rename_virtual_folder(name=name, new_name=new_name, refresh_library=refresh_library)

Renames a virtual folder.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jellyfin.generated.api_10_10.Configuration(
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
with jellyfin.generated.api_10_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jellyfin.generated.api_10_10.LibraryStructureApi(api_client)
    name = 'name_example' # str | The name of the virtual folder. (optional)
    new_name = 'new_name_example' # str | The new name. (optional)
    refresh_library = False # bool | Whether to refresh the library. (optional) (default to False)

    try:
        # Renames a virtual folder.
        api_instance.rename_virtual_folder(name=name, new_name=new_name, refresh_library=refresh_library)
    except Exception as e:
        print("Exception when calling LibraryStructureApi->rename_virtual_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the virtual folder. | [optional] 
 **new_name** | **str**| The new name. | [optional] 
 **refresh_library** | **bool**| Whether to refresh the library. | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Folder renamed. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Library doesn&#39;t exist. |  -  |
**409** | Library already exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_library_options**
> update_library_options(update_library_options_dto=update_library_options_dto)

Update library options.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.update_library_options_dto import UpdateLibraryOptionsDto
from jellyfin.generated.api_10_10.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jellyfin.generated.api_10_10.Configuration(
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
with jellyfin.generated.api_10_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jellyfin.generated.api_10_10.LibraryStructureApi(api_client)
    update_library_options_dto = jellyfin.generated.api_10_10.UpdateLibraryOptionsDto() # UpdateLibraryOptionsDto | The library name and options. (optional)

    try:
        # Update library options.
        api_instance.update_library_options(update_library_options_dto=update_library_options_dto)
    except Exception as e:
        print("Exception when calling LibraryStructureApi->update_library_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_library_options_dto** | [**UpdateLibraryOptionsDto**](UpdateLibraryOptionsDto.md)| The library name and options. | [optional] 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Library updated. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Item not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_media_path**
> update_media_path(update_media_path_request_dto)

Updates a media path.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.update_media_path_request_dto import UpdateMediaPathRequestDto
from jellyfin.generated.api_10_10.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jellyfin.generated.api_10_10.Configuration(
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
with jellyfin.generated.api_10_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jellyfin.generated.api_10_10.LibraryStructureApi(api_client)
    update_media_path_request_dto = jellyfin.generated.api_10_10.UpdateMediaPathRequestDto() # UpdateMediaPathRequestDto | The name of the library and path infos.

    try:
        # Updates a media path.
        api_instance.update_media_path(update_media_path_request_dto)
    except Exception as e:
        print("Exception when calling LibraryStructureApi->update_media_path: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_media_path_request_dto** | [**UpdateMediaPathRequestDto**](UpdateMediaPathRequestDto.md)| The name of the library and path infos. | 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Media path updated. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

