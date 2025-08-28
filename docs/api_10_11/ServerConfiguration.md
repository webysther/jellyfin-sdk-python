# ServerConfiguration

Represents the server configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_file_retention_days** | **int** | Gets or sets the number of days we should retain log files. | [optional] 
**is_startup_wizard_completed** | **bool** | Gets or sets a value indicating whether this instance is first run. | [optional] 
**cache_path** | **str** | Gets or sets the cache path. | [optional] 
**previous_version** | **str** | Gets or sets the last known version that was ran using the configuration. | [optional] 
**previous_version_str** | **str** | Gets or sets the stringified PreviousVersion to be stored/loaded,  because System.Version itself isn&#39;t xml-serializable. | [optional] 
**enable_metrics** | **bool** | Gets or sets a value indicating whether to enable prometheus metrics exporting. | [optional] 
**enable_normalized_item_by_name_ids** | **bool** |  | [optional] 
**is_port_authorized** | **bool** | Gets or sets a value indicating whether this instance is port authorized. | [optional] 
**quick_connect_available** | **bool** | Gets or sets a value indicating whether quick connect is available for use on this server. | [optional] 
**enable_case_sensitive_item_ids** | **bool** | Gets or sets a value indicating whether [enable case-sensitive item ids]. | [optional] 
**disable_live_tv_channel_user_data_name** | **bool** |  | [optional] 
**metadata_path** | **str** | Gets or sets the metadata path. | [optional] 
**preferred_metadata_language** | **str** | Gets or sets the preferred metadata language. | [optional] 
**metadata_country_code** | **str** | Gets or sets the metadata country code. | [optional] 
**sort_replace_characters** | **List[str]** | Gets or sets characters to be replaced with a &#39; &#39; in strings to create a sort name. | [optional] 
**sort_remove_characters** | **List[str]** | Gets or sets characters to be removed from strings to create a sort name. | [optional] 
**sort_remove_words** | **List[str]** | Gets or sets words to be removed from strings to create a sort name. | [optional] 
**min_resume_pct** | **int** | Gets or sets the minimum percentage of an item that must be played in order for playstate to be updated. | [optional] 
**max_resume_pct** | **int** | Gets or sets the maximum percentage of an item that can be played while still saving playstate. If this percentage is crossed playstate will be reset to the beginning and the item will be marked watched. | [optional] 
**min_resume_duration_seconds** | **int** | Gets or sets the minimum duration that an item must have in order to be eligible for playstate updates.. | [optional] 
**min_audiobook_resume** | **int** | Gets or sets the minimum minutes of a book that must be played in order for playstate to be updated. | [optional] 
**max_audiobook_resume** | **int** | Gets or sets the remaining minutes of a book that can be played while still saving playstate. If this percentage is crossed playstate will be reset to the beginning and the item will be marked watched. | [optional] 
**inactive_session_threshold** | **int** | Gets or sets the threshold in minutes after a inactive session gets closed automatically.  If set to 0 the check for inactive sessions gets disabled. | [optional] 
**library_monitor_delay** | **int** | Gets or sets the delay in seconds that we will wait after a file system change to try and discover what has been added/removed  Some delay is necessary with some items because their creation is not atomic.  It involves the creation of several  different directories and files. | [optional] 
**library_update_duration** | **int** | Gets or sets the duration in seconds that we will wait after a library updated event before executing the library changed notification. | [optional] 
**cache_size** | **int** | Gets or sets the maximum amount of items to cache. | [optional] 
**image_saving_convention** | [**ImageSavingConvention**](ImageSavingConvention.md) | Gets or sets the image saving convention. | [optional] 
**metadata_options** | [**List[MetadataOptions]**](MetadataOptions.md) |  | [optional] 
**skip_deserialization_for_basic_types** | **bool** |  | [optional] 
**server_name** | **str** |  | [optional] 
**ui_culture** | **str** |  | [optional] 
**save_metadata_hidden** | **bool** |  | [optional] 
**content_types** | [**List[NameValuePair]**](NameValuePair.md) |  | [optional] 
**remote_client_bitrate_limit** | **int** |  | [optional] 
**enable_folder_view** | **bool** |  | [optional] 
**enable_grouping_movies_into_collections** | **bool** |  | [optional] 
**enable_grouping_shows_into_collections** | **bool** |  | [optional] 
**display_specials_within_seasons** | **bool** |  | [optional] 
**codecs_used** | **List[str]** |  | [optional] 
**plugin_repositories** | [**List[RepositoryInfo]**](RepositoryInfo.md) |  | [optional] 
**enable_external_content_in_suggestions** | **bool** |  | [optional] 
**image_extraction_timeout_ms** | **int** |  | [optional] 
**path_substitutions** | [**List[PathSubstitution]**](PathSubstitution.md) |  | [optional] 
**enable_slow_response_warning** | **bool** | Gets or sets a value indicating whether slow server responses should be logged as a warning. | [optional] 
**slow_response_threshold_ms** | **int** | Gets or sets the threshold for the slow response time warning in ms. | [optional] 
**cors_hosts** | **List[str]** | Gets or sets the cors hosts. | [optional] 
**activity_log_retention_days** | **int** | Gets or sets the number of days we should retain activity logs. | [optional] 
**library_scan_fanout_concurrency** | **int** | Gets or sets the how the library scan fans out. | [optional] 
**library_metadata_refresh_concurrency** | **int** | Gets or sets the how many metadata refreshes can run concurrently. | [optional] 
**allow_client_log_upload** | **bool** | Gets or sets a value indicating whether clients should be allowed to upload logs. | [optional] 
**dummy_chapter_duration** | **int** | Gets or sets the dummy chapter duration in seconds, use 0 (zero) or less to disable generation altogether. | [optional] 
**chapter_image_resolution** | [**ImageResolution**](ImageResolution.md) | Gets or sets the chapter image resolution. | [optional] 
**parallel_image_encoding_limit** | **int** | Gets or sets the limit for parallel image encoding. | [optional] 
**cast_receiver_applications** | [**List[CastReceiverApplication]**](CastReceiverApplication.md) | Gets or sets the list of cast receiver applications. | [optional] 
**trickplay_options** | [**TrickplayOptions**](TrickplayOptions.md) | Gets or sets the trickplay options. | [optional] 
**enable_legacy_authorization** | **bool** | Gets or sets a value indicating whether old authorization methods are allowed. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.server_configuration import ServerConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfiguration from a JSON string
server_configuration_instance = ServerConfiguration.from_json(json)
# print the JSON string representation of the object
print(ServerConfiguration.to_json())

# convert the object into a dict
server_configuration_dict = server_configuration_instance.to_dict()
# create an instance of ServerConfiguration from a dict
server_configuration_from_dict = ServerConfiguration.from_dict(server_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


