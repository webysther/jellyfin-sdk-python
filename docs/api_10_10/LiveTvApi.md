# jellyfin.generated.api_10_10.LiveTvApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_listing_provider**](LiveTvApi.md#add_listing_provider) | **POST** /LiveTv/ListingProviders | Adds a listings provider.
[**add_tuner_host**](LiveTvApi.md#add_tuner_host) | **POST** /LiveTv/TunerHosts | Adds a tuner host.
[**cancel_series_timer**](LiveTvApi.md#cancel_series_timer) | **DELETE** /LiveTv/SeriesTimers/{timerId} | Cancels a live tv series timer.
[**cancel_timer**](LiveTvApi.md#cancel_timer) | **DELETE** /LiveTv/Timers/{timerId} | Cancels a live tv timer.
[**create_series_timer**](LiveTvApi.md#create_series_timer) | **POST** /LiveTv/SeriesTimers | Creates a live tv series timer.
[**create_timer**](LiveTvApi.md#create_timer) | **POST** /LiveTv/Timers | Creates a live tv timer.
[**delete_listing_provider**](LiveTvApi.md#delete_listing_provider) | **DELETE** /LiveTv/ListingProviders | Delete listing provider.
[**delete_recording**](LiveTvApi.md#delete_recording) | **DELETE** /LiveTv/Recordings/{recordingId} | Deletes a live tv recording.
[**delete_tuner_host**](LiveTvApi.md#delete_tuner_host) | **DELETE** /LiveTv/TunerHosts | Deletes a tuner host.
[**discover_tuners**](LiveTvApi.md#discover_tuners) | **GET** /LiveTv/Tuners/Discover | Discover tuners.
[**discvover_tuners**](LiveTvApi.md#discvover_tuners) | **GET** /LiveTv/Tuners/Discvover | Discover tuners.
[**get_channel**](LiveTvApi.md#get_channel) | **GET** /LiveTv/Channels/{channelId} | Gets a live tv channel.
[**get_channel_mapping_options**](LiveTvApi.md#get_channel_mapping_options) | **GET** /LiveTv/ChannelMappingOptions | Get channel mapping options.
[**get_default_listing_provider**](LiveTvApi.md#get_default_listing_provider) | **GET** /LiveTv/ListingProviders/Default | Gets default listings provider info.
[**get_default_timer**](LiveTvApi.md#get_default_timer) | **GET** /LiveTv/Timers/Defaults | Gets the default values for a new timer.
[**get_guide_info**](LiveTvApi.md#get_guide_info) | **GET** /LiveTv/GuideInfo | Get guid info.
[**get_lineups**](LiveTvApi.md#get_lineups) | **GET** /LiveTv/ListingProviders/Lineups | Gets available lineups.
[**get_live_recording_file**](LiveTvApi.md#get_live_recording_file) | **GET** /LiveTv/LiveRecordings/{recordingId}/stream | Gets a live tv recording stream.
[**get_live_stream_file**](LiveTvApi.md#get_live_stream_file) | **GET** /LiveTv/LiveStreamFiles/{streamId}/stream.{container} | Gets a live tv channel stream.
[**get_live_tv_channels**](LiveTvApi.md#get_live_tv_channels) | **GET** /LiveTv/Channels | Gets available live tv channels.
[**get_live_tv_info**](LiveTvApi.md#get_live_tv_info) | **GET** /LiveTv/Info | Gets available live tv services.
[**get_live_tv_programs**](LiveTvApi.md#get_live_tv_programs) | **GET** /LiveTv/Programs | Gets available live tv epgs.
[**get_program**](LiveTvApi.md#get_program) | **GET** /LiveTv/Programs/{programId} | Gets a live tv program.
[**get_programs**](LiveTvApi.md#get_programs) | **POST** /LiveTv/Programs | Gets available live tv epgs.
[**get_recommended_programs**](LiveTvApi.md#get_recommended_programs) | **GET** /LiveTv/Programs/Recommended | Gets recommended live tv epgs.
[**get_recording**](LiveTvApi.md#get_recording) | **GET** /LiveTv/Recordings/{recordingId} | Gets a live tv recording.
[**get_recording_folders**](LiveTvApi.md#get_recording_folders) | **GET** /LiveTv/Recordings/Folders | Gets recording folders.
[**get_recording_group**](LiveTvApi.md#get_recording_group) | **GET** /LiveTv/Recordings/Groups/{groupId} | Get recording group.
[**get_recording_groups**](LiveTvApi.md#get_recording_groups) | **GET** /LiveTv/Recordings/Groups | Gets live tv recording groups.
[**get_recordings**](LiveTvApi.md#get_recordings) | **GET** /LiveTv/Recordings | Gets live tv recordings.
[**get_recordings_series**](LiveTvApi.md#get_recordings_series) | **GET** /LiveTv/Recordings/Series | Gets live tv recording series.
[**get_schedules_direct_countries**](LiveTvApi.md#get_schedules_direct_countries) | **GET** /LiveTv/ListingProviders/SchedulesDirect/Countries | Gets available countries.
[**get_series_timer**](LiveTvApi.md#get_series_timer) | **GET** /LiveTv/SeriesTimers/{timerId} | Gets a live tv series timer.
[**get_series_timers**](LiveTvApi.md#get_series_timers) | **GET** /LiveTv/SeriesTimers | Gets live tv series timers.
[**get_timer**](LiveTvApi.md#get_timer) | **GET** /LiveTv/Timers/{timerId} | Gets a timer.
[**get_timers**](LiveTvApi.md#get_timers) | **GET** /LiveTv/Timers | Gets the live tv timers.
[**get_tuner_host_types**](LiveTvApi.md#get_tuner_host_types) | **GET** /LiveTv/TunerHosts/Types | Get tuner host types.
[**reset_tuner**](LiveTvApi.md#reset_tuner) | **POST** /LiveTv/Tuners/{tunerId}/Reset | Resets a tv tuner.
[**set_channel_mapping**](LiveTvApi.md#set_channel_mapping) | **POST** /LiveTv/ChannelMappings | Set channel mappings.
[**update_series_timer**](LiveTvApi.md#update_series_timer) | **POST** /LiveTv/SeriesTimers/{timerId} | Updates a live tv series timer.
[**update_timer**](LiveTvApi.md#update_timer) | **POST** /LiveTv/Timers/{timerId} | Updates a live tv timer.


# **add_listing_provider**
> ListingsProviderInfo add_listing_provider(pw=pw, validate_listings=validate_listings, validate_login=validate_login, listings_provider_info=listings_provider_info)

Adds a listings provider.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.listings_provider_info import ListingsProviderInfo
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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    pw = 'pw_example' # str | Password. (optional)
    validate_listings = False # bool | Validate listings. (optional) (default to False)
    validate_login = False # bool | Validate login. (optional) (default to False)
    listings_provider_info = jellyfin.generated.api_10_10.ListingsProviderInfo() # ListingsProviderInfo | New listings info. (optional)

    try:
        # Adds a listings provider.
        api_response = api_instance.add_listing_provider(pw=pw, validate_listings=validate_listings, validate_login=validate_login, listings_provider_info=listings_provider_info)
        print("The response of LiveTvApi->add_listing_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvApi->add_listing_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pw** | **str**| Password. | [optional] 
 **validate_listings** | **bool**| Validate listings. | [optional] [default to False]
 **validate_login** | **bool**| Validate login. | [optional] [default to False]
 **listings_provider_info** | [**ListingsProviderInfo**](ListingsProviderInfo.md)| New listings info. | [optional] 

### Return type

[**ListingsProviderInfo**](ListingsProviderInfo.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created listings provider returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_tuner_host**
> TunerHostInfo add_tuner_host(tuner_host_info=tuner_host_info)

Adds a tuner host.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.tuner_host_info import TunerHostInfo
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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    tuner_host_info = jellyfin.generated.api_10_10.TunerHostInfo() # TunerHostInfo | New tuner host. (optional)

    try:
        # Adds a tuner host.
        api_response = api_instance.add_tuner_host(tuner_host_info=tuner_host_info)
        print("The response of LiveTvApi->add_tuner_host:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvApi->add_tuner_host: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tuner_host_info** | [**TunerHostInfo**](TunerHostInfo.md)| New tuner host. | [optional] 

### Return type

[**TunerHostInfo**](TunerHostInfo.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created tuner host returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_series_timer**
> cancel_series_timer(timer_id)

Cancels a live tv series timer.

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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    timer_id = 'timer_id_example' # str | Timer id.

    try:
        # Cancels a live tv series timer.
        api_instance.cancel_series_timer(timer_id)
    except Exception as e:
        print("Exception when calling LiveTvApi->cancel_series_timer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timer_id** | **str**| Timer id. | 

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
**204** | Timer cancelled. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_timer**
> cancel_timer(timer_id)

Cancels a live tv timer.

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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    timer_id = 'timer_id_example' # str | Timer id.

    try:
        # Cancels a live tv timer.
        api_instance.cancel_timer(timer_id)
    except Exception as e:
        print("Exception when calling LiveTvApi->cancel_timer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timer_id** | **str**| Timer id. | 

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
**204** | Timer deleted. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_series_timer**
> create_series_timer(series_timer_info_dto=series_timer_info_dto)

Creates a live tv series timer.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.series_timer_info_dto import SeriesTimerInfoDto
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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    series_timer_info_dto = jellyfin.generated.api_10_10.SeriesTimerInfoDto() # SeriesTimerInfoDto | New series timer info. (optional)

    try:
        # Creates a live tv series timer.
        api_instance.create_series_timer(series_timer_info_dto=series_timer_info_dto)
    except Exception as e:
        print("Exception when calling LiveTvApi->create_series_timer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_timer_info_dto** | [**SeriesTimerInfoDto**](SeriesTimerInfoDto.md)| New series timer info. | [optional] 

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
**204** | Series timer info created. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_timer**
> create_timer(timer_info_dto=timer_info_dto)

Creates a live tv timer.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.timer_info_dto import TimerInfoDto
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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    timer_info_dto = jellyfin.generated.api_10_10.TimerInfoDto() # TimerInfoDto | New timer info. (optional)

    try:
        # Creates a live tv timer.
        api_instance.create_timer(timer_info_dto=timer_info_dto)
    except Exception as e:
        print("Exception when calling LiveTvApi->create_timer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timer_info_dto** | [**TimerInfoDto**](TimerInfoDto.md)| New timer info. | [optional] 

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
**204** | Timer created. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_listing_provider**
> delete_listing_provider(id=id)

Delete listing provider.

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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    id = 'id_example' # str | Listing provider id. (optional)

    try:
        # Delete listing provider.
        api_instance.delete_listing_provider(id=id)
    except Exception as e:
        print("Exception when calling LiveTvApi->delete_listing_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Listing provider id. | [optional] 

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
**204** | Listing provider deleted. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_recording**
> delete_recording(recording_id)

Deletes a live tv recording.

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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    recording_id = 'recording_id_example' # str | Recording id.

    try:
        # Deletes a live tv recording.
        api_instance.delete_recording(recording_id)
    except Exception as e:
        print("Exception when calling LiveTvApi->delete_recording: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_id** | **str**| Recording id. | 

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
**204** | Recording deleted. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Item not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tuner_host**
> delete_tuner_host(id=id)

Deletes a tuner host.

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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    id = 'id_example' # str | Tuner host id. (optional)

    try:
        # Deletes a tuner host.
        api_instance.delete_tuner_host(id=id)
    except Exception as e:
        print("Exception when calling LiveTvApi->delete_tuner_host: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tuner host id. | [optional] 

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
**204** | Tuner host deleted. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discover_tuners**
> List[TunerHostInfo] discover_tuners(new_devices_only=new_devices_only)

Discover tuners.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.tuner_host_info import TunerHostInfo
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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    new_devices_only = False # bool | Only discover new tuners. (optional) (default to False)

    try:
        # Discover tuners.
        api_response = api_instance.discover_tuners(new_devices_only=new_devices_only)
        print("The response of LiveTvApi->discover_tuners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvApi->discover_tuners: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_devices_only** | **bool**| Only discover new tuners. | [optional] [default to False]

### Return type

[**List[TunerHostInfo]**](TunerHostInfo.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tuners returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discvover_tuners**
> List[TunerHostInfo] discvover_tuners(new_devices_only=new_devices_only)

Discover tuners.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.tuner_host_info import TunerHostInfo
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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    new_devices_only = False # bool | Only discover new tuners. (optional) (default to False)

    try:
        # Discover tuners.
        api_response = api_instance.discvover_tuners(new_devices_only=new_devices_only)
        print("The response of LiveTvApi->discvover_tuners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvApi->discvover_tuners: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_devices_only** | **bool**| Only discover new tuners. | [optional] [default to False]

### Return type

[**List[TunerHostInfo]**](TunerHostInfo.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tuners returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel**
> BaseItemDto get_channel(channel_id, user_id=user_id)

Gets a live tv channel.

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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    channel_id = 'channel_id_example' # str | Channel id.
    user_id = 'user_id_example' # str | Optional. Attach user data. (optional)

    try:
        # Gets a live tv channel.
        api_response = api_instance.get_channel(channel_id, user_id=user_id)
        print("The response of LiveTvApi->get_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvApi->get_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Channel id. | 
 **user_id** | **str**| Optional. Attach user data. | [optional] 

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
**200** | Live tv channel returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Item not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_mapping_options**
> ChannelMappingOptionsDto get_channel_mapping_options(provider_id=provider_id)

Get channel mapping options.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.channel_mapping_options_dto import ChannelMappingOptionsDto
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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    provider_id = 'provider_id_example' # str | Provider id. (optional)

    try:
        # Get channel mapping options.
        api_response = api_instance.get_channel_mapping_options(provider_id=provider_id)
        print("The response of LiveTvApi->get_channel_mapping_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvApi->get_channel_mapping_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider id. | [optional] 

### Return type

[**ChannelMappingOptionsDto**](ChannelMappingOptionsDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Channel mapping options returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_default_listing_provider**
> ListingsProviderInfo get_default_listing_provider()

Gets default listings provider info.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.listings_provider_info import ListingsProviderInfo
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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)

    try:
        # Gets default listings provider info.
        api_response = api_instance.get_default_listing_provider()
        print("The response of LiveTvApi->get_default_listing_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvApi->get_default_listing_provider: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListingsProviderInfo**](ListingsProviderInfo.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default listings provider info returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_default_timer**
> SeriesTimerInfoDto get_default_timer(program_id=program_id)

Gets the default values for a new timer.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.series_timer_info_dto import SeriesTimerInfoDto
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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    program_id = 'program_id_example' # str | Optional. To attach default values based on a program. (optional)

    try:
        # Gets the default values for a new timer.
        api_response = api_instance.get_default_timer(program_id=program_id)
        print("The response of LiveTvApi->get_default_timer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvApi->get_default_timer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Optional. To attach default values based on a program. | [optional] 

### Return type

[**SeriesTimerInfoDto**](SeriesTimerInfoDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default values returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_guide_info**
> GuideInfo get_guide_info()

Get guid info.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.guide_info import GuideInfo
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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)

    try:
        # Get guid info.
        api_response = api_instance.get_guide_info()
        print("The response of LiveTvApi->get_guide_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvApi->get_guide_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GuideInfo**](GuideInfo.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Guid info returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lineups**
> List[NameIdPair] get_lineups(id=id, type=type, location=location, country=country)

Gets available lineups.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.name_id_pair import NameIdPair
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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    id = 'id_example' # str | Provider id. (optional)
    type = 'type_example' # str | Provider type. (optional)
    location = 'location_example' # str | Location. (optional)
    country = 'country_example' # str | Country. (optional)

    try:
        # Gets available lineups.
        api_response = api_instance.get_lineups(id=id, type=type, location=location, country=country)
        print("The response of LiveTvApi->get_lineups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvApi->get_lineups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Provider id. | [optional] 
 **type** | **str**| Provider type. | [optional] 
 **location** | **str**| Location. | [optional] 
 **country** | **str**| Country. | [optional] 

### Return type

[**List[NameIdPair]**](NameIdPair.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Available lineups returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_live_recording_file**
> bytearray get_live_recording_file(recording_id)

Gets a live tv recording stream.

### Example


```python
import jellyfin.generated.api_10_10
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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    recording_id = 'recording_id_example' # str | Recording id.

    try:
        # Gets a live tv recording stream.
        api_response = api_instance.get_live_recording_file(recording_id)
        print("The response of LiveTvApi->get_live_recording_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvApi->get_live_recording_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_id** | **str**| Recording id. | 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: video/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recording stream returned. |  -  |
**404** | Recording not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_live_stream_file**
> bytearray get_live_stream_file(stream_id, container)

Gets a live tv channel stream.

### Example


```python
import jellyfin.generated.api_10_10
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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    stream_id = 'stream_id_example' # str | Stream id.
    container = 'container_example' # str | Container type.

    try:
        # Gets a live tv channel stream.
        api_response = api_instance.get_live_stream_file(stream_id, container)
        print("The response of LiveTvApi->get_live_stream_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvApi->get_live_stream_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_id** | **str**| Stream id. | 
 **container** | **str**| Container type. | 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: video/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stream returned. |  -  |
**404** | Stream not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_live_tv_channels**
> BaseItemDtoQueryResult get_live_tv_channels(type=type, user_id=user_id, start_index=start_index, is_movie=is_movie, is_series=is_series, is_news=is_news, is_kids=is_kids, is_sports=is_sports, limit=limit, is_favorite=is_favorite, is_liked=is_liked, is_disliked=is_disliked, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, fields=fields, enable_user_data=enable_user_data, sort_by=sort_by, sort_order=sort_order, enable_favorite_sorting=enable_favorite_sorting, add_current_program=add_current_program)

Gets available live tv channels.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.base_item_dto_query_result import BaseItemDtoQueryResult
from jellyfin.generated.api_10_10.models.channel_type import ChannelType
from jellyfin.generated.api_10_10.models.image_type import ImageType
from jellyfin.generated.api_10_10.models.item_fields import ItemFields
from jellyfin.generated.api_10_10.models.item_sort_by import ItemSortBy
from jellyfin.generated.api_10_10.models.sort_order import SortOrder
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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    type = jellyfin.generated.api_10_10.ChannelType() # ChannelType | Optional. Filter by channel type. (optional)
    user_id = 'user_id_example' # str | Optional. Filter by user and attach user data. (optional)
    start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
    is_movie = True # bool | Optional. Filter for movies. (optional)
    is_series = True # bool | Optional. Filter for series. (optional)
    is_news = True # bool | Optional. Filter for news. (optional)
    is_kids = True # bool | Optional. Filter for kids. (optional)
    is_sports = True # bool | Optional. Filter for sports. (optional)
    limit = 56 # int | Optional. The maximum number of records to return. (optional)
    is_favorite = True # bool | Optional. Filter by channels that are favorites, or not. (optional)
    is_liked = True # bool | Optional. Filter by channels that are liked, or not. (optional)
    is_disliked = True # bool | Optional. Filter by channels that are disliked, or not. (optional)
    enable_images = True # bool | Optional. Include image information in output. (optional)
    image_type_limit = 56 # int | Optional. The max number of images to return, per image type. (optional)
    enable_image_types = [jellyfin.generated.api_10_10.ImageType()] # List[ImageType] | \"Optional. The image types to include in the output. (optional)
    fields = [jellyfin.generated.api_10_10.ItemFields()] # List[ItemFields] | Optional. Specify additional fields of information to return in the output. (optional)
    enable_user_data = True # bool | Optional. Include user data. (optional)
    sort_by = [jellyfin.generated.api_10_10.ItemSortBy()] # List[ItemSortBy] | Optional. Key to sort by. (optional)
    sort_order = jellyfin.generated.api_10_10.SortOrder() # SortOrder | Optional. Sort order. (optional)
    enable_favorite_sorting = False # bool | Optional. Incorporate favorite and like status into channel sorting. (optional) (default to False)
    add_current_program = True # bool | Optional. Adds current program info to each channel. (optional) (default to True)

    try:
        # Gets available live tv channels.
        api_response = api_instance.get_live_tv_channels(type=type, user_id=user_id, start_index=start_index, is_movie=is_movie, is_series=is_series, is_news=is_news, is_kids=is_kids, is_sports=is_sports, limit=limit, is_favorite=is_favorite, is_liked=is_liked, is_disliked=is_disliked, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, fields=fields, enable_user_data=enable_user_data, sort_by=sort_by, sort_order=sort_order, enable_favorite_sorting=enable_favorite_sorting, add_current_program=add_current_program)
        print("The response of LiveTvApi->get_live_tv_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvApi->get_live_tv_channels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**ChannelType**](.md)| Optional. Filter by channel type. | [optional] 
 **user_id** | **str**| Optional. Filter by user and attach user data. | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **is_movie** | **bool**| Optional. Filter for movies. | [optional] 
 **is_series** | **bool**| Optional. Filter for series. | [optional] 
 **is_news** | **bool**| Optional. Filter for news. | [optional] 
 **is_kids** | **bool**| Optional. Filter for kids. | [optional] 
 **is_sports** | **bool**| Optional. Filter for sports. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return. | [optional] 
 **is_favorite** | **bool**| Optional. Filter by channels that are favorites, or not. | [optional] 
 **is_liked** | **bool**| Optional. Filter by channels that are liked, or not. | [optional] 
 **is_disliked** | **bool**| Optional. Filter by channels that are disliked, or not. | [optional] 
 **enable_images** | **bool**| Optional. Include image information in output. | [optional] 
 **image_type_limit** | **int**| Optional. The max number of images to return, per image type. | [optional] 
 **enable_image_types** | [**List[ImageType]**](ImageType.md)| \&quot;Optional. The image types to include in the output. | [optional] 
 **fields** | [**List[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. | [optional] 
 **enable_user_data** | **bool**| Optional. Include user data. | [optional] 
 **sort_by** | [**List[ItemSortBy]**](ItemSortBy.md)| Optional. Key to sort by. | [optional] 
 **sort_order** | [**SortOrder**](.md)| Optional. Sort order. | [optional] 
 **enable_favorite_sorting** | **bool**| Optional. Incorporate favorite and like status into channel sorting. | [optional] [default to False]
 **add_current_program** | **bool**| Optional. Adds current program info to each channel. | [optional] [default to True]

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
**200** | Available live tv channels returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_live_tv_info**
> LiveTvInfo get_live_tv_info()

Gets available live tv services.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.live_tv_info import LiveTvInfo
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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)

    try:
        # Gets available live tv services.
        api_response = api_instance.get_live_tv_info()
        print("The response of LiveTvApi->get_live_tv_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvApi->get_live_tv_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LiveTvInfo**](LiveTvInfo.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Available live tv services returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_live_tv_programs**
> BaseItemDtoQueryResult get_live_tv_programs(channel_ids=channel_ids, user_id=user_id, min_start_date=min_start_date, has_aired=has_aired, is_airing=is_airing, max_start_date=max_start_date, min_end_date=min_end_date, max_end_date=max_end_date, is_movie=is_movie, is_series=is_series, is_news=is_news, is_kids=is_kids, is_sports=is_sports, start_index=start_index, limit=limit, sort_by=sort_by, sort_order=sort_order, genres=genres, genre_ids=genre_ids, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, enable_user_data=enable_user_data, series_timer_id=series_timer_id, library_series_id=library_series_id, fields=fields, enable_total_record_count=enable_total_record_count)

Gets available live tv epgs.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.base_item_dto_query_result import BaseItemDtoQueryResult
from jellyfin.generated.api_10_10.models.image_type import ImageType
from jellyfin.generated.api_10_10.models.item_fields import ItemFields
from jellyfin.generated.api_10_10.models.item_sort_by import ItemSortBy
from jellyfin.generated.api_10_10.models.sort_order import SortOrder
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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    channel_ids = ['channel_ids_example'] # List[str] | The channels to return guide information for. (optional)
    user_id = 'user_id_example' # str | Optional. Filter by user id. (optional)
    min_start_date = '2013-10-20T19:20:30+01:00' # datetime | Optional. The minimum premiere start date. (optional)
    has_aired = True # bool | Optional. Filter by programs that have completed airing, or not. (optional)
    is_airing = True # bool | Optional. Filter by programs that are currently airing, or not. (optional)
    max_start_date = '2013-10-20T19:20:30+01:00' # datetime | Optional. The maximum premiere start date. (optional)
    min_end_date = '2013-10-20T19:20:30+01:00' # datetime | Optional. The minimum premiere end date. (optional)
    max_end_date = '2013-10-20T19:20:30+01:00' # datetime | Optional. The maximum premiere end date. (optional)
    is_movie = True # bool | Optional. Filter for movies. (optional)
    is_series = True # bool | Optional. Filter for series. (optional)
    is_news = True # bool | Optional. Filter for news. (optional)
    is_kids = True # bool | Optional. Filter for kids. (optional)
    is_sports = True # bool | Optional. Filter for sports. (optional)
    start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
    limit = 56 # int | Optional. The maximum number of records to return. (optional)
    sort_by = [jellyfin.generated.api_10_10.ItemSortBy()] # List[ItemSortBy] | Optional. Specify one or more sort orders, comma delimited. Options: Name, StartDate. (optional)
    sort_order = [jellyfin.generated.api_10_10.SortOrder()] # List[SortOrder] | Sort Order - Ascending,Descending. (optional)
    genres = ['genres_example'] # List[str] | The genres to return guide information for. (optional)
    genre_ids = ['genre_ids_example'] # List[str] | The genre ids to return guide information for. (optional)
    enable_images = True # bool | Optional. Include image information in output. (optional)
    image_type_limit = 56 # int | Optional. The max number of images to return, per image type. (optional)
    enable_image_types = [jellyfin.generated.api_10_10.ImageType()] # List[ImageType] | Optional. The image types to include in the output. (optional)
    enable_user_data = True # bool | Optional. Include user data. (optional)
    series_timer_id = 'series_timer_id_example' # str | Optional. Filter by series timer id. (optional)
    library_series_id = 'library_series_id_example' # str | Optional. Filter by library series id. (optional)
    fields = [jellyfin.generated.api_10_10.ItemFields()] # List[ItemFields] | Optional. Specify additional fields of information to return in the output. (optional)
    enable_total_record_count = True # bool | Retrieve total record count. (optional) (default to True)

    try:
        # Gets available live tv epgs.
        api_response = api_instance.get_live_tv_programs(channel_ids=channel_ids, user_id=user_id, min_start_date=min_start_date, has_aired=has_aired, is_airing=is_airing, max_start_date=max_start_date, min_end_date=min_end_date, max_end_date=max_end_date, is_movie=is_movie, is_series=is_series, is_news=is_news, is_kids=is_kids, is_sports=is_sports, start_index=start_index, limit=limit, sort_by=sort_by, sort_order=sort_order, genres=genres, genre_ids=genre_ids, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, enable_user_data=enable_user_data, series_timer_id=series_timer_id, library_series_id=library_series_id, fields=fields, enable_total_record_count=enable_total_record_count)
        print("The response of LiveTvApi->get_live_tv_programs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvApi->get_live_tv_programs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_ids** | [**List[str]**](str.md)| The channels to return guide information for. | [optional] 
 **user_id** | **str**| Optional. Filter by user id. | [optional] 
 **min_start_date** | **datetime**| Optional. The minimum premiere start date. | [optional] 
 **has_aired** | **bool**| Optional. Filter by programs that have completed airing, or not. | [optional] 
 **is_airing** | **bool**| Optional. Filter by programs that are currently airing, or not. | [optional] 
 **max_start_date** | **datetime**| Optional. The maximum premiere start date. | [optional] 
 **min_end_date** | **datetime**| Optional. The minimum premiere end date. | [optional] 
 **max_end_date** | **datetime**| Optional. The maximum premiere end date. | [optional] 
 **is_movie** | **bool**| Optional. Filter for movies. | [optional] 
 **is_series** | **bool**| Optional. Filter for series. | [optional] 
 **is_news** | **bool**| Optional. Filter for news. | [optional] 
 **is_kids** | **bool**| Optional. Filter for kids. | [optional] 
 **is_sports** | **bool**| Optional. Filter for sports. | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return. | [optional] 
 **sort_by** | [**List[ItemSortBy]**](ItemSortBy.md)| Optional. Specify one or more sort orders, comma delimited. Options: Name, StartDate. | [optional] 
 **sort_order** | [**List[SortOrder]**](SortOrder.md)| Sort Order - Ascending,Descending. | [optional] 
 **genres** | [**List[str]**](str.md)| The genres to return guide information for. | [optional] 
 **genre_ids** | [**List[str]**](str.md)| The genre ids to return guide information for. | [optional] 
 **enable_images** | **bool**| Optional. Include image information in output. | [optional] 
 **image_type_limit** | **int**| Optional. The max number of images to return, per image type. | [optional] 
 **enable_image_types** | [**List[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 
 **enable_user_data** | **bool**| Optional. Include user data. | [optional] 
 **series_timer_id** | **str**| Optional. Filter by series timer id. | [optional] 
 **library_series_id** | **str**| Optional. Filter by library series id. | [optional] 
 **fields** | [**List[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. | [optional] 
 **enable_total_record_count** | **bool**| Retrieve total record count. | [optional] [default to True]

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
**200** | Live tv epgs returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_program**
> BaseItemDto get_program(program_id, user_id=user_id)

Gets a live tv program.

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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    program_id = 'program_id_example' # str | Program id.
    user_id = 'user_id_example' # str | Optional. Attach user data. (optional)

    try:
        # Gets a live tv program.
        api_response = api_instance.get_program(program_id, user_id=user_id)
        print("The response of LiveTvApi->get_program:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvApi->get_program: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Program id. | 
 **user_id** | **str**| Optional. Attach user data. | [optional] 

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
**200** | Program returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_programs**
> BaseItemDtoQueryResult get_programs(get_programs_dto=get_programs_dto)

Gets available live tv epgs.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.base_item_dto_query_result import BaseItemDtoQueryResult
from jellyfin.generated.api_10_10.models.get_programs_dto import GetProgramsDto
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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    get_programs_dto = jellyfin.generated.api_10_10.GetProgramsDto() # GetProgramsDto | Request body. (optional)

    try:
        # Gets available live tv epgs.
        api_response = api_instance.get_programs(get_programs_dto=get_programs_dto)
        print("The response of LiveTvApi->get_programs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvApi->get_programs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_programs_dto** | [**GetProgramsDto**](GetProgramsDto.md)| Request body. | [optional] 

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Live tv epgs returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommended_programs**
> BaseItemDtoQueryResult get_recommended_programs(user_id=user_id, limit=limit, is_airing=is_airing, has_aired=has_aired, is_series=is_series, is_movie=is_movie, is_news=is_news, is_kids=is_kids, is_sports=is_sports, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, genre_ids=genre_ids, fields=fields, enable_user_data=enable_user_data, enable_total_record_count=enable_total_record_count)

Gets recommended live tv epgs.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.base_item_dto_query_result import BaseItemDtoQueryResult
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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    user_id = 'user_id_example' # str | Optional. filter by user id. (optional)
    limit = 56 # int | Optional. The maximum number of records to return. (optional)
    is_airing = True # bool | Optional. Filter by programs that are currently airing, or not. (optional)
    has_aired = True # bool | Optional. Filter by programs that have completed airing, or not. (optional)
    is_series = True # bool | Optional. Filter for series. (optional)
    is_movie = True # bool | Optional. Filter for movies. (optional)
    is_news = True # bool | Optional. Filter for news. (optional)
    is_kids = True # bool | Optional. Filter for kids. (optional)
    is_sports = True # bool | Optional. Filter for sports. (optional)
    enable_images = True # bool | Optional. Include image information in output. (optional)
    image_type_limit = 56 # int | Optional. The max number of images to return, per image type. (optional)
    enable_image_types = [jellyfin.generated.api_10_10.ImageType()] # List[ImageType] | Optional. The image types to include in the output. (optional)
    genre_ids = ['genre_ids_example'] # List[str] | The genres to return guide information for. (optional)
    fields = [jellyfin.generated.api_10_10.ItemFields()] # List[ItemFields] | Optional. Specify additional fields of information to return in the output. (optional)
    enable_user_data = True # bool | Optional. include user data. (optional)
    enable_total_record_count = True # bool | Retrieve total record count. (optional) (default to True)

    try:
        # Gets recommended live tv epgs.
        api_response = api_instance.get_recommended_programs(user_id=user_id, limit=limit, is_airing=is_airing, has_aired=has_aired, is_series=is_series, is_movie=is_movie, is_news=is_news, is_kids=is_kids, is_sports=is_sports, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, genre_ids=genre_ids, fields=fields, enable_user_data=enable_user_data, enable_total_record_count=enable_total_record_count)
        print("The response of LiveTvApi->get_recommended_programs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvApi->get_recommended_programs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Optional. filter by user id. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return. | [optional] 
 **is_airing** | **bool**| Optional. Filter by programs that are currently airing, or not. | [optional] 
 **has_aired** | **bool**| Optional. Filter by programs that have completed airing, or not. | [optional] 
 **is_series** | **bool**| Optional. Filter for series. | [optional] 
 **is_movie** | **bool**| Optional. Filter for movies. | [optional] 
 **is_news** | **bool**| Optional. Filter for news. | [optional] 
 **is_kids** | **bool**| Optional. Filter for kids. | [optional] 
 **is_sports** | **bool**| Optional. Filter for sports. | [optional] 
 **enable_images** | **bool**| Optional. Include image information in output. | [optional] 
 **image_type_limit** | **int**| Optional. The max number of images to return, per image type. | [optional] 
 **enable_image_types** | [**List[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 
 **genre_ids** | [**List[str]**](str.md)| The genres to return guide information for. | [optional] 
 **fields** | [**List[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. | [optional] 
 **enable_user_data** | **bool**| Optional. include user data. | [optional] 
 **enable_total_record_count** | **bool**| Retrieve total record count. | [optional] [default to True]

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
**200** | Recommended epgs returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording**
> BaseItemDto get_recording(recording_id, user_id=user_id)

Gets a live tv recording.

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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    recording_id = 'recording_id_example' # str | Recording id.
    user_id = 'user_id_example' # str | Optional. Attach user data. (optional)

    try:
        # Gets a live tv recording.
        api_response = api_instance.get_recording(recording_id, user_id=user_id)
        print("The response of LiveTvApi->get_recording:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvApi->get_recording: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_id** | **str**| Recording id. | 
 **user_id** | **str**| Optional. Attach user data. | [optional] 

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
**200** | Recording returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Item not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording_folders**
> BaseItemDtoQueryResult get_recording_folders(user_id=user_id)

Gets recording folders.

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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    user_id = 'user_id_example' # str | Optional. Filter by user and attach user data. (optional)

    try:
        # Gets recording folders.
        api_response = api_instance.get_recording_folders(user_id=user_id)
        print("The response of LiveTvApi->get_recording_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvApi->get_recording_folders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Optional. Filter by user and attach user data. | [optional] 

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
**200** | Recording folders returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording_group**
> get_recording_group(group_id)

Get recording group.

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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    group_id = 'group_id_example' # str | Group id.

    try:
        # Get recording group.
        api_instance.get_recording_group(group_id)
    except Exception as e:
        print("Exception when calling LiveTvApi->get_recording_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Group id. | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording_groups**
> BaseItemDtoQueryResult get_recording_groups(user_id=user_id)

Gets live tv recording groups.

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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    user_id = 'user_id_example' # str | Optional. Filter by user and attach user data. (optional)

    try:
        # Gets live tv recording groups.
        api_response = api_instance.get_recording_groups(user_id=user_id)
        print("The response of LiveTvApi->get_recording_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvApi->get_recording_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Optional. Filter by user and attach user data. | [optional] 

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
**200** | Recording groups returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recordings**
> BaseItemDtoQueryResult get_recordings(channel_id=channel_id, user_id=user_id, start_index=start_index, limit=limit, status=status, is_in_progress=is_in_progress, series_timer_id=series_timer_id, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, fields=fields, enable_user_data=enable_user_data, is_movie=is_movie, is_series=is_series, is_kids=is_kids, is_sports=is_sports, is_news=is_news, is_library_item=is_library_item, enable_total_record_count=enable_total_record_count)

Gets live tv recordings.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.base_item_dto_query_result import BaseItemDtoQueryResult
from jellyfin.generated.api_10_10.models.image_type import ImageType
from jellyfin.generated.api_10_10.models.item_fields import ItemFields
from jellyfin.generated.api_10_10.models.recording_status import RecordingStatus
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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    channel_id = 'channel_id_example' # str | Optional. Filter by channel id. (optional)
    user_id = 'user_id_example' # str | Optional. Filter by user and attach user data. (optional)
    start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
    limit = 56 # int | Optional. The maximum number of records to return. (optional)
    status = jellyfin.generated.api_10_10.RecordingStatus() # RecordingStatus | Optional. Filter by recording status. (optional)
    is_in_progress = True # bool | Optional. Filter by recordings that are in progress, or not. (optional)
    series_timer_id = 'series_timer_id_example' # str | Optional. Filter by recordings belonging to a series timer. (optional)
    enable_images = True # bool | Optional. Include image information in output. (optional)
    image_type_limit = 56 # int | Optional. The max number of images to return, per image type. (optional)
    enable_image_types = [jellyfin.generated.api_10_10.ImageType()] # List[ImageType] | Optional. The image types to include in the output. (optional)
    fields = [jellyfin.generated.api_10_10.ItemFields()] # List[ItemFields] | Optional. Specify additional fields of information to return in the output. (optional)
    enable_user_data = True # bool | Optional. Include user data. (optional)
    is_movie = True # bool | Optional. Filter for movies. (optional)
    is_series = True # bool | Optional. Filter for series. (optional)
    is_kids = True # bool | Optional. Filter for kids. (optional)
    is_sports = True # bool | Optional. Filter for sports. (optional)
    is_news = True # bool | Optional. Filter for news. (optional)
    is_library_item = True # bool | Optional. Filter for is library item. (optional)
    enable_total_record_count = True # bool | Optional. Return total record count. (optional) (default to True)

    try:
        # Gets live tv recordings.
        api_response = api_instance.get_recordings(channel_id=channel_id, user_id=user_id, start_index=start_index, limit=limit, status=status, is_in_progress=is_in_progress, series_timer_id=series_timer_id, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, fields=fields, enable_user_data=enable_user_data, is_movie=is_movie, is_series=is_series, is_kids=is_kids, is_sports=is_sports, is_news=is_news, is_library_item=is_library_item, enable_total_record_count=enable_total_record_count)
        print("The response of LiveTvApi->get_recordings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvApi->get_recordings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Optional. Filter by channel id. | [optional] 
 **user_id** | **str**| Optional. Filter by user and attach user data. | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return. | [optional] 
 **status** | [**RecordingStatus**](.md)| Optional. Filter by recording status. | [optional] 
 **is_in_progress** | **bool**| Optional. Filter by recordings that are in progress, or not. | [optional] 
 **series_timer_id** | **str**| Optional. Filter by recordings belonging to a series timer. | [optional] 
 **enable_images** | **bool**| Optional. Include image information in output. | [optional] 
 **image_type_limit** | **int**| Optional. The max number of images to return, per image type. | [optional] 
 **enable_image_types** | [**List[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 
 **fields** | [**List[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. | [optional] 
 **enable_user_data** | **bool**| Optional. Include user data. | [optional] 
 **is_movie** | **bool**| Optional. Filter for movies. | [optional] 
 **is_series** | **bool**| Optional. Filter for series. | [optional] 
 **is_kids** | **bool**| Optional. Filter for kids. | [optional] 
 **is_sports** | **bool**| Optional. Filter for sports. | [optional] 
 **is_news** | **bool**| Optional. Filter for news. | [optional] 
 **is_library_item** | **bool**| Optional. Filter for is library item. | [optional] 
 **enable_total_record_count** | **bool**| Optional. Return total record count. | [optional] [default to True]

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
**200** | Live tv recordings returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recordings_series**
> BaseItemDtoQueryResult get_recordings_series(channel_id=channel_id, user_id=user_id, group_id=group_id, start_index=start_index, limit=limit, status=status, is_in_progress=is_in_progress, series_timer_id=series_timer_id, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, fields=fields, enable_user_data=enable_user_data, enable_total_record_count=enable_total_record_count)

Gets live tv recording series.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.base_item_dto_query_result import BaseItemDtoQueryResult
from jellyfin.generated.api_10_10.models.image_type import ImageType
from jellyfin.generated.api_10_10.models.item_fields import ItemFields
from jellyfin.generated.api_10_10.models.recording_status import RecordingStatus
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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    channel_id = 'channel_id_example' # str | Optional. Filter by channel id. (optional)
    user_id = 'user_id_example' # str | Optional. Filter by user and attach user data. (optional)
    group_id = 'group_id_example' # str | Optional. Filter by recording group. (optional)
    start_index = 56 # int | Optional. The record index to start at. All items with a lower index will be dropped from the results. (optional)
    limit = 56 # int | Optional. The maximum number of records to return. (optional)
    status = jellyfin.generated.api_10_10.RecordingStatus() # RecordingStatus | Optional. Filter by recording status. (optional)
    is_in_progress = True # bool | Optional. Filter by recordings that are in progress, or not. (optional)
    series_timer_id = 'series_timer_id_example' # str | Optional. Filter by recordings belonging to a series timer. (optional)
    enable_images = True # bool | Optional. Include image information in output. (optional)
    image_type_limit = 56 # int | Optional. The max number of images to return, per image type. (optional)
    enable_image_types = [jellyfin.generated.api_10_10.ImageType()] # List[ImageType] | Optional. The image types to include in the output. (optional)
    fields = [jellyfin.generated.api_10_10.ItemFields()] # List[ItemFields] | Optional. Specify additional fields of information to return in the output. (optional)
    enable_user_data = True # bool | Optional. Include user data. (optional)
    enable_total_record_count = True # bool | Optional. Return total record count. (optional) (default to True)

    try:
        # Gets live tv recording series.
        api_response = api_instance.get_recordings_series(channel_id=channel_id, user_id=user_id, group_id=group_id, start_index=start_index, limit=limit, status=status, is_in_progress=is_in_progress, series_timer_id=series_timer_id, enable_images=enable_images, image_type_limit=image_type_limit, enable_image_types=enable_image_types, fields=fields, enable_user_data=enable_user_data, enable_total_record_count=enable_total_record_count)
        print("The response of LiveTvApi->get_recordings_series:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvApi->get_recordings_series: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Optional. Filter by channel id. | [optional] 
 **user_id** | **str**| Optional. Filter by user and attach user data. | [optional] 
 **group_id** | **str**| Optional. Filter by recording group. | [optional] 
 **start_index** | **int**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **int**| Optional. The maximum number of records to return. | [optional] 
 **status** | [**RecordingStatus**](.md)| Optional. Filter by recording status. | [optional] 
 **is_in_progress** | **bool**| Optional. Filter by recordings that are in progress, or not. | [optional] 
 **series_timer_id** | **str**| Optional. Filter by recordings belonging to a series timer. | [optional] 
 **enable_images** | **bool**| Optional. Include image information in output. | [optional] 
 **image_type_limit** | **int**| Optional. The max number of images to return, per image type. | [optional] 
 **enable_image_types** | [**List[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 
 **fields** | [**List[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. | [optional] 
 **enable_user_data** | **bool**| Optional. Include user data. | [optional] 
 **enable_total_record_count** | **bool**| Optional. Return total record count. | [optional] [default to True]

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
**200** | Live tv recordings returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schedules_direct_countries**
> bytearray get_schedules_direct_countries()

Gets available countries.

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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)

    try:
        # Gets available countries.
        api_response = api_instance.get_schedules_direct_countries()
        print("The response of LiveTvApi->get_schedules_direct_countries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvApi->get_schedules_direct_countries: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**bytearray**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Available countries returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_series_timer**
> SeriesTimerInfoDto get_series_timer(timer_id)

Gets a live tv series timer.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.series_timer_info_dto import SeriesTimerInfoDto
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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    timer_id = 'timer_id_example' # str | Timer id.

    try:
        # Gets a live tv series timer.
        api_response = api_instance.get_series_timer(timer_id)
        print("The response of LiveTvApi->get_series_timer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvApi->get_series_timer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timer_id** | **str**| Timer id. | 

### Return type

[**SeriesTimerInfoDto**](SeriesTimerInfoDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Series timer returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Series timer not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_series_timers**
> SeriesTimerInfoDtoQueryResult get_series_timers(sort_by=sort_by, sort_order=sort_order)

Gets live tv series timers.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.series_timer_info_dto_query_result import SeriesTimerInfoDtoQueryResult
from jellyfin.generated.api_10_10.models.sort_order import SortOrder
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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    sort_by = 'sort_by_example' # str | Optional. Sort by SortName or Priority. (optional)
    sort_order = jellyfin.generated.api_10_10.SortOrder() # SortOrder | Optional. Sort in Ascending or Descending order. (optional)

    try:
        # Gets live tv series timers.
        api_response = api_instance.get_series_timers(sort_by=sort_by, sort_order=sort_order)
        print("The response of LiveTvApi->get_series_timers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvApi->get_series_timers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_by** | **str**| Optional. Sort by SortName or Priority. | [optional] 
 **sort_order** | [**SortOrder**](.md)| Optional. Sort in Ascending or Descending order. | [optional] 

### Return type

[**SeriesTimerInfoDtoQueryResult**](SeriesTimerInfoDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Timers returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_timer**
> TimerInfoDto get_timer(timer_id)

Gets a timer.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.timer_info_dto import TimerInfoDto
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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    timer_id = 'timer_id_example' # str | Timer id.

    try:
        # Gets a timer.
        api_response = api_instance.get_timer(timer_id)
        print("The response of LiveTvApi->get_timer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvApi->get_timer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timer_id** | **str**| Timer id. | 

### Return type

[**TimerInfoDto**](TimerInfoDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Timer returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_timers**
> TimerInfoDtoQueryResult get_timers(channel_id=channel_id, series_timer_id=series_timer_id, is_active=is_active, is_scheduled=is_scheduled)

Gets the live tv timers.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.timer_info_dto_query_result import TimerInfoDtoQueryResult
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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    channel_id = 'channel_id_example' # str | Optional. Filter by channel id. (optional)
    series_timer_id = 'series_timer_id_example' # str | Optional. Filter by timers belonging to a series timer. (optional)
    is_active = True # bool | Optional. Filter by timers that are active. (optional)
    is_scheduled = True # bool | Optional. Filter by timers that are scheduled. (optional)

    try:
        # Gets the live tv timers.
        api_response = api_instance.get_timers(channel_id=channel_id, series_timer_id=series_timer_id, is_active=is_active, is_scheduled=is_scheduled)
        print("The response of LiveTvApi->get_timers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvApi->get_timers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Optional. Filter by channel id. | [optional] 
 **series_timer_id** | **str**| Optional. Filter by timers belonging to a series timer. | [optional] 
 **is_active** | **bool**| Optional. Filter by timers that are active. | [optional] 
 **is_scheduled** | **bool**| Optional. Filter by timers that are scheduled. | [optional] 

### Return type

[**TimerInfoDtoQueryResult**](TimerInfoDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tuner_host_types**
> List[NameIdPair] get_tuner_host_types()

Get tuner host types.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.name_id_pair import NameIdPair
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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)

    try:
        # Get tuner host types.
        api_response = api_instance.get_tuner_host_types()
        print("The response of LiveTvApi->get_tuner_host_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvApi->get_tuner_host_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[NameIdPair]**](NameIdPair.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tuner host types returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_tuner**
> reset_tuner(tuner_id)

Resets a tv tuner.

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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    tuner_id = 'tuner_id_example' # str | Tuner id.

    try:
        # Resets a tv tuner.
        api_instance.reset_tuner(tuner_id)
    except Exception as e:
        print("Exception when calling LiveTvApi->reset_tuner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tuner_id** | **str**| Tuner id. | 

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
**204** | Tuner reset. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_channel_mapping**
> TunerChannelMapping set_channel_mapping(set_channel_mapping_dto)

Set channel mappings.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.set_channel_mapping_dto import SetChannelMappingDto
from jellyfin.generated.api_10_10.models.tuner_channel_mapping import TunerChannelMapping
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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    set_channel_mapping_dto = jellyfin.generated.api_10_10.SetChannelMappingDto() # SetChannelMappingDto | The set channel mapping dto.

    try:
        # Set channel mappings.
        api_response = api_instance.set_channel_mapping(set_channel_mapping_dto)
        print("The response of LiveTvApi->set_channel_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveTvApi->set_channel_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_channel_mapping_dto** | [**SetChannelMappingDto**](SetChannelMappingDto.md)| The set channel mapping dto. | 

### Return type

[**TunerChannelMapping**](TunerChannelMapping.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created channel mapping returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_series_timer**
> update_series_timer(timer_id, series_timer_info_dto=series_timer_info_dto)

Updates a live tv series timer.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.series_timer_info_dto import SeriesTimerInfoDto
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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    timer_id = 'timer_id_example' # str | Timer id.
    series_timer_info_dto = jellyfin.generated.api_10_10.SeriesTimerInfoDto() # SeriesTimerInfoDto | New series timer info. (optional)

    try:
        # Updates a live tv series timer.
        api_instance.update_series_timer(timer_id, series_timer_info_dto=series_timer_info_dto)
    except Exception as e:
        print("Exception when calling LiveTvApi->update_series_timer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timer_id** | **str**| Timer id. | 
 **series_timer_info_dto** | [**SeriesTimerInfoDto**](SeriesTimerInfoDto.md)| New series timer info. | [optional] 

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
**204** | Series timer updated. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_timer**
> update_timer(timer_id, timer_info_dto=timer_info_dto)

Updates a live tv timer.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.timer_info_dto import TimerInfoDto
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
    api_instance = jellyfin.generated.api_10_10.LiveTvApi(api_client)
    timer_id = 'timer_id_example' # str | Timer id.
    timer_info_dto = jellyfin.generated.api_10_10.TimerInfoDto() # TimerInfoDto | New timer info. (optional)

    try:
        # Updates a live tv timer.
        api_instance.update_timer(timer_id, timer_info_dto=timer_info_dto)
    except Exception as e:
        print("Exception when calling LiveTvApi->update_timer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timer_id** | **str**| Timer id. | 
 **timer_info_dto** | [**TimerInfoDto**](TimerInfoDto.md)| New timer info. | [optional] 

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
**204** | Timer updated. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

