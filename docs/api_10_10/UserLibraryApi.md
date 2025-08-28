# jellyfin.generated.api_10_10.UserLibraryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user_item_rating**](UserLibraryApi.md#delete_user_item_rating) | **DELETE** /UserItems/{itemId}/Rating | Deletes a user&#39;s saved personal rating for an item.
[**get_intros**](UserLibraryApi.md#get_intros) | **GET** /Items/{itemId}/Intros | Gets intros to play before the main media item plays.
[**get_item**](UserLibraryApi.md#get_item) | **GET** /Items/{itemId} | Gets an item from a user&#39;s library.
[**get_latest_media**](UserLibraryApi.md#get_latest_media) | **GET** /Items/Latest | Gets latest media.
[**get_local_trailers**](UserLibraryApi.md#get_local_trailers) | **GET** /Items/{itemId}/LocalTrailers | Gets local trailers for an item.
[**get_root_folder**](UserLibraryApi.md#get_root_folder) | **GET** /Items/Root | Gets the root folder from a user&#39;s library.
[**get_special_features**](UserLibraryApi.md#get_special_features) | **GET** /Items/{itemId}/SpecialFeatures | Gets special features for an item.
[**mark_favorite_item**](UserLibraryApi.md#mark_favorite_item) | **POST** /UserFavoriteItems/{itemId} | Marks an item as a favorite.
[**unmark_favorite_item**](UserLibraryApi.md#unmark_favorite_item) | **DELETE** /UserFavoriteItems/{itemId} | Unmarks item as a favorite.
[**update_user_item_rating**](UserLibraryApi.md#update_user_item_rating) | **POST** /UserItems/{itemId}/Rating | Updates a user&#39;s rating for an item.


# **delete_user_item_rating**
> UserItemDataDto delete_user_item_rating(item_id, user_id=user_id)

Deletes a user's saved personal rating for an item.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.user_item_data_dto import UserItemDataDto
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
    api_instance = jellyfin.generated.api_10_10.UserLibraryApi(api_client)
    item_id = 'item_id_example' # str | Item id.
    user_id = 'user_id_example' # str | User id. (optional)

    try:
        # Deletes a user's saved personal rating for an item.
        api_response = api_instance.delete_user_item_rating(item_id, user_id=user_id)
        print("The response of UserLibraryApi->delete_user_item_rating:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserLibraryApi->delete_user_item_rating: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item id. | 
 **user_id** | **str**| User id. | [optional] 

### Return type

[**UserItemDataDto**](UserItemDataDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Personal rating removed. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_intros**
> BaseItemDtoQueryResult get_intros(item_id, user_id=user_id)

Gets intros to play before the main media item plays.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.base_item_dto_query_result import BaseItemDtoQueryResult
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
    api_instance = jellyfin.generated.api_10_10.UserLibraryApi(api_client)
    item_id = 'item_id_example' # str | Item id.
    user_id = 'user_id_example' # str | User id. (optional)

    try:
        # Gets intros to play before the main media item plays.
        api_response = api_instance.get_intros(item_id, user_id=user_id)
        print("The response of UserLibraryApi->get_intros:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserLibraryApi->get_intros: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item id. | 
 **user_id** | **str**| User id. | [optional] 

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Intros returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item**
> BaseItemDto get_item(item_id, user_id=user_id)

Gets an item from a user's library.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.base_item_dto import BaseItemDto
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
    api_instance = jellyfin.generated.api_10_10.UserLibraryApi(api_client)
    item_id = 'item_id_example' # str | Item id.
    user_id = 'user_id_example' # str | User id. (optional)

    try:
        # Gets an item from a user's library.
        api_response = api_instance.get_item(item_id, user_id=user_id)
        print("The response of UserLibraryApi->get_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserLibraryApi->get_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item id. | 
 **user_id** | **str**| User id. | [optional] 

### Return type

[**BaseItemDto**](BaseItemDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Item returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_media**
> List[BaseItemDto] get_latest_media(user_id=user_id, parent_id=parent_id, fields=fields, include_item_types=include_item_types, is_played=is_played, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, enable_user_data=enable_user_data, limit=limit, group_items=group_items)

Gets latest media.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.base_item_dto import BaseItemDto
from jellyfin.generated.api_10_10.models.base_item_kind import BaseItemKind
from jellyfin.generated.api_10_10.models.image_type import ImageType
from jellyfin.generated.api_10_10.models.item_fields import ItemFields
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
    api_instance = jellyfin.generated.api_10_10.UserLibraryApi(api_client)
    user_id = 'user_id_example' # str | User id. (optional)
    parent_id = 'parent_id_example' # str | Specify this to localize the search to a specific item or folder. Omit to use the root. (optional)
    fields = [jellyfin.generated.api_10_10.ItemFields()] # List[ItemFields] | Optional. Specify additional fields of information to return in the output. (optional)
    include_item_types = [jellyfin.generated.api_10_10.BaseItemKind()] # List[BaseItemKind] | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited. (optional)
    is_played = True # bool | Filter by items that are played, or not. (optional)
    enable_images = True # bool | Optional. include image information in output. (optional)
    image_type_limit = 56 # int | Optional. the max number of images to return, per image type. (optional)
    enable_image_types = [jellyfin.generated.api_10_10.ImageType()] # List[ImageType] | Optional. The image types to include in the output. (optional)
    enable_user_data = True # bool | Optional. include user data. (optional)
    limit = 20 # int | Return item limit. (optional) (default to 20)
    group_items = True # bool | Whether or not to group items into a parent container. (optional) (default to True)

    try:
        # Gets latest media.
        api_response = api_instance.get_latest_media(user_id=user_id, parent_id=parent_id, fields=fields, include_item_types=include_item_types, is_played=is_played, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, enable_user_data=enable_user_data, limit=limit, group_items=group_items)
        print("The response of UserLibraryApi->get_latest_media:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserLibraryApi->get_latest_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User id. | [optional] 
 **parent_id** | **str**| Specify this to localize the search to a specific item or folder. Omit to use the root. | [optional] 
 **fields** | [**List[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. | [optional] 
 **include_item_types** | [**List[BaseItemKind]**](BaseItemKind.md)| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited. | [optional] 
 **is_played** | **bool**| Filter by items that are played, or not. | [optional] 
 **enable_images** | **bool**| Optional. include image information in output. | [optional] 
 **image_type_limit** | **int**| Optional. the max number of images to return, per image type. | [optional] 
 **enable_image_types** | [**List[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 
 **enable_user_data** | **bool**| Optional. include user data. | [optional] 
 **limit** | **int**| Return item limit. | [optional] [default to 20]
 **group_items** | **bool**| Whether or not to group items into a parent container. | [optional] [default to True]

### Return type

[**List[BaseItemDto]**](BaseItemDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Latest media returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_local_trailers**
> List[BaseItemDto] get_local_trailers(item_id, user_id=user_id)

Gets local trailers for an item.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.base_item_dto import BaseItemDto
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
    api_instance = jellyfin.generated.api_10_10.UserLibraryApi(api_client)
    item_id = 'item_id_example' # str | Item id.
    user_id = 'user_id_example' # str | User id. (optional)

    try:
        # Gets local trailers for an item.
        api_response = api_instance.get_local_trailers(item_id, user_id=user_id)
        print("The response of UserLibraryApi->get_local_trailers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserLibraryApi->get_local_trailers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item id. | 
 **user_id** | **str**| User id. | [optional] 

### Return type

[**List[BaseItemDto]**](BaseItemDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An Microsoft.AspNetCore.Mvc.OkResult containing the item&#39;s local trailers. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_root_folder**
> BaseItemDto get_root_folder(user_id=user_id)

Gets the root folder from a user's library.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.base_item_dto import BaseItemDto
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
    api_instance = jellyfin.generated.api_10_10.UserLibraryApi(api_client)
    user_id = 'user_id_example' # str | User id. (optional)

    try:
        # Gets the root folder from a user's library.
        api_response = api_instance.get_root_folder(user_id=user_id)
        print("The response of UserLibraryApi->get_root_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserLibraryApi->get_root_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User id. | [optional] 

### Return type

[**BaseItemDto**](BaseItemDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Root folder returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_special_features**
> List[BaseItemDto] get_special_features(item_id, user_id=user_id)

Gets special features for an item.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.base_item_dto import BaseItemDto
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
    api_instance = jellyfin.generated.api_10_10.UserLibraryApi(api_client)
    item_id = 'item_id_example' # str | Item id.
    user_id = 'user_id_example' # str | User id. (optional)

    try:
        # Gets special features for an item.
        api_response = api_instance.get_special_features(item_id, user_id=user_id)
        print("The response of UserLibraryApi->get_special_features:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserLibraryApi->get_special_features: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item id. | 
 **user_id** | **str**| User id. | [optional] 

### Return type

[**List[BaseItemDto]**](BaseItemDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Special features returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_favorite_item**
> UserItemDataDto mark_favorite_item(item_id, user_id=user_id)

Marks an item as a favorite.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.user_item_data_dto import UserItemDataDto
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
    api_instance = jellyfin.generated.api_10_10.UserLibraryApi(api_client)
    item_id = 'item_id_example' # str | Item id.
    user_id = 'user_id_example' # str | User id. (optional)

    try:
        # Marks an item as a favorite.
        api_response = api_instance.mark_favorite_item(item_id, user_id=user_id)
        print("The response of UserLibraryApi->mark_favorite_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserLibraryApi->mark_favorite_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item id. | 
 **user_id** | **str**| User id. | [optional] 

### Return type

[**UserItemDataDto**](UserItemDataDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Item marked as favorite. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unmark_favorite_item**
> UserItemDataDto unmark_favorite_item(item_id, user_id=user_id)

Unmarks item as a favorite.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.user_item_data_dto import UserItemDataDto
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
    api_instance = jellyfin.generated.api_10_10.UserLibraryApi(api_client)
    item_id = 'item_id_example' # str | Item id.
    user_id = 'user_id_example' # str | User id. (optional)

    try:
        # Unmarks item as a favorite.
        api_response = api_instance.unmark_favorite_item(item_id, user_id=user_id)
        print("The response of UserLibraryApi->unmark_favorite_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserLibraryApi->unmark_favorite_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item id. | 
 **user_id** | **str**| User id. | [optional] 

### Return type

[**UserItemDataDto**](UserItemDataDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Item unmarked as favorite. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_item_rating**
> UserItemDataDto update_user_item_rating(item_id, user_id=user_id, likes=likes)

Updates a user's rating for an item.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.user_item_data_dto import UserItemDataDto
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
    api_instance = jellyfin.generated.api_10_10.UserLibraryApi(api_client)
    item_id = 'item_id_example' # str | Item id.
    user_id = 'user_id_example' # str | User id. (optional)
    likes = True # bool | Whether this M:Jellyfin.Api.Controllers.UserLibraryController.UpdateUserItemRating(System.Nullable{System.Guid},System.Guid,System.Nullable{System.Boolean}) is likes. (optional)

    try:
        # Updates a user's rating for an item.
        api_response = api_instance.update_user_item_rating(item_id, user_id=user_id, likes=likes)
        print("The response of UserLibraryApi->update_user_item_rating:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserLibraryApi->update_user_item_rating: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item id. | 
 **user_id** | **str**| User id. | [optional] 
 **likes** | **bool**| Whether this M:Jellyfin.Api.Controllers.UserLibraryController.UpdateUserItemRating(System.Nullable{System.Guid},System.Guid,System.Nullable{System.Boolean}) is likes. | [optional] 

### Return type

[**UserItemDataDto**](UserItemDataDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Item rating updated. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

