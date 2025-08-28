# ServerDiscoveryInfo

The server discovery info model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Gets the address. | [optional] 
**id** | **str** | Gets the server identifier. | [optional] 
**name** | **str** | Gets the name. | [optional] 
**endpoint_address** | **str** | Gets the endpoint address. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.server_discovery_info import ServerDiscoveryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ServerDiscoveryInfo from a JSON string
server_discovery_info_instance = ServerDiscoveryInfo.from_json(json)
# print the JSON string representation of the object
print(ServerDiscoveryInfo.to_json())

# convert the object into a dict
server_discovery_info_dict = server_discovery_info_instance.to_dict()
# create an instance of ServerDiscoveryInfo from a dict
server_discovery_info_from_dict = ServerDiscoveryInfo.from_dict(server_discovery_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


