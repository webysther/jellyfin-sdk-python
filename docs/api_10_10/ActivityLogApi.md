# jellyfin.generated.api_10_10.ActivityLogApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_log_entries**](ActivityLogApi.md#get_log_entries) | **GET** /System/ActivityLog/Entries | Gets activity log entries.


# **get_log_entries**
> ActivityLogEntryQueryResult get_log_entries(start_index=start_index, limit=limit, min_date=min_date, has_user_id=has_user_id)

Gets activity log entries.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.activity_log_entry_query_result import ActivityLogEntryQueryResult
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
    api_instance = jellyfin.generated.api_10_10.ActivityLogApi(api_client)
    start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
    limit = 56 # int | Optional. The maximum number of records to return. (optional)
    min_date = '2013-10-20T19:20:30+01:00' # datetime | Optional. The minimum date. Format = ISO. (optional)
    has_user_id = True # bool | Optional. Filter log entries if it has user id, or not. (optional)

    try:
        # Gets activity log entries.
        api_response = api_instance.get_log_entries(start_index=start_index, limit=limit, min_date=min_date, has_user_id=has_user_id)
        print("The response of ActivityLogApi->get_log_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityLogApi->get_log_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return. | [optional] 
 **min_date** | **datetime**| Optional. The minimum date. Format &#x3D; ISO. | [optional] 
 **has_user_id** | **bool**| Optional. Filter log entries if it has user id, or not. | [optional] 

### Return type

[**ActivityLogEntryQueryResult**](ActivityLogEntryQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Activity log returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

