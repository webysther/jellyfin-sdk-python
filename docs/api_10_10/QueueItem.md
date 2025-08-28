# QueueItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**playlist_item_id** | **str** |  | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.queue_item import QueueItem

# TODO update the JSON string below
json = "{}"
# create an instance of QueueItem from a JSON string
queue_item_instance = QueueItem.from_json(json)
# print the JSON string representation of the object
print(QueueItem.to_json())

# convert the object into a dict
queue_item_dict = queue_item_instance.to_dict()
# create an instance of QueueItem from a dict
queue_item_from_dict = QueueItem.from_dict(queue_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


