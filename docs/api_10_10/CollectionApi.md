# jellyfin.generated.api_10_10.CollectionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_to_collection**](CollectionApi.md#add_to_collection) | **POST** /Collections/{collectionId}/Items | Adds items to a collection.
[**create_collection**](CollectionApi.md#create_collection) | **POST** /Collections | Creates a new collection.
[**remove_from_collection**](CollectionApi.md#remove_from_collection) | **DELETE** /Collections/{collectionId}/Items | Removes items from a collection.


# **add_to_collection**
> add_to_collection(collection_id, ids)

Adds items to a collection.

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
    api_instance = jellyfin.generated.api_10_10.CollectionApi(api_client)
    collection_id = 'collection_id_example' # str | The collection id.
    ids = ['ids_example'] # List[str] | Item ids, comma delimited.

    try:
        # Adds items to a collection.
        api_instance.add_to_collection(collection_id, ids)
    except Exception as e:
        print("Exception when calling CollectionApi->add_to_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection id. | 
 **ids** | [**List[str]**](str.md)| Item ids, comma delimited. | 

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
**204** | Items added to collection. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_collection**
> CollectionCreationResult create_collection(name=name, ids=ids, parent_id=parent_id, is_locked=is_locked)

Creates a new collection.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.collection_creation_result import CollectionCreationResult
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
    api_instance = jellyfin.generated.api_10_10.CollectionApi(api_client)
    name = 'name_example' # str | The name of the collection. (optional)
    ids = ['ids_example'] # List[str] | Item Ids to add to the collection. (optional)
    parent_id = 'parent_id_example' # str | Optional. Create the collection within a specific folder. (optional)
    is_locked = False # bool | Whether or not to lock the new collection. (optional) (default to False)

    try:
        # Creates a new collection.
        api_response = api_instance.create_collection(name=name, ids=ids, parent_id=parent_id, is_locked=is_locked)
        print("The response of CollectionApi->create_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->create_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the collection. | [optional] 
 **ids** | [**List[str]**](str.md)| Item Ids to add to the collection. | [optional] 
 **parent_id** | **str**| Optional. Create the collection within a specific folder. | [optional] 
 **is_locked** | **bool**| Whether or not to lock the new collection. | [optional] [default to False]

### Return type

[**CollectionCreationResult**](CollectionCreationResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Collection created. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_from_collection**
> remove_from_collection(collection_id, ids)

Removes items from a collection.

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
    api_instance = jellyfin.generated.api_10_10.CollectionApi(api_client)
    collection_id = 'collection_id_example' # str | The collection id.
    ids = ['ids_example'] # List[str] | Item ids, comma delimited.

    try:
        # Removes items from a collection.
        api_instance.remove_from_collection(collection_id, ids)
    except Exception as e:
        print("Exception when calling CollectionApi->remove_from_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection id. | 
 **ids** | [**List[str]**](str.md)| Item ids, comma delimited. | 

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
**204** | Items removed from collection. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

