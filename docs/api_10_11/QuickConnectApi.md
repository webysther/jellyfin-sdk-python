# jellyfin.generated.api_10_11.QuickConnectApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize_quick_connect**](QuickConnectApi.md#authorize_quick_connect) | **POST** /QuickConnect/Authorize | Authorizes a pending quick connect request.
[**get_quick_connect_enabled**](QuickConnectApi.md#get_quick_connect_enabled) | **GET** /QuickConnect/Enabled | Gets the current quick connect state.
[**get_quick_connect_state**](QuickConnectApi.md#get_quick_connect_state) | **GET** /QuickConnect/Connect | Attempts to retrieve authentication information.
[**initiate_quick_connect**](QuickConnectApi.md#initiate_quick_connect) | **POST** /QuickConnect/Initiate | Initiate a new quick connect request.


# **authorize_quick_connect**
> bool authorize_quick_connect(code, user_id=user_id)

Authorizes a pending quick connect request.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
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
    api_instance = jellyfin.generated.api_10_11.QuickConnectApi(api_client)
    code = 'code_example' # str | Quick connect code to authorize.
    user_id = 'user_id_example' # str | The user the authorize. Access to the requested user is required. (optional)

    try:
        # Authorizes a pending quick connect request.
        api_response = api_instance.authorize_quick_connect(code, user_id=user_id)
        print("The response of QuickConnectApi->authorize_quick_connect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuickConnectApi->authorize_quick_connect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Quick connect code to authorize. | 
 **user_id** | **str**| The user the authorize. Access to the requested user is required. | [optional] 

### Return type

**bool**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Quick connect result authorized successfully. |  -  |
**403** | Unknown user id. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quick_connect_enabled**
> bool get_quick_connect_enabled()

Gets the current quick connect state.

### Example


```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jellyfin.generated.api_10_11.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with jellyfin.generated.api_10_11.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jellyfin.generated.api_10_11.QuickConnectApi(api_client)

    try:
        # Gets the current quick connect state.
        api_response = api_instance.get_quick_connect_enabled()
        print("The response of QuickConnectApi->get_quick_connect_enabled:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuickConnectApi->get_quick_connect_enabled: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Quick connect state returned. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quick_connect_state**
> QuickConnectResult get_quick_connect_state(secret)

Attempts to retrieve authentication information.

### Example


```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.quick_connect_result import QuickConnectResult
from jellyfin.generated.api_10_11.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jellyfin.generated.api_10_11.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with jellyfin.generated.api_10_11.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jellyfin.generated.api_10_11.QuickConnectApi(api_client)
    secret = 'secret_example' # str | Secret previously returned from the Initiate endpoint.

    try:
        # Attempts to retrieve authentication information.
        api_response = api_instance.get_quick_connect_state(secret)
        print("The response of QuickConnectApi->get_quick_connect_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuickConnectApi->get_quick_connect_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret** | **str**| Secret previously returned from the Initiate endpoint. | 

### Return type

[**QuickConnectResult**](QuickConnectResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Quick connect result returned. |  -  |
**404** | Unknown quick connect secret. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initiate_quick_connect**
> QuickConnectResult initiate_quick_connect()

Initiate a new quick connect request.

### Example


```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.quick_connect_result import QuickConnectResult
from jellyfin.generated.api_10_11.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jellyfin.generated.api_10_11.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with jellyfin.generated.api_10_11.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jellyfin.generated.api_10_11.QuickConnectApi(api_client)

    try:
        # Initiate a new quick connect request.
        api_response = api_instance.initiate_quick_connect()
        print("The response of QuickConnectApi->initiate_quick_connect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuickConnectApi->initiate_quick_connect: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**QuickConnectResult**](QuickConnectResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Quick connect request successfully created. |  -  |
**401** | Quick connect is not active on this server. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

