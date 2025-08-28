# QueueRequestDto

Class QueueRequestDto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_ids** | **List[str]** | Gets or sets the items to enqueue. | [optional] 
**mode** | [**GroupQueueMode**](GroupQueueMode.md) | Gets or sets the mode in which to add the new items. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.queue_request_dto import QueueRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of QueueRequestDto from a JSON string
queue_request_dto_instance = QueueRequestDto.from_json(json)
# print the JSON string representation of the object
print(QueueRequestDto.to_json())

# convert the object into a dict
queue_request_dto_dict = queue_request_dto_instance.to_dict()
# create an instance of QueueRequestDto from a dict
queue_request_dto_from_dict = QueueRequestDto.from_dict(queue_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


