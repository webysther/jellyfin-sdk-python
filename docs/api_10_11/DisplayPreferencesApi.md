# jellyfin.generated.api_10_11.DisplayPreferencesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_display_preferences**](DisplayPreferencesApi.md#get_display_preferences) | **GET** /DisplayPreferences/{displayPreferencesId} | Get Display Preferences.
[**update_display_preferences**](DisplayPreferencesApi.md#update_display_preferences) | **POST** /DisplayPreferences/{displayPreferencesId} | Update Display Preferences.


# **get_display_preferences**
> DisplayPreferencesDto get_display_preferences(display_preferences_id, client, user_id=user_id)

Get Display Preferences.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.display_preferences_dto import DisplayPreferencesDto
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
    api_instance = jellyfin.generated.api_10_11.DisplayPreferencesApi(api_client)
    display_preferences_id = 'display_preferences_id_example' # str | Display preferences id.
    client = 'client_example' # str | Client.
    user_id = 'user_id_example' # str | User id. (optional)

    try:
        # Get Display Preferences.
        api_response = api_instance.get_display_preferences(display_preferences_id, client, user_id=user_id)
        print("The response of DisplayPreferencesApi->get_display_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisplayPreferencesApi->get_display_preferences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_preferences_id** | **str**| Display preferences id. | 
 **client** | **str**| Client. | 
 **user_id** | **str**| User id. | [optional] 

### Return type

[**DisplayPreferencesDto**](DisplayPreferencesDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Display preferences retrieved. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_display_preferences**
> update_display_preferences(display_preferences_id, client, display_preferences_dto, user_id=user_id)

Update Display Preferences.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.display_preferences_dto import DisplayPreferencesDto
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
    api_instance = jellyfin.generated.api_10_11.DisplayPreferencesApi(api_client)
    display_preferences_id = 'display_preferences_id_example' # str | Display preferences id.
    client = 'client_example' # str | Client.
    display_preferences_dto = jellyfin.generated.api_10_11.DisplayPreferencesDto() # DisplayPreferencesDto | New Display Preferences object.
    user_id = 'user_id_example' # str | User Id. (optional)

    try:
        # Update Display Preferences.
        api_instance.update_display_preferences(display_preferences_id, client, display_preferences_dto, user_id=user_id)
    except Exception as e:
        print("Exception when calling DisplayPreferencesApi->update_display_preferences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_preferences_id** | **str**| Display preferences id. | 
 **client** | **str**| Client. | 
 **display_preferences_dto** | [**DisplayPreferencesDto**](DisplayPreferencesDto.md)| New Display Preferences object. | 
 **user_id** | **str**| User Id. | [optional] 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Display preferences updated. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

