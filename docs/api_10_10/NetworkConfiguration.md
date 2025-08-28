# NetworkConfiguration

Defines the MediaBrowser.Common.Net.NetworkConfiguration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_url** | **str** | Gets or sets a value used to specify the URL prefix that your Jellyfin instance can be accessed at. | [optional] 
**enable_https** | **bool** | Gets or sets a value indicating whether to use HTTPS. | [optional] 
**require_https** | **bool** | Gets or sets a value indicating whether the server should force connections over HTTPS. | [optional] 
**certificate_path** | **str** | Gets or sets the filesystem path of an X.509 certificate to use for SSL. | [optional] 
**certificate_password** | **str** | Gets or sets the password required to access the X.509 certificate data in the file specified by MediaBrowser.Common.Net.NetworkConfiguration.CertificatePath. | [optional] 
**internal_http_port** | **int** | Gets or sets the internal HTTP server port. | [optional] 
**internal_https_port** | **int** | Gets or sets the internal HTTPS server port. | [optional] 
**public_http_port** | **int** | Gets or sets the public HTTP port. | [optional] 
**public_https_port** | **int** | Gets or sets the public HTTPS port. | [optional] 
**auto_discovery** | **bool** | Gets or sets a value indicating whether Autodiscovery is enabled. | [optional] 
**enable_upn_p** | **bool** | Gets or sets a value indicating whether to enable automatic port forwarding. | [optional] 
**enable_ipv4** | **bool** | Gets or sets a value indicating whether IPv6 is enabled. | [optional] 
**enable_ipv6** | **bool** | Gets or sets a value indicating whether IPv6 is enabled. | [optional] 
**enable_remote_access** | **bool** | Gets or sets a value indicating whether access from outside of the LAN is permitted. | [optional] 
**local_network_subnets** | **List[str]** | Gets or sets the subnets that are deemed to make up the LAN. | [optional] 
**local_network_addresses** | **List[str]** | Gets or sets the interface addresses which Jellyfin will bind to. If empty, all interfaces will be used. | [optional] 
**known_proxies** | **List[str]** | Gets or sets the known proxies. | [optional] 
**ignore_virtual_interfaces** | **bool** | Gets or sets a value indicating whether address names that match MediaBrowser.Common.Net.NetworkConfiguration.VirtualInterfaceNames should be ignored for the purposes of binding. | [optional] 
**virtual_interface_names** | **List[str]** | Gets or sets a value indicating the interface name prefixes that should be ignored. The list can be comma separated and values are case-insensitive. &lt;seealso cref&#x3D;\&quot;P:MediaBrowser.Common.Net.NetworkConfiguration.IgnoreVirtualInterfaces\&quot; /&gt;. | [optional] 
**enable_published_server_uri_by_request** | **bool** | Gets or sets a value indicating whether the published server uri is based on information in HTTP requests. | [optional] 
**published_server_uri_by_subnet** | **List[str]** | Gets or sets the PublishedServerUriBySubnet  Gets or sets PublishedServerUri to advertise for specific subnets. | [optional] 
**remote_ip_filter** | **List[str]** | Gets or sets the filter for remote IP connectivity. Used in conjunction with &lt;seealso cref&#x3D;\&quot;P:MediaBrowser.Common.Net.NetworkConfiguration.IsRemoteIPFilterBlacklist\&quot; /&gt;. | [optional] 
**is_remote_ip_filter_blacklist** | **bool** | Gets or sets a value indicating whether &lt;seealso cref&#x3D;\&quot;P:MediaBrowser.Common.Net.NetworkConfiguration.RemoteIPFilter\&quot; /&gt; contains a blacklist or a whitelist. Default is a whitelist. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.network_configuration import NetworkConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkConfiguration from a JSON string
network_configuration_instance = NetworkConfiguration.from_json(json)
# print the JSON string representation of the object
print(NetworkConfiguration.to_json())

# convert the object into a dict
network_configuration_dict = network_configuration_instance.to_dict()
# create an instance of NetworkConfiguration from a dict
network_configuration_from_dict = NetworkConfiguration.from_dict(network_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


