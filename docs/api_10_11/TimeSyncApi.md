# jellyfin.generated.api_10_11.TimeSyncApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_utc_time**](TimeSyncApi.md#get_utc_time) | **GET** /GetUtcTime | Gets the current UTC time.


# **get_utc_time**
> UtcTimeResponse get_utc_time()

Gets the current UTC time.

### Example


```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.utc_time_response import UtcTimeResponse
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
    api_instance = jellyfin.generated.api_10_11.TimeSyncApi(api_client)

    try:
        # Gets the current UTC time.
        api_response = api_instance.get_utc_time()
        print("The response of TimeSyncApi->get_utc_time:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeSyncApi->get_utc_time: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UtcTimeResponse**](UtcTimeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Time returned. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

