# jellyfin.generated.api_10_10.PersonsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_person**](PersonsApi.md#get_person) | **GET** /Persons/{name} | Get person by name.
[**get_persons**](PersonsApi.md#get_persons) | **GET** /Persons | Gets all persons.


# **get_person**
> BaseItemDto get_person(name, user_id=user_id)

Get person by name.

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
    api_instance = jellyfin.generated.api_10_10.PersonsApi(api_client)
    name = 'name_example' # str | Person name.
    user_id = 'user_id_example' # str | Optional. Filter by user id, and attach user data. (optional)

    try:
        # Get person by name.
        api_response = api_instance.get_person(name, user_id=user_id)
        print("The response of PersonsApi->get_person:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->get_person: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Person name. | 
 **user_id** | **str**| Optional. Filter by user id, and attach user data. | [optional] 

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
**200** | Person returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Person not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_persons**
> BaseItemDtoQueryResult get_persons(limit=limit, search_term=search_term, fields=fields, filters=filters, is_favorite=is_favorite, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, exclude_person_types=exclude_person_types, person_types=person_types, appears_in_item_id=appears_in_item_id, user_id=user_id, enable_images=enable_images)

Gets all persons.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.base_item_dto_query_result import BaseItemDtoQueryResult
from jellyfin.generated.api_10_10.models.image_type import ImageType
from jellyfin.generated.api_10_10.models.item_fields import ItemFields
from jellyfin.generated.api_10_10.models.item_filter import ItemFilter
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
    api_instance = jellyfin.generated.api_10_10.PersonsApi(api_client)
    limit = 56 # int | Optional. The maximum number of records to return. (optional)
    search_term = 'search_term_example' # str | The search term. (optional)
    fields = [jellyfin.generated.api_10_10.ItemFields()] # List[ItemFields] | Optional. Specify additional fields of information to return in the output. (optional)
    filters = [jellyfin.generated.api_10_10.ItemFilter()] # List[ItemFilter] | Optional. Specify additional filters to apply. (optional)
    is_favorite = True # bool | Optional filter by items that are marked as favorite, or not. userId is required. (optional)
    enable_user_data = True # bool | Optional, include user data. (optional)
    image_type_limit = 56 # int | Optional, the max number of images to return, per image type. (optional)
    enable_image_types = [jellyfin.generated.api_10_10.ImageType()] # List[ImageType] | Optional. The image types to include in the output. (optional)
    exclude_person_types = ['exclude_person_types_example'] # List[str] | Optional. If specified results will be filtered to exclude those containing the specified PersonType. Allows multiple, comma-delimited. (optional)
    person_types = ['person_types_example'] # List[str] | Optional. If specified results will be filtered to include only those containing the specified PersonType. Allows multiple, comma-delimited. (optional)
    appears_in_item_id = 'appears_in_item_id_example' # str | Optional. If specified, person results will be filtered on items related to said persons. (optional)
    user_id = 'user_id_example' # str | User id. (optional)
    enable_images = True # bool | Optional, include image information in output. (optional) (default to True)

    try:
        # Gets all persons.
        api_response = api_instance.get_persons(limit=limit, search_term=search_term, fields=fields, filters=filters, is_favorite=is_favorite, enable_user_data=enable_user_data, image_type_limit=image_type_limit, enable_image_types=enable_image_types, exclude_person_types=exclude_person_types, person_types=person_types, appears_in_item_id=appears_in_item_id, user_id=user_id, enable_images=enable_images)
        print("The response of PersonsApi->get_persons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->get_persons: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Optional. The maximum number of records to return. | [optional] 
 **search_term** | **str**| The search term. | [optional] 
 **fields** | [**List[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. | [optional] 
 **filters** | [**List[ItemFilter]**](ItemFilter.md)| Optional. Specify additional filters to apply. | [optional] 
 **is_favorite** | **bool**| Optional filter by items that are marked as favorite, or not. userId is required. | [optional] 
 **enable_user_data** | **bool**| Optional, include user data. | [optional] 
 **image_type_limit** | **int**| Optional, the max number of images to return, per image type. | [optional] 
 **enable_image_types** | [**List[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 
 **exclude_person_types** | [**List[str]**](str.md)| Optional. If specified results will be filtered to exclude those containing the specified PersonType. Allows multiple, comma-delimited. | [optional] 
 **person_types** | [**List[str]**](str.md)| Optional. If specified results will be filtered to include only those containing the specified PersonType. Allows multiple, comma-delimited. | [optional] 
 **appears_in_item_id** | **str**| Optional. If specified, person results will be filtered on items related to said persons. | [optional] 
 **user_id** | **str**| User id. | [optional] 
 **enable_images** | **bool**| Optional, include image information in output. | [optional] [default to True]

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
**200** | Persons returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

