# ClientLogDocumentResponseDto

Client log document response dto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | Gets the resulting filename. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.client_log_document_response_dto import ClientLogDocumentResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ClientLogDocumentResponseDto from a JSON string
client_log_document_response_dto_instance = ClientLogDocumentResponseDto.from_json(json)
# print the JSON string representation of the object
print(ClientLogDocumentResponseDto.to_json())

# convert the object into a dict
client_log_document_response_dto_dict = client_log_document_response_dto_instance.to_dict()
# create an instance of ClientLogDocumentResponseDto from a dict
client_log_document_response_dto_from_dict = ClientLogDocumentResponseDto.from_dict(client_log_document_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


