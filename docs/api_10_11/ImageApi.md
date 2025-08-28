# jellyfin.generated.api_10_11.ImageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_custom_splashscreen**](ImageApi.md#delete_custom_splashscreen) | **DELETE** /Branding/Splashscreen | Delete a custom splashscreen.
[**delete_item_image**](ImageApi.md#delete_item_image) | **DELETE** /Items/{itemId}/Images/{imageType} | Delete an item&#39;s image.
[**delete_item_image_by_index**](ImageApi.md#delete_item_image_by_index) | **DELETE** /Items/{itemId}/Images/{imageType}/{imageIndex} | Delete an item&#39;s image.
[**delete_user_image**](ImageApi.md#delete_user_image) | **DELETE** /UserImage | Delete the user&#39;s image.
[**get_artist_image**](ImageApi.md#get_artist_image) | **GET** /Artists/{name}/Images/{imageType}/{imageIndex} | Get artist image by name.
[**get_genre_image**](ImageApi.md#get_genre_image) | **GET** /Genres/{name}/Images/{imageType} | Get genre image by name.
[**get_genre_image_by_index**](ImageApi.md#get_genre_image_by_index) | **GET** /Genres/{name}/Images/{imageType}/{imageIndex} | Get genre image by name.
[**get_item_image**](ImageApi.md#get_item_image) | **GET** /Items/{itemId}/Images/{imageType} | Gets the item&#39;s image.
[**get_item_image2**](ImageApi.md#get_item_image2) | **GET** /Items/{itemId}/Images/{imageType}/{imageIndex}/{tag}/{format}/{maxWidth}/{maxHeight}/{percentPlayed}/{unplayedCount} | Gets the item&#39;s image.
[**get_item_image_by_index**](ImageApi.md#get_item_image_by_index) | **GET** /Items/{itemId}/Images/{imageType}/{imageIndex} | Gets the item&#39;s image.
[**get_item_image_infos**](ImageApi.md#get_item_image_infos) | **GET** /Items/{itemId}/Images | Get item image infos.
[**get_music_genre_image**](ImageApi.md#get_music_genre_image) | **GET** /MusicGenres/{name}/Images/{imageType} | Get music genre image by name.
[**get_music_genre_image_by_index**](ImageApi.md#get_music_genre_image_by_index) | **GET** /MusicGenres/{name}/Images/{imageType}/{imageIndex} | Get music genre image by name.
[**get_person_image**](ImageApi.md#get_person_image) | **GET** /Persons/{name}/Images/{imageType} | Get person image by name.
[**get_person_image_by_index**](ImageApi.md#get_person_image_by_index) | **GET** /Persons/{name}/Images/{imageType}/{imageIndex} | Get person image by name.
[**get_splashscreen**](ImageApi.md#get_splashscreen) | **GET** /Branding/Splashscreen | Generates or gets the splashscreen.
[**get_studio_image**](ImageApi.md#get_studio_image) | **GET** /Studios/{name}/Images/{imageType} | Get studio image by name.
[**get_studio_image_by_index**](ImageApi.md#get_studio_image_by_index) | **GET** /Studios/{name}/Images/{imageType}/{imageIndex} | Get studio image by name.
[**get_user_image**](ImageApi.md#get_user_image) | **GET** /UserImage | Get user profile image.
[**head_artist_image**](ImageApi.md#head_artist_image) | **HEAD** /Artists/{name}/Images/{imageType}/{imageIndex} | Get artist image by name.
[**head_genre_image**](ImageApi.md#head_genre_image) | **HEAD** /Genres/{name}/Images/{imageType} | Get genre image by name.
[**head_genre_image_by_index**](ImageApi.md#head_genre_image_by_index) | **HEAD** /Genres/{name}/Images/{imageType}/{imageIndex} | Get genre image by name.
[**head_item_image**](ImageApi.md#head_item_image) | **HEAD** /Items/{itemId}/Images/{imageType} | Gets the item&#39;s image.
[**head_item_image2**](ImageApi.md#head_item_image2) | **HEAD** /Items/{itemId}/Images/{imageType}/{imageIndex}/{tag}/{format}/{maxWidth}/{maxHeight}/{percentPlayed}/{unplayedCount} | Gets the item&#39;s image.
[**head_item_image_by_index**](ImageApi.md#head_item_image_by_index) | **HEAD** /Items/{itemId}/Images/{imageType}/{imageIndex} | Gets the item&#39;s image.
[**head_music_genre_image**](ImageApi.md#head_music_genre_image) | **HEAD** /MusicGenres/{name}/Images/{imageType} | Get music genre image by name.
[**head_music_genre_image_by_index**](ImageApi.md#head_music_genre_image_by_index) | **HEAD** /MusicGenres/{name}/Images/{imageType}/{imageIndex} | Get music genre image by name.
[**head_person_image**](ImageApi.md#head_person_image) | **HEAD** /Persons/{name}/Images/{imageType} | Get person image by name.
[**head_person_image_by_index**](ImageApi.md#head_person_image_by_index) | **HEAD** /Persons/{name}/Images/{imageType}/{imageIndex} | Get person image by name.
[**head_studio_image**](ImageApi.md#head_studio_image) | **HEAD** /Studios/{name}/Images/{imageType} | Get studio image by name.
[**head_studio_image_by_index**](ImageApi.md#head_studio_image_by_index) | **HEAD** /Studios/{name}/Images/{imageType}/{imageIndex} | Get studio image by name.
[**head_user_image**](ImageApi.md#head_user_image) | **HEAD** /UserImage | Get user profile image.
[**post_user_image**](ImageApi.md#post_user_image) | **POST** /UserImage | Sets the user image.
[**set_item_image**](ImageApi.md#set_item_image) | **POST** /Items/{itemId}/Images/{imageType} | Set item image.
[**set_item_image_by_index**](ImageApi.md#set_item_image_by_index) | **POST** /Items/{itemId}/Images/{imageType}/{imageIndex} | Set item image.
[**update_item_image_index**](ImageApi.md#update_item_image_index) | **POST** /Items/{itemId}/Images/{imageType}/{imageIndex}/Index | Updates the index for an item image.
[**upload_custom_splashscreen**](ImageApi.md#upload_custom_splashscreen) | **POST** /Branding/Splashscreen | Uploads a custom splashscreen.  The body is expected to the image contents base64 encoded.


# **delete_custom_splashscreen**
> delete_custom_splashscreen()

Delete a custom splashscreen.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)

    try:
        # Delete a custom splashscreen.
        api_instance.delete_custom_splashscreen()
    except Exception as e:
        print("Exception when calling ImageApi->delete_custom_splashscreen: %s\n" % e)
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
**204** | Successfully deleted the custom splashscreen. |  -  |
**403** | User does not have permission to delete splashscreen.. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_image**
> delete_item_image(item_id, image_type, image_index=image_index)

Delete an item's image.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    item_id = 'item_id_example' # str | Item id.
    image_type = jellyfin.generated.api_10_11.ImageType() # ImageType | Image type.
    image_index = 56 # int | The image index. (optional)

    try:
        # Delete an item's image.
        api_instance.delete_item_image(item_id, image_type, image_index=image_index)
    except Exception as e:
        print("Exception when calling ImageApi->delete_item_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item id. | 
 **image_type** | **ImageType**| Image type. | 
 **image_index** | **int**| The image index. | [optional] 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Image deleted. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_image_by_index**
> delete_item_image_by_index(item_id, image_type, image_index)

Delete an item's image.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    item_id = 'item_id_example' # str | Item id.
    image_type = jellyfin.generated.api_10_11.ImageType() # ImageType | Image type.
    image_index = 56 # int | The image index.

    try:
        # Delete an item's image.
        api_instance.delete_item_image_by_index(item_id, image_type, image_index)
    except Exception as e:
        print("Exception when calling ImageApi->delete_item_image_by_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item id. | 
 **image_type** | **ImageType**| Image type. | 
 **image_index** | **int**| The image index. | 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Image deleted. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_image**
> delete_user_image(user_id=user_id)

Delete the user's image.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    user_id = 'user_id_example' # str | User Id. (optional)

    try:
        # Delete the user's image.
        api_instance.delete_user_image(user_id=user_id)
    except Exception as e:
        print("Exception when calling ImageApi->delete_user_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id. | [optional] 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Image deleted. |  -  |
**403** | User does not have permission to delete the image. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artist_image**
> bytearray get_artist_image(name, image_type, image_index, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer)

Get artist image by name.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    name = 'name_example' # str | Artist name.
    image_type = jellyfin.generated.api_10_11.ImageType() # ImageType | Image type.
    image_index = 56 # int | Image index.
    tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
    format = jellyfin.generated.api_10_11.ImageFormat() # ImageFormat | Determines the output format of the image - original,gif,jpg,png. (optional)
    max_width = 56 # int | The maximum image width to return. (optional)
    max_height = 56 # int | The maximum image height to return. (optional)
    percent_played = 3.4 # float | Optional. Percent to render for the percent played overlay. (optional)
    unplayed_count = 56 # int | Optional. Unplayed count overlay to render. (optional)
    width = 56 # int | The fixed image width to return. (optional)
    height = 56 # int | The fixed image height to return. (optional)
    quality = 56 # int | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
    fill_width = 56 # int | Width of box to fill. (optional)
    fill_height = 56 # int | Height of box to fill. (optional)
    blur = 56 # int | Optional. Blur image. (optional)
    background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
    foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)

    try:
        # Get artist image by name.
        api_response = api_instance.get_artist_image(name, image_type, image_index, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer)
        print("The response of ImageApi->get_artist_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->get_artist_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Artist name. | 
 **image_type** | **ImageType**| Image type. | 
 **image_index** | **int**| Image index. | 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | **ImageFormat**| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **percent_played** | **float**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayed_count** | **int**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **fill_width** | **int**| Width of box to fill. | [optional] 
 **fill_height** | **int**| Height of box to fill. | [optional] 
 **blur** | **int**| Optional. Blur image. | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image stream returned. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_genre_image**
> bytearray get_genre_image(name, image_type, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer, image_index=image_index)

Get genre image by name.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    name = 'name_example' # str | Genre name.
    image_type = jellyfin.generated.api_10_11.ImageType() # ImageType | Image type.
    tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
    format = jellyfin.generated.api_10_11.ImageFormat() # ImageFormat | Determines the output format of the image - original,gif,jpg,png. (optional)
    max_width = 56 # int | The maximum image width to return. (optional)
    max_height = 56 # int | The maximum image height to return. (optional)
    percent_played = 3.4 # float | Optional. Percent to render for the percent played overlay. (optional)
    unplayed_count = 56 # int | Optional. Unplayed count overlay to render. (optional)
    width = 56 # int | The fixed image width to return. (optional)
    height = 56 # int | The fixed image height to return. (optional)
    quality = 56 # int | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
    fill_width = 56 # int | Width of box to fill. (optional)
    fill_height = 56 # int | Height of box to fill. (optional)
    blur = 56 # int | Optional. Blur image. (optional)
    background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
    foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)
    image_index = 56 # int | Image index. (optional)

    try:
        # Get genre image by name.
        api_response = api_instance.get_genre_image(name, image_type, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer, image_index=image_index)
        print("The response of ImageApi->get_genre_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->get_genre_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Genre name. | 
 **image_type** | **ImageType**| Image type. | 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | **ImageFormat**| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **percent_played** | **float**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayed_count** | **int**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **fill_width** | **int**| Width of box to fill. | [optional] 
 **fill_height** | **int**| Height of box to fill. | [optional] 
 **blur** | **int**| Optional. Blur image. | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **image_index** | **int**| Image index. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image stream returned. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_genre_image_by_index**
> bytearray get_genre_image_by_index(name, image_type, image_index, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer)

Get genre image by name.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    name = 'name_example' # str | Genre name.
    image_type = jellyfin.generated.api_10_11.ImageType() # ImageType | Image type.
    image_index = 56 # int | Image index.
    tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
    format = jellyfin.generated.api_10_11.ImageFormat() # ImageFormat | Determines the output format of the image - original,gif,jpg,png. (optional)
    max_width = 56 # int | The maximum image width to return. (optional)
    max_height = 56 # int | The maximum image height to return. (optional)
    percent_played = 3.4 # float | Optional. Percent to render for the percent played overlay. (optional)
    unplayed_count = 56 # int | Optional. Unplayed count overlay to render. (optional)
    width = 56 # int | The fixed image width to return. (optional)
    height = 56 # int | The fixed image height to return. (optional)
    quality = 56 # int | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
    fill_width = 56 # int | Width of box to fill. (optional)
    fill_height = 56 # int | Height of box to fill. (optional)
    blur = 56 # int | Optional. Blur image. (optional)
    background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
    foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)

    try:
        # Get genre image by name.
        api_response = api_instance.get_genre_image_by_index(name, image_type, image_index, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer)
        print("The response of ImageApi->get_genre_image_by_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->get_genre_image_by_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Genre name. | 
 **image_type** | **ImageType**| Image type. | 
 **image_index** | **int**| Image index. | 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | **ImageFormat**| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **percent_played** | **float**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayed_count** | **int**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **fill_width** | **int**| Width of box to fill. | [optional] 
 **fill_height** | **int**| Height of box to fill. | [optional] 
 **blur** | **int**| Optional. Blur image. | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image stream returned. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_image**
> bytearray get_item_image(item_id, image_type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, tag=tag, format=format, percent_played=percent_played, unplayed_count=unplayed_count, blur=blur, background_color=background_color, foreground_layer=foreground_layer, image_index=image_index)

Gets the item's image.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    item_id = 'item_id_example' # str | Item id.
    image_type = jellyfin.generated.api_10_11.ImageType() # ImageType | Image type.
    max_width = 56 # int | The maximum image width to return. (optional)
    max_height = 56 # int | The maximum image height to return. (optional)
    width = 56 # int | The fixed image width to return. (optional)
    height = 56 # int | The fixed image height to return. (optional)
    quality = 56 # int | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
    fill_width = 56 # int | Width of box to fill. (optional)
    fill_height = 56 # int | Height of box to fill. (optional)
    tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
    format = jellyfin.generated.api_10_11.ImageFormat() # ImageFormat | Optional. The MediaBrowser.Model.Drawing.ImageFormat of the returned image. (optional)
    percent_played = 3.4 # float | Optional. Percent to render for the percent played overlay. (optional)
    unplayed_count = 56 # int | Optional. Unplayed count overlay to render. (optional)
    blur = 56 # int | Optional. Blur image. (optional)
    background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
    foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)
    image_index = 56 # int | Image index. (optional)

    try:
        # Gets the item's image.
        api_response = api_instance.get_item_image(item_id, image_type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, tag=tag, format=format, percent_played=percent_played, unplayed_count=unplayed_count, blur=blur, background_color=background_color, foreground_layer=foreground_layer, image_index=image_index)
        print("The response of ImageApi->get_item_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->get_item_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item id. | 
 **image_type** | **ImageType**| Image type. | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **fill_width** | **int**| Width of box to fill. | [optional] 
 **fill_height** | **int**| Height of box to fill. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | **ImageFormat**| Optional. The MediaBrowser.Model.Drawing.ImageFormat of the returned image. | [optional] 
 **percent_played** | **float**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayed_count** | **int**| Optional. Unplayed count overlay to render. | [optional] 
 **blur** | **int**| Optional. Blur image. | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **image_index** | **int**| Image index. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image stream returned. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_image2**
> bytearray get_item_image2(item_id, image_type, max_width, max_height, tag, format, percent_played, unplayed_count, image_index, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer)

Gets the item's image.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    item_id = 'item_id_example' # str | Item id.
    image_type = jellyfin.generated.api_10_11.ImageType() # ImageType | Image type.
    max_width = 56 # int | The maximum image width to return.
    max_height = 56 # int | The maximum image height to return.
    tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers.
    format = jellyfin.generated.api_10_11.ImageFormat() # ImageFormat | Determines the output format of the image - original,gif,jpg,png.
    percent_played = 3.4 # float | Optional. Percent to render for the percent played overlay.
    unplayed_count = 56 # int | Optional. Unplayed count overlay to render.
    image_index = 56 # int | Image index.
    width = 56 # int | The fixed image width to return. (optional)
    height = 56 # int | The fixed image height to return. (optional)
    quality = 56 # int | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
    fill_width = 56 # int | Width of box to fill. (optional)
    fill_height = 56 # int | Height of box to fill. (optional)
    blur = 56 # int | Optional. Blur image. (optional)
    background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
    foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)

    try:
        # Gets the item's image.
        api_response = api_instance.get_item_image2(item_id, image_type, max_width, max_height, tag, format, percent_played, unplayed_count, image_index, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer)
        print("The response of ImageApi->get_item_image2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->get_item_image2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item id. | 
 **image_type** | **ImageType**| Image type. | 
 **max_width** | **int**| The maximum image width to return. | 
 **max_height** | **int**| The maximum image height to return. | 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | 
 **format** | **ImageFormat**| Determines the output format of the image - original,gif,jpg,png. | 
 **percent_played** | **float**| Optional. Percent to render for the percent played overlay. | 
 **unplayed_count** | **int**| Optional. Unplayed count overlay to render. | 
 **image_index** | **int**| Image index. | 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **fill_width** | **int**| Width of box to fill. | [optional] 
 **fill_height** | **int**| Height of box to fill. | [optional] 
 **blur** | **int**| Optional. Blur image. | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image stream returned. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_image_by_index**
> bytearray get_item_image_by_index(item_id, image_type, image_index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, tag=tag, format=format, percent_played=percent_played, unplayed_count=unplayed_count, blur=blur, background_color=background_color, foreground_layer=foreground_layer)

Gets the item's image.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    item_id = 'item_id_example' # str | Item id.
    image_type = jellyfin.generated.api_10_11.ImageType() # ImageType | Image type.
    image_index = 56 # int | Image index.
    max_width = 56 # int | The maximum image width to return. (optional)
    max_height = 56 # int | The maximum image height to return. (optional)
    width = 56 # int | The fixed image width to return. (optional)
    height = 56 # int | The fixed image height to return. (optional)
    quality = 56 # int | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
    fill_width = 56 # int | Width of box to fill. (optional)
    fill_height = 56 # int | Height of box to fill. (optional)
    tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
    format = jellyfin.generated.api_10_11.ImageFormat() # ImageFormat | Optional. The MediaBrowser.Model.Drawing.ImageFormat of the returned image. (optional)
    percent_played = 3.4 # float | Optional. Percent to render for the percent played overlay. (optional)
    unplayed_count = 56 # int | Optional. Unplayed count overlay to render. (optional)
    blur = 56 # int | Optional. Blur image. (optional)
    background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
    foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)

    try:
        # Gets the item's image.
        api_response = api_instance.get_item_image_by_index(item_id, image_type, image_index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, tag=tag, format=format, percent_played=percent_played, unplayed_count=unplayed_count, blur=blur, background_color=background_color, foreground_layer=foreground_layer)
        print("The response of ImageApi->get_item_image_by_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->get_item_image_by_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item id. | 
 **image_type** | **ImageType**| Image type. | 
 **image_index** | **int**| Image index. | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **fill_width** | **int**| Width of box to fill. | [optional] 
 **fill_height** | **int**| Height of box to fill. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | **ImageFormat**| Optional. The MediaBrowser.Model.Drawing.ImageFormat of the returned image. | [optional] 
 **percent_played** | **float**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayed_count** | **int**| Optional. Unplayed count overlay to render. | [optional] 
 **blur** | **int**| Optional. Blur image. | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image stream returned. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_image_infos**
> List[ImageInfo] get_item_image_infos(item_id)

Get item image infos.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import jellyfin.generated.api_10_11
from jellyfin.generated.api_10_11.models.image_info import ImageInfo
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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    item_id = 'item_id_example' # str | Item id.

    try:
        # Get item image infos.
        api_response = api_instance.get_item_image_infos(item_id)
        print("The response of ImageApi->get_item_image_infos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->get_item_image_infos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item id. | 

### Return type

[**List[ImageInfo]**](ImageInfo.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Item images returned. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_music_genre_image**
> bytearray get_music_genre_image(name, image_type, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer, image_index=image_index)

Get music genre image by name.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    name = 'name_example' # str | Music genre name.
    image_type = jellyfin.generated.api_10_11.ImageType() # ImageType | Image type.
    tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
    format = jellyfin.generated.api_10_11.ImageFormat() # ImageFormat | Determines the output format of the image - original,gif,jpg,png. (optional)
    max_width = 56 # int | The maximum image width to return. (optional)
    max_height = 56 # int | The maximum image height to return. (optional)
    percent_played = 3.4 # float | Optional. Percent to render for the percent played overlay. (optional)
    unplayed_count = 56 # int | Optional. Unplayed count overlay to render. (optional)
    width = 56 # int | The fixed image width to return. (optional)
    height = 56 # int | The fixed image height to return. (optional)
    quality = 56 # int | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
    fill_width = 56 # int | Width of box to fill. (optional)
    fill_height = 56 # int | Height of box to fill. (optional)
    blur = 56 # int | Optional. Blur image. (optional)
    background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
    foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)
    image_index = 56 # int | Image index. (optional)

    try:
        # Get music genre image by name.
        api_response = api_instance.get_music_genre_image(name, image_type, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer, image_index=image_index)
        print("The response of ImageApi->get_music_genre_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->get_music_genre_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Music genre name. | 
 **image_type** | **ImageType**| Image type. | 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | **ImageFormat**| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **percent_played** | **float**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayed_count** | **int**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **fill_width** | **int**| Width of box to fill. | [optional] 
 **fill_height** | **int**| Height of box to fill. | [optional] 
 **blur** | **int**| Optional. Blur image. | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **image_index** | **int**| Image index. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image stream returned. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_music_genre_image_by_index**
> bytearray get_music_genre_image_by_index(name, image_type, image_index, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer)

Get music genre image by name.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    name = 'name_example' # str | Music genre name.
    image_type = jellyfin.generated.api_10_11.ImageType() # ImageType | Image type.
    image_index = 56 # int | Image index.
    tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
    format = jellyfin.generated.api_10_11.ImageFormat() # ImageFormat | Determines the output format of the image - original,gif,jpg,png. (optional)
    max_width = 56 # int | The maximum image width to return. (optional)
    max_height = 56 # int | The maximum image height to return. (optional)
    percent_played = 3.4 # float | Optional. Percent to render for the percent played overlay. (optional)
    unplayed_count = 56 # int | Optional. Unplayed count overlay to render. (optional)
    width = 56 # int | The fixed image width to return. (optional)
    height = 56 # int | The fixed image height to return. (optional)
    quality = 56 # int | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
    fill_width = 56 # int | Width of box to fill. (optional)
    fill_height = 56 # int | Height of box to fill. (optional)
    blur = 56 # int | Optional. Blur image. (optional)
    background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
    foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)

    try:
        # Get music genre image by name.
        api_response = api_instance.get_music_genre_image_by_index(name, image_type, image_index, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer)
        print("The response of ImageApi->get_music_genre_image_by_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->get_music_genre_image_by_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Music genre name. | 
 **image_type** | **ImageType**| Image type. | 
 **image_index** | **int**| Image index. | 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | **ImageFormat**| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **percent_played** | **float**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayed_count** | **int**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **fill_width** | **int**| Width of box to fill. | [optional] 
 **fill_height** | **int**| Height of box to fill. | [optional] 
 **blur** | **int**| Optional. Blur image. | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image stream returned. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_person_image**
> bytearray get_person_image(name, image_type, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer, image_index=image_index)

Get person image by name.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    name = 'name_example' # str | Person name.
    image_type = jellyfin.generated.api_10_11.ImageType() # ImageType | Image type.
    tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
    format = jellyfin.generated.api_10_11.ImageFormat() # ImageFormat | Determines the output format of the image - original,gif,jpg,png. (optional)
    max_width = 56 # int | The maximum image width to return. (optional)
    max_height = 56 # int | The maximum image height to return. (optional)
    percent_played = 3.4 # float | Optional. Percent to render for the percent played overlay. (optional)
    unplayed_count = 56 # int | Optional. Unplayed count overlay to render. (optional)
    width = 56 # int | The fixed image width to return. (optional)
    height = 56 # int | The fixed image height to return. (optional)
    quality = 56 # int | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
    fill_width = 56 # int | Width of box to fill. (optional)
    fill_height = 56 # int | Height of box to fill. (optional)
    blur = 56 # int | Optional. Blur image. (optional)
    background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
    foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)
    image_index = 56 # int | Image index. (optional)

    try:
        # Get person image by name.
        api_response = api_instance.get_person_image(name, image_type, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer, image_index=image_index)
        print("The response of ImageApi->get_person_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->get_person_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Person name. | 
 **image_type** | **ImageType**| Image type. | 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | **ImageFormat**| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **percent_played** | **float**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayed_count** | **int**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **fill_width** | **int**| Width of box to fill. | [optional] 
 **fill_height** | **int**| Height of box to fill. | [optional] 
 **blur** | **int**| Optional. Blur image. | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **image_index** | **int**| Image index. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image stream returned. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_person_image_by_index**
> bytearray get_person_image_by_index(name, image_type, image_index, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer)

Get person image by name.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    name = 'name_example' # str | Person name.
    image_type = jellyfin.generated.api_10_11.ImageType() # ImageType | Image type.
    image_index = 56 # int | Image index.
    tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
    format = jellyfin.generated.api_10_11.ImageFormat() # ImageFormat | Determines the output format of the image - original,gif,jpg,png. (optional)
    max_width = 56 # int | The maximum image width to return. (optional)
    max_height = 56 # int | The maximum image height to return. (optional)
    percent_played = 3.4 # float | Optional. Percent to render for the percent played overlay. (optional)
    unplayed_count = 56 # int | Optional. Unplayed count overlay to render. (optional)
    width = 56 # int | The fixed image width to return. (optional)
    height = 56 # int | The fixed image height to return. (optional)
    quality = 56 # int | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
    fill_width = 56 # int | Width of box to fill. (optional)
    fill_height = 56 # int | Height of box to fill. (optional)
    blur = 56 # int | Optional. Blur image. (optional)
    background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
    foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)

    try:
        # Get person image by name.
        api_response = api_instance.get_person_image_by_index(name, image_type, image_index, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer)
        print("The response of ImageApi->get_person_image_by_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->get_person_image_by_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Person name. | 
 **image_type** | **ImageType**| Image type. | 
 **image_index** | **int**| Image index. | 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | **ImageFormat**| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **percent_played** | **float**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayed_count** | **int**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **fill_width** | **int**| Width of box to fill. | [optional] 
 **fill_height** | **int**| Height of box to fill. | [optional] 
 **blur** | **int**| Optional. Blur image. | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image stream returned. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_splashscreen**
> bytearray get_splashscreen(tag=tag, format=format)

Generates or gets the splashscreen.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    tag = 'tag_example' # str | Supply the cache tag from the item object to receive strong caching headers. (optional)
    format = jellyfin.generated.api_10_11.ImageFormat() # ImageFormat | Determines the output format of the image - original,gif,jpg,png. (optional)

    try:
        # Generates or gets the splashscreen.
        api_response = api_instance.get_splashscreen(tag=tag, format=format)
        print("The response of ImageApi->get_splashscreen:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->get_splashscreen: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | **ImageFormat**| Determines the output format of the image - original,gif,jpg,png. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Splashscreen returned successfully. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_studio_image**
> bytearray get_studio_image(name, image_type, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer, image_index=image_index)

Get studio image by name.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    name = 'name_example' # str | Studio name.
    image_type = jellyfin.generated.api_10_11.ImageType() # ImageType | Image type.
    tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
    format = jellyfin.generated.api_10_11.ImageFormat() # ImageFormat | Determines the output format of the image - original,gif,jpg,png. (optional)
    max_width = 56 # int | The maximum image width to return. (optional)
    max_height = 56 # int | The maximum image height to return. (optional)
    percent_played = 3.4 # float | Optional. Percent to render for the percent played overlay. (optional)
    unplayed_count = 56 # int | Optional. Unplayed count overlay to render. (optional)
    width = 56 # int | The fixed image width to return. (optional)
    height = 56 # int | The fixed image height to return. (optional)
    quality = 56 # int | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
    fill_width = 56 # int | Width of box to fill. (optional)
    fill_height = 56 # int | Height of box to fill. (optional)
    blur = 56 # int | Optional. Blur image. (optional)
    background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
    foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)
    image_index = 56 # int | Image index. (optional)

    try:
        # Get studio image by name.
        api_response = api_instance.get_studio_image(name, image_type, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer, image_index=image_index)
        print("The response of ImageApi->get_studio_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->get_studio_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Studio name. | 
 **image_type** | **ImageType**| Image type. | 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | **ImageFormat**| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **percent_played** | **float**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayed_count** | **int**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **fill_width** | **int**| Width of box to fill. | [optional] 
 **fill_height** | **int**| Height of box to fill. | [optional] 
 **blur** | **int**| Optional. Blur image. | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **image_index** | **int**| Image index. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image stream returned. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_studio_image_by_index**
> bytearray get_studio_image_by_index(name, image_type, image_index, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer)

Get studio image by name.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    name = 'name_example' # str | Studio name.
    image_type = jellyfin.generated.api_10_11.ImageType() # ImageType | Image type.
    image_index = 56 # int | Image index.
    tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
    format = jellyfin.generated.api_10_11.ImageFormat() # ImageFormat | Determines the output format of the image - original,gif,jpg,png. (optional)
    max_width = 56 # int | The maximum image width to return. (optional)
    max_height = 56 # int | The maximum image height to return. (optional)
    percent_played = 3.4 # float | Optional. Percent to render for the percent played overlay. (optional)
    unplayed_count = 56 # int | Optional. Unplayed count overlay to render. (optional)
    width = 56 # int | The fixed image width to return. (optional)
    height = 56 # int | The fixed image height to return. (optional)
    quality = 56 # int | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
    fill_width = 56 # int | Width of box to fill. (optional)
    fill_height = 56 # int | Height of box to fill. (optional)
    blur = 56 # int | Optional. Blur image. (optional)
    background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
    foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)

    try:
        # Get studio image by name.
        api_response = api_instance.get_studio_image_by_index(name, image_type, image_index, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer)
        print("The response of ImageApi->get_studio_image_by_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->get_studio_image_by_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Studio name. | 
 **image_type** | **ImageType**| Image type. | 
 **image_index** | **int**| Image index. | 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | **ImageFormat**| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **percent_played** | **float**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayed_count** | **int**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **fill_width** | **int**| Width of box to fill. | [optional] 
 **fill_height** | **int**| Height of box to fill. | [optional] 
 **blur** | **int**| Optional. Blur image. | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image stream returned. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_image**
> bytearray get_user_image(user_id=user_id, tag=tag, format=format)

Get user profile image.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    user_id = 'user_id_example' # str | User id. (optional)
    tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
    format = jellyfin.generated.api_10_11.ImageFormat() # ImageFormat | Determines the output format of the image - original,gif,jpg,png. (optional)

    try:
        # Get user profile image.
        api_response = api_instance.get_user_image(user_id=user_id, tag=tag, format=format)
        print("The response of ImageApi->get_user_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->get_user_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User id. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | **ImageFormat**| Determines the output format of the image - original,gif,jpg,png. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image stream returned. |  -  |
**400** | User id not provided. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_artist_image**
> bytearray head_artist_image(name, image_type, image_index, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer)

Get artist image by name.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    name = 'name_example' # str | Artist name.
    image_type = jellyfin.generated.api_10_11.ImageType() # ImageType | Image type.
    image_index = 56 # int | Image index.
    tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
    format = jellyfin.generated.api_10_11.ImageFormat() # ImageFormat | Determines the output format of the image - original,gif,jpg,png. (optional)
    max_width = 56 # int | The maximum image width to return. (optional)
    max_height = 56 # int | The maximum image height to return. (optional)
    percent_played = 3.4 # float | Optional. Percent to render for the percent played overlay. (optional)
    unplayed_count = 56 # int | Optional. Unplayed count overlay to render. (optional)
    width = 56 # int | The fixed image width to return. (optional)
    height = 56 # int | The fixed image height to return. (optional)
    quality = 56 # int | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
    fill_width = 56 # int | Width of box to fill. (optional)
    fill_height = 56 # int | Height of box to fill. (optional)
    blur = 56 # int | Optional. Blur image. (optional)
    background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
    foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)

    try:
        # Get artist image by name.
        api_response = api_instance.head_artist_image(name, image_type, image_index, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer)
        print("The response of ImageApi->head_artist_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->head_artist_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Artist name. | 
 **image_type** | **ImageType**| Image type. | 
 **image_index** | **int**| Image index. | 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | **ImageFormat**| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **percent_played** | **float**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayed_count** | **int**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **fill_width** | **int**| Width of box to fill. | [optional] 
 **fill_height** | **int**| Height of box to fill. | [optional] 
 **blur** | **int**| Optional. Blur image. | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image stream returned. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_genre_image**
> bytearray head_genre_image(name, image_type, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer, image_index=image_index)

Get genre image by name.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    name = 'name_example' # str | Genre name.
    image_type = jellyfin.generated.api_10_11.ImageType() # ImageType | Image type.
    tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
    format = jellyfin.generated.api_10_11.ImageFormat() # ImageFormat | Determines the output format of the image - original,gif,jpg,png. (optional)
    max_width = 56 # int | The maximum image width to return. (optional)
    max_height = 56 # int | The maximum image height to return. (optional)
    percent_played = 3.4 # float | Optional. Percent to render for the percent played overlay. (optional)
    unplayed_count = 56 # int | Optional. Unplayed count overlay to render. (optional)
    width = 56 # int | The fixed image width to return. (optional)
    height = 56 # int | The fixed image height to return. (optional)
    quality = 56 # int | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
    fill_width = 56 # int | Width of box to fill. (optional)
    fill_height = 56 # int | Height of box to fill. (optional)
    blur = 56 # int | Optional. Blur image. (optional)
    background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
    foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)
    image_index = 56 # int | Image index. (optional)

    try:
        # Get genre image by name.
        api_response = api_instance.head_genre_image(name, image_type, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer, image_index=image_index)
        print("The response of ImageApi->head_genre_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->head_genre_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Genre name. | 
 **image_type** | **ImageType**| Image type. | 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | **ImageFormat**| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **percent_played** | **float**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayed_count** | **int**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **fill_width** | **int**| Width of box to fill. | [optional] 
 **fill_height** | **int**| Height of box to fill. | [optional] 
 **blur** | **int**| Optional. Blur image. | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **image_index** | **int**| Image index. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image stream returned. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_genre_image_by_index**
> bytearray head_genre_image_by_index(name, image_type, image_index, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer)

Get genre image by name.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    name = 'name_example' # str | Genre name.
    image_type = jellyfin.generated.api_10_11.ImageType() # ImageType | Image type.
    image_index = 56 # int | Image index.
    tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
    format = jellyfin.generated.api_10_11.ImageFormat() # ImageFormat | Determines the output format of the image - original,gif,jpg,png. (optional)
    max_width = 56 # int | The maximum image width to return. (optional)
    max_height = 56 # int | The maximum image height to return. (optional)
    percent_played = 3.4 # float | Optional. Percent to render for the percent played overlay. (optional)
    unplayed_count = 56 # int | Optional. Unplayed count overlay to render. (optional)
    width = 56 # int | The fixed image width to return. (optional)
    height = 56 # int | The fixed image height to return. (optional)
    quality = 56 # int | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
    fill_width = 56 # int | Width of box to fill. (optional)
    fill_height = 56 # int | Height of box to fill. (optional)
    blur = 56 # int | Optional. Blur image. (optional)
    background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
    foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)

    try:
        # Get genre image by name.
        api_response = api_instance.head_genre_image_by_index(name, image_type, image_index, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer)
        print("The response of ImageApi->head_genre_image_by_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->head_genre_image_by_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Genre name. | 
 **image_type** | **ImageType**| Image type. | 
 **image_index** | **int**| Image index. | 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | **ImageFormat**| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **percent_played** | **float**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayed_count** | **int**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **fill_width** | **int**| Width of box to fill. | [optional] 
 **fill_height** | **int**| Height of box to fill. | [optional] 
 **blur** | **int**| Optional. Blur image. | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image stream returned. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_item_image**
> bytearray head_item_image(item_id, image_type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, tag=tag, format=format, percent_played=percent_played, unplayed_count=unplayed_count, blur=blur, background_color=background_color, foreground_layer=foreground_layer, image_index=image_index)

Gets the item's image.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    item_id = 'item_id_example' # str | Item id.
    image_type = jellyfin.generated.api_10_11.ImageType() # ImageType | Image type.
    max_width = 56 # int | The maximum image width to return. (optional)
    max_height = 56 # int | The maximum image height to return. (optional)
    width = 56 # int | The fixed image width to return. (optional)
    height = 56 # int | The fixed image height to return. (optional)
    quality = 56 # int | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
    fill_width = 56 # int | Width of box to fill. (optional)
    fill_height = 56 # int | Height of box to fill. (optional)
    tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
    format = jellyfin.generated.api_10_11.ImageFormat() # ImageFormat | Optional. The MediaBrowser.Model.Drawing.ImageFormat of the returned image. (optional)
    percent_played = 3.4 # float | Optional. Percent to render for the percent played overlay. (optional)
    unplayed_count = 56 # int | Optional. Unplayed count overlay to render. (optional)
    blur = 56 # int | Optional. Blur image. (optional)
    background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
    foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)
    image_index = 56 # int | Image index. (optional)

    try:
        # Gets the item's image.
        api_response = api_instance.head_item_image(item_id, image_type, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, tag=tag, format=format, percent_played=percent_played, unplayed_count=unplayed_count, blur=blur, background_color=background_color, foreground_layer=foreground_layer, image_index=image_index)
        print("The response of ImageApi->head_item_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->head_item_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item id. | 
 **image_type** | **ImageType**| Image type. | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **fill_width** | **int**| Width of box to fill. | [optional] 
 **fill_height** | **int**| Height of box to fill. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | **ImageFormat**| Optional. The MediaBrowser.Model.Drawing.ImageFormat of the returned image. | [optional] 
 **percent_played** | **float**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayed_count** | **int**| Optional. Unplayed count overlay to render. | [optional] 
 **blur** | **int**| Optional. Blur image. | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **image_index** | **int**| Image index. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image stream returned. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_item_image2**
> bytearray head_item_image2(item_id, image_type, max_width, max_height, tag, format, percent_played, unplayed_count, image_index, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer)

Gets the item's image.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    item_id = 'item_id_example' # str | Item id.
    image_type = jellyfin.generated.api_10_11.ImageType() # ImageType | Image type.
    max_width = 56 # int | The maximum image width to return.
    max_height = 56 # int | The maximum image height to return.
    tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers.
    format = jellyfin.generated.api_10_11.ImageFormat() # ImageFormat | Determines the output format of the image - original,gif,jpg,png.
    percent_played = 3.4 # float | Optional. Percent to render for the percent played overlay.
    unplayed_count = 56 # int | Optional. Unplayed count overlay to render.
    image_index = 56 # int | Image index.
    width = 56 # int | The fixed image width to return. (optional)
    height = 56 # int | The fixed image height to return. (optional)
    quality = 56 # int | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
    fill_width = 56 # int | Width of box to fill. (optional)
    fill_height = 56 # int | Height of box to fill. (optional)
    blur = 56 # int | Optional. Blur image. (optional)
    background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
    foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)

    try:
        # Gets the item's image.
        api_response = api_instance.head_item_image2(item_id, image_type, max_width, max_height, tag, format, percent_played, unplayed_count, image_index, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer)
        print("The response of ImageApi->head_item_image2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->head_item_image2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item id. | 
 **image_type** | **ImageType**| Image type. | 
 **max_width** | **int**| The maximum image width to return. | 
 **max_height** | **int**| The maximum image height to return. | 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | 
 **format** | **ImageFormat**| Determines the output format of the image - original,gif,jpg,png. | 
 **percent_played** | **float**| Optional. Percent to render for the percent played overlay. | 
 **unplayed_count** | **int**| Optional. Unplayed count overlay to render. | 
 **image_index** | **int**| Image index. | 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **fill_width** | **int**| Width of box to fill. | [optional] 
 **fill_height** | **int**| Height of box to fill. | [optional] 
 **blur** | **int**| Optional. Blur image. | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image stream returned. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_item_image_by_index**
> bytearray head_item_image_by_index(item_id, image_type, image_index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, tag=tag, format=format, percent_played=percent_played, unplayed_count=unplayed_count, blur=blur, background_color=background_color, foreground_layer=foreground_layer)

Gets the item's image.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    item_id = 'item_id_example' # str | Item id.
    image_type = jellyfin.generated.api_10_11.ImageType() # ImageType | Image type.
    image_index = 56 # int | Image index.
    max_width = 56 # int | The maximum image width to return. (optional)
    max_height = 56 # int | The maximum image height to return. (optional)
    width = 56 # int | The fixed image width to return. (optional)
    height = 56 # int | The fixed image height to return. (optional)
    quality = 56 # int | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
    fill_width = 56 # int | Width of box to fill. (optional)
    fill_height = 56 # int | Height of box to fill. (optional)
    tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
    format = jellyfin.generated.api_10_11.ImageFormat() # ImageFormat | Optional. The MediaBrowser.Model.Drawing.ImageFormat of the returned image. (optional)
    percent_played = 3.4 # float | Optional. Percent to render for the percent played overlay. (optional)
    unplayed_count = 56 # int | Optional. Unplayed count overlay to render. (optional)
    blur = 56 # int | Optional. Blur image. (optional)
    background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
    foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)

    try:
        # Gets the item's image.
        api_response = api_instance.head_item_image_by_index(item_id, image_type, image_index, max_width=max_width, max_height=max_height, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, tag=tag, format=format, percent_played=percent_played, unplayed_count=unplayed_count, blur=blur, background_color=background_color, foreground_layer=foreground_layer)
        print("The response of ImageApi->head_item_image_by_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->head_item_image_by_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item id. | 
 **image_type** | **ImageType**| Image type. | 
 **image_index** | **int**| Image index. | 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **fill_width** | **int**| Width of box to fill. | [optional] 
 **fill_height** | **int**| Height of box to fill. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | **ImageFormat**| Optional. The MediaBrowser.Model.Drawing.ImageFormat of the returned image. | [optional] 
 **percent_played** | **float**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayed_count** | **int**| Optional. Unplayed count overlay to render. | [optional] 
 **blur** | **int**| Optional. Blur image. | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image stream returned. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_music_genre_image**
> bytearray head_music_genre_image(name, image_type, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer, image_index=image_index)

Get music genre image by name.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    name = 'name_example' # str | Music genre name.
    image_type = jellyfin.generated.api_10_11.ImageType() # ImageType | Image type.
    tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
    format = jellyfin.generated.api_10_11.ImageFormat() # ImageFormat | Determines the output format of the image - original,gif,jpg,png. (optional)
    max_width = 56 # int | The maximum image width to return. (optional)
    max_height = 56 # int | The maximum image height to return. (optional)
    percent_played = 3.4 # float | Optional. Percent to render for the percent played overlay. (optional)
    unplayed_count = 56 # int | Optional. Unplayed count overlay to render. (optional)
    width = 56 # int | The fixed image width to return. (optional)
    height = 56 # int | The fixed image height to return. (optional)
    quality = 56 # int | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
    fill_width = 56 # int | Width of box to fill. (optional)
    fill_height = 56 # int | Height of box to fill. (optional)
    blur = 56 # int | Optional. Blur image. (optional)
    background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
    foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)
    image_index = 56 # int | Image index. (optional)

    try:
        # Get music genre image by name.
        api_response = api_instance.head_music_genre_image(name, image_type, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer, image_index=image_index)
        print("The response of ImageApi->head_music_genre_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->head_music_genre_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Music genre name. | 
 **image_type** | **ImageType**| Image type. | 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | **ImageFormat**| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **percent_played** | **float**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayed_count** | **int**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **fill_width** | **int**| Width of box to fill. | [optional] 
 **fill_height** | **int**| Height of box to fill. | [optional] 
 **blur** | **int**| Optional. Blur image. | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **image_index** | **int**| Image index. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image stream returned. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_music_genre_image_by_index**
> bytearray head_music_genre_image_by_index(name, image_type, image_index, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer)

Get music genre image by name.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    name = 'name_example' # str | Music genre name.
    image_type = jellyfin.generated.api_10_11.ImageType() # ImageType | Image type.
    image_index = 56 # int | Image index.
    tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
    format = jellyfin.generated.api_10_11.ImageFormat() # ImageFormat | Determines the output format of the image - original,gif,jpg,png. (optional)
    max_width = 56 # int | The maximum image width to return. (optional)
    max_height = 56 # int | The maximum image height to return. (optional)
    percent_played = 3.4 # float | Optional. Percent to render for the percent played overlay. (optional)
    unplayed_count = 56 # int | Optional. Unplayed count overlay to render. (optional)
    width = 56 # int | The fixed image width to return. (optional)
    height = 56 # int | The fixed image height to return. (optional)
    quality = 56 # int | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
    fill_width = 56 # int | Width of box to fill. (optional)
    fill_height = 56 # int | Height of box to fill. (optional)
    blur = 56 # int | Optional. Blur image. (optional)
    background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
    foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)

    try:
        # Get music genre image by name.
        api_response = api_instance.head_music_genre_image_by_index(name, image_type, image_index, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer)
        print("The response of ImageApi->head_music_genre_image_by_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->head_music_genre_image_by_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Music genre name. | 
 **image_type** | **ImageType**| Image type. | 
 **image_index** | **int**| Image index. | 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | **ImageFormat**| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **percent_played** | **float**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayed_count** | **int**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **fill_width** | **int**| Width of box to fill. | [optional] 
 **fill_height** | **int**| Height of box to fill. | [optional] 
 **blur** | **int**| Optional. Blur image. | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image stream returned. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_person_image**
> bytearray head_person_image(name, image_type, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer, image_index=image_index)

Get person image by name.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    name = 'name_example' # str | Person name.
    image_type = jellyfin.generated.api_10_11.ImageType() # ImageType | Image type.
    tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
    format = jellyfin.generated.api_10_11.ImageFormat() # ImageFormat | Determines the output format of the image - original,gif,jpg,png. (optional)
    max_width = 56 # int | The maximum image width to return. (optional)
    max_height = 56 # int | The maximum image height to return. (optional)
    percent_played = 3.4 # float | Optional. Percent to render for the percent played overlay. (optional)
    unplayed_count = 56 # int | Optional. Unplayed count overlay to render. (optional)
    width = 56 # int | The fixed image width to return. (optional)
    height = 56 # int | The fixed image height to return. (optional)
    quality = 56 # int | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
    fill_width = 56 # int | Width of box to fill. (optional)
    fill_height = 56 # int | Height of box to fill. (optional)
    blur = 56 # int | Optional. Blur image. (optional)
    background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
    foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)
    image_index = 56 # int | Image index. (optional)

    try:
        # Get person image by name.
        api_response = api_instance.head_person_image(name, image_type, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer, image_index=image_index)
        print("The response of ImageApi->head_person_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->head_person_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Person name. | 
 **image_type** | **ImageType**| Image type. | 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | **ImageFormat**| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **percent_played** | **float**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayed_count** | **int**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **fill_width** | **int**| Width of box to fill. | [optional] 
 **fill_height** | **int**| Height of box to fill. | [optional] 
 **blur** | **int**| Optional. Blur image. | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **image_index** | **int**| Image index. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image stream returned. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_person_image_by_index**
> bytearray head_person_image_by_index(name, image_type, image_index, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer)

Get person image by name.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    name = 'name_example' # str | Person name.
    image_type = jellyfin.generated.api_10_11.ImageType() # ImageType | Image type.
    image_index = 56 # int | Image index.
    tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
    format = jellyfin.generated.api_10_11.ImageFormat() # ImageFormat | Determines the output format of the image - original,gif,jpg,png. (optional)
    max_width = 56 # int | The maximum image width to return. (optional)
    max_height = 56 # int | The maximum image height to return. (optional)
    percent_played = 3.4 # float | Optional. Percent to render for the percent played overlay. (optional)
    unplayed_count = 56 # int | Optional. Unplayed count overlay to render. (optional)
    width = 56 # int | The fixed image width to return. (optional)
    height = 56 # int | The fixed image height to return. (optional)
    quality = 56 # int | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
    fill_width = 56 # int | Width of box to fill. (optional)
    fill_height = 56 # int | Height of box to fill. (optional)
    blur = 56 # int | Optional. Blur image. (optional)
    background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
    foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)

    try:
        # Get person image by name.
        api_response = api_instance.head_person_image_by_index(name, image_type, image_index, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer)
        print("The response of ImageApi->head_person_image_by_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->head_person_image_by_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Person name. | 
 **image_type** | **ImageType**| Image type. | 
 **image_index** | **int**| Image index. | 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | **ImageFormat**| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **percent_played** | **float**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayed_count** | **int**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **fill_width** | **int**| Width of box to fill. | [optional] 
 **fill_height** | **int**| Height of box to fill. | [optional] 
 **blur** | **int**| Optional. Blur image. | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image stream returned. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_studio_image**
> bytearray head_studio_image(name, image_type, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer, image_index=image_index)

Get studio image by name.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    name = 'name_example' # str | Studio name.
    image_type = jellyfin.generated.api_10_11.ImageType() # ImageType | Image type.
    tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
    format = jellyfin.generated.api_10_11.ImageFormat() # ImageFormat | Determines the output format of the image - original,gif,jpg,png. (optional)
    max_width = 56 # int | The maximum image width to return. (optional)
    max_height = 56 # int | The maximum image height to return. (optional)
    percent_played = 3.4 # float | Optional. Percent to render for the percent played overlay. (optional)
    unplayed_count = 56 # int | Optional. Unplayed count overlay to render. (optional)
    width = 56 # int | The fixed image width to return. (optional)
    height = 56 # int | The fixed image height to return. (optional)
    quality = 56 # int | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
    fill_width = 56 # int | Width of box to fill. (optional)
    fill_height = 56 # int | Height of box to fill. (optional)
    blur = 56 # int | Optional. Blur image. (optional)
    background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
    foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)
    image_index = 56 # int | Image index. (optional)

    try:
        # Get studio image by name.
        api_response = api_instance.head_studio_image(name, image_type, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer, image_index=image_index)
        print("The response of ImageApi->head_studio_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->head_studio_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Studio name. | 
 **image_type** | **ImageType**| Image type. | 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | **ImageFormat**| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **percent_played** | **float**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayed_count** | **int**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **fill_width** | **int**| Width of box to fill. | [optional] 
 **fill_height** | **int**| Height of box to fill. | [optional] 
 **blur** | **int**| Optional. Blur image. | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **image_index** | **int**| Image index. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image stream returned. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_studio_image_by_index**
> bytearray head_studio_image_by_index(name, image_type, image_index, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer)

Get studio image by name.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    name = 'name_example' # str | Studio name.
    image_type = jellyfin.generated.api_10_11.ImageType() # ImageType | Image type.
    image_index = 56 # int | Image index.
    tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
    format = jellyfin.generated.api_10_11.ImageFormat() # ImageFormat | Determines the output format of the image - original,gif,jpg,png. (optional)
    max_width = 56 # int | The maximum image width to return. (optional)
    max_height = 56 # int | The maximum image height to return. (optional)
    percent_played = 3.4 # float | Optional. Percent to render for the percent played overlay. (optional)
    unplayed_count = 56 # int | Optional. Unplayed count overlay to render. (optional)
    width = 56 # int | The fixed image width to return. (optional)
    height = 56 # int | The fixed image height to return. (optional)
    quality = 56 # int | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. (optional)
    fill_width = 56 # int | Width of box to fill. (optional)
    fill_height = 56 # int | Height of box to fill. (optional)
    blur = 56 # int | Optional. Blur image. (optional)
    background_color = 'background_color_example' # str | Optional. Apply a background color for transparent images. (optional)
    foreground_layer = 'foreground_layer_example' # str | Optional. Apply a foreground layer on top of the image. (optional)

    try:
        # Get studio image by name.
        api_response = api_instance.head_studio_image_by_index(name, image_type, image_index, tag=tag, format=format, max_width=max_width, max_height=max_height, percent_played=percent_played, unplayed_count=unplayed_count, width=width, height=height, quality=quality, fill_width=fill_width, fill_height=fill_height, blur=blur, background_color=background_color, foreground_layer=foreground_layer)
        print("The response of ImageApi->head_studio_image_by_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->head_studio_image_by_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Studio name. | 
 **image_type** | **ImageType**| Image type. | 
 **image_index** | **int**| Image index. | 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | **ImageFormat**| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **max_width** | **int**| The maximum image width to return. | [optional] 
 **max_height** | **int**| The maximum image height to return. | [optional] 
 **percent_played** | **float**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayed_count** | **int**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **int**| The fixed image width to return. | [optional] 
 **height** | **int**| The fixed image height to return. | [optional] 
 **quality** | **int**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **fill_width** | **int**| Width of box to fill. | [optional] 
 **fill_height** | **int**| Height of box to fill. | [optional] 
 **blur** | **int**| Optional. Blur image. | [optional] 
 **background_color** | **str**| Optional. Apply a background color for transparent images. | [optional] 
 **foreground_layer** | **str**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image stream returned. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_user_image**
> bytearray head_user_image(user_id=user_id, tag=tag, format=format)

Get user profile image.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    user_id = 'user_id_example' # str | User id. (optional)
    tag = 'tag_example' # str | Optional. Supply the cache tag from the item object to receive strong caching headers. (optional)
    format = jellyfin.generated.api_10_11.ImageFormat() # ImageFormat | Determines the output format of the image - original,gif,jpg,png. (optional)

    try:
        # Get user profile image.
        api_response = api_instance.head_user_image(user_id=user_id, tag=tag, format=format)
        print("The response of ImageApi->head_user_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->head_user_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User id. | [optional] 
 **tag** | **str**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | **ImageFormat**| Determines the output format of the image - original,gif,jpg,png. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image stream returned. |  -  |
**400** | User id not provided. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_user_image**
> post_user_image(user_id=user_id, body=body)

Sets the user image.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    user_id = 'user_id_example' # str | User Id. (optional)
    body = None # bytearray |  (optional)

    try:
        # Sets the user image.
        api_instance.post_user_image(user_id=user_id, body=body)
    except Exception as e:
        print("Exception when calling ImageApi->post_user_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id. | [optional] 
 **body** | **bytearray**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: image/*
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Image updated. |  -  |
**400** | Bad Request |  -  |
**403** | User does not have permission to delete the image. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_item_image**
> set_item_image(item_id, image_type, body=body)

Set item image.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    item_id = 'item_id_example' # str | Item id.
    image_type = jellyfin.generated.api_10_11.ImageType() # ImageType | Image type.
    body = None # bytearray |  (optional)

    try:
        # Set item image.
        api_instance.set_item_image(item_id, image_type, body=body)
    except Exception as e:
        print("Exception when calling ImageApi->set_item_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item id. | 
 **image_type** | **ImageType**| Image type. | 
 **body** | **bytearray**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: image/*
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Image saved. |  -  |
**400** | Bad Request |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_item_image_by_index**
> set_item_image_by_index(item_id, image_type, image_index, body=body)

Set item image.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    item_id = 'item_id_example' # str | Item id.
    image_type = jellyfin.generated.api_10_11.ImageType() # ImageType | Image type.
    image_index = 56 # int | (Unused) Image index.
    body = None # bytearray |  (optional)

    try:
        # Set item image.
        api_instance.set_item_image_by_index(item_id, image_type, image_index, body=body)
    except Exception as e:
        print("Exception when calling ImageApi->set_item_image_by_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item id. | 
 **image_type** | **ImageType**| Image type. | 
 **image_index** | **int**| (Unused) Image index. | 
 **body** | **bytearray**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: image/*
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Image saved. |  -  |
**400** | Bad Request |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_image_index**
> update_item_image_index(item_id, image_type, image_index, new_index)

Updates the index for an item image.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    item_id = 'item_id_example' # str | Item id.
    image_type = jellyfin.generated.api_10_11.ImageType() # ImageType | Image type.
    image_index = 56 # int | Old image index.
    new_index = 56 # int | New image index.

    try:
        # Updates the index for an item image.
        api_instance.update_item_image_index(item_id, image_type, image_index, new_index)
    except Exception as e:
        print("Exception when calling ImageApi->update_item_image_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item id. | 
 **image_type** | **ImageType**| Image type. | 
 **image_index** | **int**| Old image index. | 
 **new_index** | **int**| New image index. | 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Image index updated. |  -  |
**404** | Item not found. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_custom_splashscreen**
> upload_custom_splashscreen(body=body)

Uploads a custom splashscreen.  The body is expected to the image contents base64 encoded.

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
    api_instance = jellyfin.generated.api_10_11.ImageApi(api_client)
    body = None # bytearray |  (optional)

    try:
        # Uploads a custom splashscreen.  The body is expected to the image contents base64 encoded.
        api_instance.upload_custom_splashscreen(body=body)
    except Exception as e:
        print("Exception when calling ImageApi->upload_custom_splashscreen: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **bytearray**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: image/*
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully uploaded new splashscreen. |  -  |
**400** | Error reading MimeType from uploaded image. |  -  |
**403** | User does not have permission to upload splashscreen.. |  -  |
**503** | The server is currently starting or is temporarily not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

