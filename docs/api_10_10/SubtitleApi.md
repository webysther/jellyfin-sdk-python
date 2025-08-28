# jellyfin.generated.api_10_10.SubtitleApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_subtitle**](SubtitleApi.md#delete_subtitle) | **DELETE** /Videos/{itemId}/Subtitles/{index} | Deletes an external subtitle file.
[**download_remote_subtitles**](SubtitleApi.md#download_remote_subtitles) | **POST** /Items/{itemId}/RemoteSearch/Subtitles/{subtitleId} | Downloads a remote subtitle.
[**get_fallback_font**](SubtitleApi.md#get_fallback_font) | **GET** /FallbackFont/Fonts/{name} | Gets a fallback font file.
[**get_fallback_font_list**](SubtitleApi.md#get_fallback_font_list) | **GET** /FallbackFont/Fonts | Gets a list of available fallback font files.
[**get_remote_subtitles**](SubtitleApi.md#get_remote_subtitles) | **GET** /Providers/Subtitles/Subtitles/{subtitleId} | Gets the remote subtitles.
[**get_subtitle**](SubtitleApi.md#get_subtitle) | **GET** /Videos/{routeItemId}/{routeMediaSourceId}/Subtitles/{routeIndex}/Stream.{routeFormat} | Gets subtitles in a specified format.
[**get_subtitle_playlist**](SubtitleApi.md#get_subtitle_playlist) | **GET** /Videos/{itemId}/{mediaSourceId}/Subtitles/{index}/subtitles.m3u8 | Gets an HLS subtitle playlist.
[**get_subtitle_with_ticks**](SubtitleApi.md#get_subtitle_with_ticks) | **GET** /Videos/{routeItemId}/{routeMediaSourceId}/Subtitles/{routeIndex}/{routeStartPositionTicks}/Stream.{routeFormat} | Gets subtitles in a specified format.
[**search_remote_subtitles**](SubtitleApi.md#search_remote_subtitles) | **GET** /Items/{itemId}/RemoteSearch/Subtitles/{language} | Search remote subtitles.
[**upload_subtitle**](SubtitleApi.md#upload_subtitle) | **POST** /Videos/{itemId}/Subtitles | Upload an external subtitle file.


# **delete_subtitle**
> delete_subtitle(item_id, index)

Deletes an external subtitle file.

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
    api_instance = jellyfin.generated.api_10_10.SubtitleApi(api_client)
    item_id = 'item_id_example' # str | The item id.
    index = 56 # int | The index of the subtitle file.

    try:
        # Deletes an external subtitle file.
        api_instance.delete_subtitle(item_id, index)
    except Exception as e:
        print("Exception when calling SubtitleApi->delete_subtitle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **index** | **int**| The index of the subtitle file. | 

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
**204** | Subtitle deleted. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Item not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_remote_subtitles**
> download_remote_subtitles(item_id, subtitle_id)

Downloads a remote subtitle.

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
    api_instance = jellyfin.generated.api_10_10.SubtitleApi(api_client)
    item_id = 'item_id_example' # str | The item id.
    subtitle_id = 'subtitle_id_example' # str | The subtitle id.

    try:
        # Downloads a remote subtitle.
        api_instance.download_remote_subtitles(item_id, subtitle_id)
    except Exception as e:
        print("Exception when calling SubtitleApi->download_remote_subtitles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **subtitle_id** | **str**| The subtitle id. | 

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
**204** | Subtitle downloaded. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Item not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fallback_font**
> bytearray get_fallback_font(name)

Gets a fallback font file.

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
    api_instance = jellyfin.generated.api_10_10.SubtitleApi(api_client)
    name = 'name_example' # str | The name of the fallback font file to get.

    try:
        # Gets a fallback font file.
        api_response = api_instance.get_fallback_font(name)
        print("The response of SubtitleApi->get_fallback_font:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubtitleApi->get_fallback_font: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the fallback font file to get. | 

### Return type

**bytearray**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: font/*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fallback font file retrieved. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fallback_font_list**
> List[FontFile] get_fallback_font_list()

Gets a list of available fallback font files.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.font_file import FontFile
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
    api_instance = jellyfin.generated.api_10_10.SubtitleApi(api_client)

    try:
        # Gets a list of available fallback font files.
        api_response = api_instance.get_fallback_font_list()
        print("The response of SubtitleApi->get_fallback_font_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubtitleApi->get_fallback_font_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FontFile]**](FontFile.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information retrieved. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_remote_subtitles**
> bytearray get_remote_subtitles(subtitle_id)

Gets the remote subtitles.

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
    api_instance = jellyfin.generated.api_10_10.SubtitleApi(api_client)
    subtitle_id = 'subtitle_id_example' # str | The item id.

    try:
        # Gets the remote subtitles.
        api_response = api_instance.get_remote_subtitles(subtitle_id)
        print("The response of SubtitleApi->get_remote_subtitles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubtitleApi->get_remote_subtitles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subtitle_id** | **str**| The item id. | 

### Return type

**bytearray**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subtitle**
> bytearray get_subtitle(route_item_id, route_media_source_id, route_index, route_format, item_id=item_id, media_source_id=media_source_id, index=index, format=format, end_position_ticks=end_position_ticks, copy_timestamps=copy_timestamps, add_vtt_time_map=add_vtt_time_map, start_position_ticks=start_position_ticks)

Gets subtitles in a specified format.

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
    api_instance = jellyfin.generated.api_10_10.SubtitleApi(api_client)
    route_item_id = 'route_item_id_example' # str | The (route) item id.
    route_media_source_id = 'route_media_source_id_example' # str | The (route) media source id.
    route_index = 56 # int | The (route) subtitle stream index.
    route_format = 'route_format_example' # str | The (route) format of the returned subtitle.
    item_id = 'item_id_example' # str | The item id. (optional)
    media_source_id = 'media_source_id_example' # str | The media source id. (optional)
    index = 56 # int | The subtitle stream index. (optional)
    format = 'format_example' # str | The format of the returned subtitle. (optional)
    end_position_ticks = 56 # int | Optional. The end position of the subtitle in ticks. (optional)
    copy_timestamps = False # bool | Optional. Whether to copy the timestamps. (optional) (default to False)
    add_vtt_time_map = False # bool | Optional. Whether to add a VTT time map. (optional) (default to False)
    start_position_ticks = 0 # int | The start position of the subtitle in ticks. (optional) (default to 0)

    try:
        # Gets subtitles in a specified format.
        api_response = api_instance.get_subtitle(route_item_id, route_media_source_id, route_index, route_format, item_id=item_id, media_source_id=media_source_id, index=index, format=format, end_position_ticks=end_position_ticks, copy_timestamps=copy_timestamps, add_vtt_time_map=add_vtt_time_map, start_position_ticks=start_position_ticks)
        print("The response of SubtitleApi->get_subtitle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubtitleApi->get_subtitle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_item_id** | **str**| The (route) item id. | 
 **route_media_source_id** | **str**| The (route) media source id. | 
 **route_index** | **int**| The (route) subtitle stream index. | 
 **route_format** | **str**| The (route) format of the returned subtitle. | 
 **item_id** | **str**| The item id. | [optional] 
 **media_source_id** | **str**| The media source id. | [optional] 
 **index** | **int**| The subtitle stream index. | [optional] 
 **format** | **str**| The format of the returned subtitle. | [optional] 
 **end_position_ticks** | **int**| Optional. The end position of the subtitle in ticks. | [optional] 
 **copy_timestamps** | **bool**| Optional. Whether to copy the timestamps. | [optional] [default to False]
 **add_vtt_time_map** | **bool**| Optional. Whether to add a VTT time map. | [optional] [default to False]
 **start_position_ticks** | **int**| The start position of the subtitle in ticks. | [optional] [default to 0]

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subtitle_playlist**
> bytearray get_subtitle_playlist(item_id, index, media_source_id, segment_length)

Gets an HLS subtitle playlist.

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
    api_instance = jellyfin.generated.api_10_10.SubtitleApi(api_client)
    item_id = 'item_id_example' # str | The item id.
    index = 56 # int | The subtitle stream index.
    media_source_id = 'media_source_id_example' # str | The media source id.
    segment_length = 56 # int | The subtitle segment length.

    try:
        # Gets an HLS subtitle playlist.
        api_response = api_instance.get_subtitle_playlist(item_id, index, media_source_id, segment_length)
        print("The response of SubtitleApi->get_subtitle_playlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubtitleApi->get_subtitle_playlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **index** | **int**| The subtitle stream index. | 
 **media_source_id** | **str**| The media source id. | 
 **segment_length** | **int**| The subtitle segment length. | 

### Return type

**bytearray**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-mpegURL, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subtitle playlist retrieved. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Item not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subtitle_with_ticks**
> bytearray get_subtitle_with_ticks(route_item_id, route_media_source_id, route_index, route_start_position_ticks, route_format, item_id=item_id, media_source_id=media_source_id, index=index, start_position_ticks=start_position_ticks, format=format, end_position_ticks=end_position_ticks, copy_timestamps=copy_timestamps, add_vtt_time_map=add_vtt_time_map)

Gets subtitles in a specified format.

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
    api_instance = jellyfin.generated.api_10_10.SubtitleApi(api_client)
    route_item_id = 'route_item_id_example' # str | The (route) item id.
    route_media_source_id = 'route_media_source_id_example' # str | The (route) media source id.
    route_index = 56 # int | The (route) subtitle stream index.
    route_start_position_ticks = 56 # int | The (route) start position of the subtitle in ticks.
    route_format = 'route_format_example' # str | The (route) format of the returned subtitle.
    item_id = 'item_id_example' # str | The item id. (optional)
    media_source_id = 'media_source_id_example' # str | The media source id. (optional)
    index = 56 # int | The subtitle stream index. (optional)
    start_position_ticks = 56 # int | The start position of the subtitle in ticks. (optional)
    format = 'format_example' # str | The format of the returned subtitle. (optional)
    end_position_ticks = 56 # int | Optional. The end position of the subtitle in ticks. (optional)
    copy_timestamps = False # bool | Optional. Whether to copy the timestamps. (optional) (default to False)
    add_vtt_time_map = False # bool | Optional. Whether to add a VTT time map. (optional) (default to False)

    try:
        # Gets subtitles in a specified format.
        api_response = api_instance.get_subtitle_with_ticks(route_item_id, route_media_source_id, route_index, route_start_position_ticks, route_format, item_id=item_id, media_source_id=media_source_id, index=index, start_position_ticks=start_position_ticks, format=format, end_position_ticks=end_position_ticks, copy_timestamps=copy_timestamps, add_vtt_time_map=add_vtt_time_map)
        print("The response of SubtitleApi->get_subtitle_with_ticks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubtitleApi->get_subtitle_with_ticks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_item_id** | **str**| The (route) item id. | 
 **route_media_source_id** | **str**| The (route) media source id. | 
 **route_index** | **int**| The (route) subtitle stream index. | 
 **route_start_position_ticks** | **int**| The (route) start position of the subtitle in ticks. | 
 **route_format** | **str**| The (route) format of the returned subtitle. | 
 **item_id** | **str**| The item id. | [optional] 
 **media_source_id** | **str**| The media source id. | [optional] 
 **index** | **int**| The subtitle stream index. | [optional] 
 **start_position_ticks** | **int**| The start position of the subtitle in ticks. | [optional] 
 **format** | **str**| The format of the returned subtitle. | [optional] 
 **end_position_ticks** | **int**| Optional. The end position of the subtitle in ticks. | [optional] 
 **copy_timestamps** | **bool**| Optional. Whether to copy the timestamps. | [optional] [default to False]
 **add_vtt_time_map** | **bool**| Optional. Whether to add a VTT time map. | [optional] [default to False]

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_remote_subtitles**
> List[RemoteSubtitleInfo] search_remote_subtitles(item_id, language, is_perfect_match=is_perfect_match)

Search remote subtitles.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.remote_subtitle_info import RemoteSubtitleInfo
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
    api_instance = jellyfin.generated.api_10_10.SubtitleApi(api_client)
    item_id = 'item_id_example' # str | The item id.
    language = 'language_example' # str | The language of the subtitles.
    is_perfect_match = True # bool | Optional. Only show subtitles which are a perfect match. (optional)

    try:
        # Search remote subtitles.
        api_response = api_instance.search_remote_subtitles(item_id, language, is_perfect_match=is_perfect_match)
        print("The response of SubtitleApi->search_remote_subtitles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubtitleApi->search_remote_subtitles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **language** | **str**| The language of the subtitles. | 
 **is_perfect_match** | **bool**| Optional. Only show subtitles which are a perfect match. | [optional] 

### Return type

[**List[RemoteSubtitleInfo]**](RemoteSubtitleInfo.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subtitles retrieved. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Item not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_subtitle**
> upload_subtitle(item_id, upload_subtitle_dto)

Upload an external subtitle file.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_10
from jellyfin.generated.api_10_10.models.upload_subtitle_dto import UploadSubtitleDto
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
    api_instance = jellyfin.generated.api_10_10.SubtitleApi(api_client)
    item_id = 'item_id_example' # str | The item the subtitle belongs to.
    upload_subtitle_dto = jellyfin.generated.api_10_10.UploadSubtitleDto() # UploadSubtitleDto | The request body.

    try:
        # Upload an external subtitle file.
        api_instance.upload_subtitle(item_id, upload_subtitle_dto)
    except Exception as e:
        print("Exception when calling SubtitleApi->upload_subtitle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item the subtitle belongs to. | 
 **upload_subtitle_dto** | [**UploadSubtitleDto**](UploadSubtitleDto.md)| The request body. | 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase"

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Subtitle uploaded. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Item not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

