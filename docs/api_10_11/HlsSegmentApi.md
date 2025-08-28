# jellyfin.generated.api_10_11.HlsSegmentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_hls_audio_segment_legacy_aac**](HlsSegmentApi.md#get_hls_audio_segment_legacy_aac) | **GET** /Audio/{itemId}/hls/{segmentId}/stream.aac | Gets the specified audio segment for an audio item.
[**get_hls_audio_segment_legacy_mp3**](HlsSegmentApi.md#get_hls_audio_segment_legacy_mp3) | **GET** /Audio/{itemId}/hls/{segmentId}/stream.mp3 | Gets the specified audio segment for an audio item.
[**get_hls_playlist_legacy**](HlsSegmentApi.md#get_hls_playlist_legacy) | **GET** /Videos/{itemId}/hls/{playlistId}/stream.m3u8 | Gets a hls video playlist.
[**get_hls_video_segment_legacy**](HlsSegmentApi.md#get_hls_video_segment_legacy) | **GET** /Videos/{itemId}/hls/{playlistId}/{segmentId}.{segmentContainer} | Gets a hls video segment.
[**stop_encoding_process**](HlsSegmentApi.md#stop_encoding_process) | **DELETE** /Videos/ActiveEncodings | Stops an active encoding.


# **get_hls_audio_segment_legacy_aac**
> bytearray get_hls_audio_segment_legacy_aac(item_id, segment_id)

Gets the specified audio segment for an audio item.

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
    api_instance = jellyfin.generated.api_10_11.HlsSegmentApi(api_client)
    item_id = 'item_id_example' # str | The item id.
    segment_id = 'segment_id_example' # str | The segment id.

    try:
        # Gets the specified audio segment for an audio item.
        api_response = api_instance.get_hls_audio_segment_legacy_aac(item_id, segment_id)
        print("The response of HlsSegmentApi->get_hls_audio_segment_legacy_aac:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HlsSegmentApi->get_hls_audio_segment_legacy_aac: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **segment_id** | **str**| The segment id. | 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: audio/*, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hls audio segment returned. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hls_audio_segment_legacy_mp3**
> bytearray get_hls_audio_segment_legacy_mp3(item_id, segment_id)

Gets the specified audio segment for an audio item.

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
    api_instance = jellyfin.generated.api_10_11.HlsSegmentApi(api_client)
    item_id = 'item_id_example' # str | The item id.
    segment_id = 'segment_id_example' # str | The segment id.

    try:
        # Gets the specified audio segment for an audio item.
        api_response = api_instance.get_hls_audio_segment_legacy_mp3(item_id, segment_id)
        print("The response of HlsSegmentApi->get_hls_audio_segment_legacy_mp3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HlsSegmentApi->get_hls_audio_segment_legacy_mp3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **segment_id** | **str**| The segment id. | 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: audio/*, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hls audio segment returned. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hls_playlist_legacy**
> bytearray get_hls_playlist_legacy(item_id, playlist_id)

Gets a hls video playlist.

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
    api_instance = jellyfin.generated.api_10_11.HlsSegmentApi(api_client)
    item_id = 'item_id_example' # str | The video id.
    playlist_id = 'playlist_id_example' # str | The playlist id.

    try:
        # Gets a hls video playlist.
        api_response = api_instance.get_hls_playlist_legacy(item_id, playlist_id)
        print("The response of HlsSegmentApi->get_hls_playlist_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HlsSegmentApi->get_hls_playlist_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The video id. | 
 **playlist_id** | **str**| The playlist id. | 

### Return type

**bytearray**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-mpegURL, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hls video playlist returned. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hls_video_segment_legacy**
> bytearray get_hls_video_segment_legacy(item_id, playlist_id, segment_id, segment_container)

Gets a hls video segment.

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
    api_instance = jellyfin.generated.api_10_11.HlsSegmentApi(api_client)
    item_id = 'item_id_example' # str | The item id.
    playlist_id = 'playlist_id_example' # str | The playlist id.
    segment_id = 'segment_id_example' # str | The segment id.
    segment_container = 'segment_container_example' # str | The segment container.

    try:
        # Gets a hls video segment.
        api_response = api_instance.get_hls_video_segment_legacy(item_id, playlist_id, segment_id, segment_container)
        print("The response of HlsSegmentApi->get_hls_video_segment_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HlsSegmentApi->get_hls_video_segment_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **playlist_id** | **str**| The playlist id. | 
 **segment_id** | **str**| The segment id. | 
 **segment_container** | **str**| The segment container. | 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: video/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hls video segment returned. |  -  |
**404** | Hls segment not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_encoding_process**
> stop_encoding_process(device_id, play_session_id)

Stops an active encoding.

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
    api_instance = jellyfin.generated.api_10_11.HlsSegmentApi(api_client)
    device_id = 'device_id_example' # str | The device id of the client requesting. Used to stop encoding processes when needed.
    play_session_id = 'play_session_id_example' # str | The play session id.

    try:
        # Stops an active encoding.
        api_instance.stop_encoding_process(device_id, play_session_id)
    except Exception as e:
        print("Exception when calling HlsSegmentApi->stop_encoding_process: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| The device id of the client requesting. Used to stop encoding processes when needed. | 
 **play_session_id** | **str**| The play session id. | 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Encoding stopped successfully. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

