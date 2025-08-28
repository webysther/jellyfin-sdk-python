# jellyfin.generated.api_10_10.TimeSyncApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_utc_time**](TimeSyncApi.md#get_utc_time) | **GET** /GetUtcTime | Gets the current UTC time.


# **get_utc_time**
> UtcTimeResponse get_utc_time()

Gets the current UTC time.

### Example


```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.utc_time_response import UtcTimeResponse
from jellyfin.generated.api_10_10.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jellyfin.generated.api_10_10.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with jellyfin.generated.api_10_10.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jellyfin.generated.api_10_10.TimeSyncApi(api_client)

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
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Time returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

