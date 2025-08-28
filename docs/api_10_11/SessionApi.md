# jellyfin.generated.api_10_11.SessionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_to_session**](SessionApi.md#add_user_to_session) | **POST** /Sessions/{sessionId}/User/{userId} | Adds an additional user to a session.
[**display_content**](SessionApi.md#display_content) | **POST** /Sessions/{sessionId}/Viewing | Instructs a session to browse to an item or view.
[**get_auth_providers**](SessionApi.md#get_auth_providers) | **GET** /Auth/Providers | Get all auth providers.
[**get_password_reset_providers**](SessionApi.md#get_password_reset_providers) | **GET** /Auth/PasswordResetProviders | Get all password reset providers.
[**get_sessions**](SessionApi.md#get_sessions) | **GET** /Sessions | Gets a list of sessions.
[**play**](SessionApi.md#play) | **POST** /Sessions/{sessionId}/Playing | Instructs a session to play an item.
[**post_capabilities**](SessionApi.md#post_capabilities) | **POST** /Sessions/Capabilities | Updates capabilities for a device.
[**post_full_capabilities**](SessionApi.md#post_full_capabilities) | **POST** /Sessions/Capabilities/Full | Updates capabilities for a device.
[**remove_user_from_session**](SessionApi.md#remove_user_from_session) | **DELETE** /Sessions/{sessionId}/User/{userId} | Removes an additional user from a session.
[**report_session_ended**](SessionApi.md#report_session_ended) | **POST** /Sessions/Logout | Reports that a session has ended.
[**report_viewing**](SessionApi.md#report_viewing) | **POST** /Sessions/Viewing | Reports that a session is viewing an item.
[**send_full_general_command**](SessionApi.md#send_full_general_command) | **POST** /Sessions/{sessionId}/Command | Issues a full general command to a client.
[**send_general_command**](SessionApi.md#send_general_command) | **POST** /Sessions/{sessionId}/Command/{command} | Issues a general command to a client.
[**send_message_command**](SessionApi.md#send_message_command) | **POST** /Sessions/{sessionId}/Message | Issues a command to a client to display a message to the user.
[**send_playstate_command**](SessionApi.md#send_playstate_command) | **POST** /Sessions/{sessionId}/Playing/{command} | Issues a playstate command to a client.
[**send_system_command**](SessionApi.md#send_system_command) | **POST** /Sessions/{sessionId}/System/{command} | Issues a system command to a client.


# **add_user_to_session**
> add_user_to_session(session_id, user_id)

Adds an additional user to a session.

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
    api_instance = jellyfin.generated.api_10_11.SessionApi(api_client)
    session_id = 'session_id_example' # str | The session id.
    user_id = 'user_id_example' # str | The user id.

    try:
        # Adds an additional user to a session.
        api_instance.add_user_to_session(session_id, user_id)
    except Exception as e:
        print("Exception when calling SessionApi->add_user_to_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The session id. | 
 **user_id** | **str**| The user id. | 

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
**204** | User added to session. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_content**
> display_content(session_id, item_type, item_id, item_name)

Instructs a session to browse to an item or view.

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
    api_instance = jellyfin.generated.api_10_11.SessionApi(api_client)
    session_id = 'session_id_example' # str | The session Id.
    item_type = jellyfin.generated.api_10_11.BaseItemKind() # BaseItemKind | The type of item to browse to.
    item_id = 'item_id_example' # str | The Id of the item.
    item_name = 'item_name_example' # str | The name of the item.

    try:
        # Instructs a session to browse to an item or view.
        api_instance.display_content(session_id, item_type, item_id, item_name)
    except Exception as e:
        print("Exception when calling SessionApi->display_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The session Id. | 
 **item_type** | **BaseItemKind**| The type of item to browse to. | 
 **item_id** | **str**| The Id of the item. | 
 **item_name** | **str**| The name of the item. | 

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
**204** | Instruction sent to session. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_providers**
> List[NameIdPair] get_auth_providers()

Get all auth providers.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.name_id_pair import NameIdPair
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
    api_instance = jellyfin.generated.api_10_11.SessionApi(api_client)

    try:
        # Get all auth providers.
        api_response = api_instance.get_auth_providers()
        print("The response of SessionApi->get_auth_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionApi->get_auth_providers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[NameIdPair]**](NameIdPair.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Auth providers retrieved. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_password_reset_providers**
> List[NameIdPair] get_password_reset_providers()

Get all password reset providers.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.name_id_pair import NameIdPair
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
    api_instance = jellyfin.generated.api_10_11.SessionApi(api_client)

    try:
        # Get all password reset providers.
        api_response = api_instance.get_password_reset_providers()
        print("The response of SessionApi->get_password_reset_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionApi->get_password_reset_providers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[NameIdPair]**](NameIdPair.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Password reset providers retrieved. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sessions**
> List[SessionInfoDto] get_sessions(controllable_by_user_id=controllable_by_user_id, device_id=device_id, active_within_seconds=active_within_seconds)

Gets a list of sessions.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.session_info_dto import SessionInfoDto
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
    api_instance = jellyfin.generated.api_10_11.SessionApi(api_client)
    controllable_by_user_id = 'controllable_by_user_id_example' # str | Filter by sessions that a given user is allowed to remote control. (optional)
    device_id = 'device_id_example' # str | Filter by device Id. (optional)
    active_within_seconds = 56 # int | Optional. Filter by sessions that were active in the last n seconds. (optional)

    try:
        # Gets a list of sessions.
        api_response = api_instance.get_sessions(controllable_by_user_id=controllable_by_user_id, device_id=device_id, active_within_seconds=active_within_seconds)
        print("The response of SessionApi->get_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionApi->get_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **controllable_by_user_id** | **str**| Filter by sessions that a given user is allowed to remote control. | [optional] 
 **device_id** | **str**| Filter by device Id. | [optional] 
 **active_within_seconds** | **int**| Optional. Filter by sessions that were active in the last n seconds. | [optional] 

### Return type

[**List[SessionInfoDto]**](SessionInfoDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of sessions returned. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **play**
> play(session_id, play_command, item_ids, start_position_ticks=start_position_ticks, media_source_id=media_source_id, audio_stream_index=audio_stream_index, subtitle_stream_index=subtitle_stream_index, start_index=start_index)

Instructs a session to play an item.

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
    api_instance = jellyfin.generated.api_10_11.SessionApi(api_client)
    session_id = 'session_id_example' # str | The session id.
    play_command = jellyfin.generated.api_10_11.PlayCommand() # PlayCommand | The type of play command to issue (PlayNow, PlayNext, PlayLast). Clients who have not yet implemented play next and play last may play now.
    item_ids = ['item_ids_example'] # List[str] | The ids of the items to play, comma delimited.
    start_position_ticks = 56 # int | The starting position of the first item. (optional)
    media_source_id = 'media_source_id_example' # str | Optional. The media source id. (optional)
    audio_stream_index = 56 # int | Optional. The index of the audio stream to play. (optional)
    subtitle_stream_index = 56 # int | Optional. The index of the subtitle stream to play. (optional)
    start_index = 56 # int | Optional. The start index. (optional)

    try:
        # Instructs a session to play an item.
        api_instance.play(session_id, play_command, item_ids, start_position_ticks=start_position_ticks, media_source_id=media_source_id, audio_stream_index=audio_stream_index, subtitle_stream_index=subtitle_stream_index, start_index=start_index)
    except Exception as e:
        print("Exception when calling SessionApi->play: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The session id. | 
 **play_command** | **PlayCommand**| The type of play command to issue (PlayNow, PlayNext, PlayLast). Clients who have not yet implemented play next and play last may play now. | 
 **item_ids** | [**List[str]**](str.md)| The ids of the items to play, comma delimited. | 
 **start_position_ticks** | **int**| The starting position of the first item. | [optional] 
 **media_source_id** | **str**| Optional. The media source id. | [optional] 
 **audio_stream_index** | **int**| Optional. The index of the audio stream to play. | [optional] 
 **subtitle_stream_index** | **int**| Optional. The index of the subtitle stream to play. | [optional] 
 **start_index** | **int**| Optional. The start index. | [optional] 

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
**204** | Instruction sent to session. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_capabilities**
> post_capabilities(id=id, playable_media_types=playable_media_types, supported_commands=supported_commands, supports_media_control=supports_media_control, supports_persistent_identifier=supports_persistent_identifier)

Updates capabilities for a device.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.general_command_type import GeneralCommandType
from jellyfin.generated.api_10_11.models.media_type import MediaType
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
    api_instance = jellyfin.generated.api_10_11.SessionApi(api_client)
    id = 'id_example' # str | The session id. (optional)
    playable_media_types = [jellyfin.generated.api_10_11.MediaType()] # List[MediaType] | A list of playable media types, comma delimited. Audio, Video, Book, Photo. (optional)
    supported_commands = [jellyfin.generated.api_10_11.GeneralCommandType()] # List[GeneralCommandType] | A list of supported remote control commands, comma delimited. (optional)
    supports_media_control = False # bool | Determines whether media can be played remotely.. (optional) (default to False)
    supports_persistent_identifier = True # bool | Determines whether the device supports a unique identifier. (optional) (default to True)

    try:
        # Updates capabilities for a device.
        api_instance.post_capabilities(id=id, playable_media_types=playable_media_types, supported_commands=supported_commands, supports_media_control=supports_media_control, supports_persistent_identifier=supports_persistent_identifier)
    except Exception as e:
        print("Exception when calling SessionApi->post_capabilities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The session id. | [optional] 
 **playable_media_types** | [**List[MediaType]**](MediaType.md)| A list of playable media types, comma delimited. Audio, Video, Book, Photo. | [optional] 
 **supported_commands** | [**List[GeneralCommandType]**](GeneralCommandType.md)| A list of supported remote control commands, comma delimited. | [optional] 
 **supports_media_control** | **bool**| Determines whether media can be played remotely.. | [optional] [default to False]
 **supports_persistent_identifier** | **bool**| Determines whether the device supports a unique identifier. | [optional] [default to True]

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
**204** | Capabilities posted. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_full_capabilities**
> post_full_capabilities(client_capabilities_dto, id=id)

Updates capabilities for a device.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.client_capabilities_dto import ClientCapabilitiesDto
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
    api_instance = jellyfin.generated.api_10_11.SessionApi(api_client)
    client_capabilities_dto = jellyfin.generated.api_10_11.ClientCapabilitiesDto() # ClientCapabilitiesDto | The MediaBrowser.Model.Session.ClientCapabilities.
    id = 'id_example' # str | The session id. (optional)

    try:
        # Updates capabilities for a device.
        api_instance.post_full_capabilities(client_capabilities_dto, id=id)
    except Exception as e:
        print("Exception when calling SessionApi->post_full_capabilities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_capabilities_dto** | [**ClientCapabilitiesDto**](ClientCapabilitiesDto.md)| The MediaBrowser.Model.Session.ClientCapabilities. | 
 **id** | **str**| The session id. | [optional] 

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
**204** | Capabilities updated. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_from_session**
> remove_user_from_session(session_id, user_id)

Removes an additional user from a session.

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
    api_instance = jellyfin.generated.api_10_11.SessionApi(api_client)
    session_id = 'session_id_example' # str | The session id.
    user_id = 'user_id_example' # str | The user id.

    try:
        # Removes an additional user from a session.
        api_instance.remove_user_from_session(session_id, user_id)
    except Exception as e:
        print("Exception when calling SessionApi->remove_user_from_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The session id. | 
 **user_id** | **str**| The user id. | 

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
**204** | User removed from session. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_session_ended**
> report_session_ended()

Reports that a session has ended.

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
    api_instance = jellyfin.generated.api_10_11.SessionApi(api_client)

    try:
        # Reports that a session has ended.
        api_instance.report_session_ended()
    except Exception as e:
        print("Exception when calling SessionApi->report_session_ended: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**204** | Session end reported to server. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_viewing**
> report_viewing(item_id, session_id=session_id)

Reports that a session is viewing an item.

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
    api_instance = jellyfin.generated.api_10_11.SessionApi(api_client)
    item_id = 'item_id_example' # str | The item id.
    session_id = 'session_id_example' # str | The session id. (optional)

    try:
        # Reports that a session is viewing an item.
        api_instance.report_viewing(item_id, session_id=session_id)
    except Exception as e:
        print("Exception when calling SessionApi->report_viewing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **session_id** | **str**| The session id. | [optional] 

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
**204** | Session reported to server. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_full_general_command**
> send_full_general_command(session_id, general_command)

Issues a full general command to a client.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.general_command import GeneralCommand
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
    api_instance = jellyfin.generated.api_10_11.SessionApi(api_client)
    session_id = 'session_id_example' # str | The session id.
    general_command = jellyfin.generated.api_10_11.GeneralCommand() # GeneralCommand | The MediaBrowser.Model.Session.GeneralCommand.

    try:
        # Issues a full general command to a client.
        api_instance.send_full_general_command(session_id, general_command)
    except Exception as e:
        print("Exception when calling SessionApi->send_full_general_command: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The session id. | 
 **general_command** | [**GeneralCommand**](GeneralCommand.md)| The MediaBrowser.Model.Session.GeneralCommand. | 

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
**204** | Full general command sent to session. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_general_command**
> send_general_command(session_id, command)

Issues a general command to a client.

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
    api_instance = jellyfin.generated.api_10_11.SessionApi(api_client)
    session_id = 'session_id_example' # str | The session id.
    command = jellyfin.generated.api_10_11.GeneralCommandType() # GeneralCommandType | The command to send.

    try:
        # Issues a general command to a client.
        api_instance.send_general_command(session_id, command)
    except Exception as e:
        print("Exception when calling SessionApi->send_general_command: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The session id. | 
 **command** | **GeneralCommandType**| The command to send. | 

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
**204** | General command sent to session. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_message_command**
> send_message_command(session_id, message_command)

Issues a command to a client to display a message to the user.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.message_command import MessageCommand
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
    api_instance = jellyfin.generated.api_10_11.SessionApi(api_client)
    session_id = 'session_id_example' # str | The session id.
    message_command = jellyfin.generated.api_10_11.MessageCommand() # MessageCommand | The MediaBrowser.Model.Session.MessageCommand object containing Header, Message Text, and TimeoutMs.

    try:
        # Issues a command to a client to display a message to the user.
        api_instance.send_message_command(session_id, message_command)
    except Exception as e:
        print("Exception when calling SessionApi->send_message_command: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The session id. | 
 **message_command** | [**MessageCommand**](MessageCommand.md)| The MediaBrowser.Model.Session.MessageCommand object containing Header, Message Text, and TimeoutMs. | 

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
**204** | Message sent. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_playstate_command**
> send_playstate_command(session_id, command, seek_position_ticks=seek_position_ticks, controlling_user_id=controlling_user_id)

Issues a playstate command to a client.

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
    api_instance = jellyfin.generated.api_10_11.SessionApi(api_client)
    session_id = 'session_id_example' # str | The session id.
    command = jellyfin.generated.api_10_11.PlaystateCommand() # PlaystateCommand | The MediaBrowser.Model.Session.PlaystateCommand.
    seek_position_ticks = 56 # int | The optional position ticks. (optional)
    controlling_user_id = 'controlling_user_id_example' # str | The optional controlling user id. (optional)

    try:
        # Issues a playstate command to a client.
        api_instance.send_playstate_command(session_id, command, seek_position_ticks=seek_position_ticks, controlling_user_id=controlling_user_id)
    except Exception as e:
        print("Exception when calling SessionApi->send_playstate_command: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The session id. | 
 **command** | **PlaystateCommand**| The MediaBrowser.Model.Session.PlaystateCommand. | 
 **seek_position_ticks** | **int**| The optional position ticks. | [optional] 
 **controlling_user_id** | **str**| The optional controlling user id. | [optional] 

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
**204** | Playstate command sent to session. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_system_command**
> send_system_command(session_id, command)

Issues a system command to a client.

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
    api_instance = jellyfin.generated.api_10_11.SessionApi(api_client)
    session_id = 'session_id_example' # str | The session id.
    command = jellyfin.generated.api_10_11.GeneralCommandType() # GeneralCommandType | The command to send.

    try:
        # Issues a system command to a client.
        api_instance.send_system_command(session_id, command)
    except Exception as e:
        print("Exception when calling SessionApi->send_system_command: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The session id. | 
 **command** | **GeneralCommandType**| The command to send. | 

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
**204** | System command sent to session. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

