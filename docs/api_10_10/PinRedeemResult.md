# PinRedeemResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Gets or sets a value indicating whether this MediaBrowser.Model.Users.PinRedeemResult is success. | [optional] 
**users_reset** | **List[str]** | Gets or sets the users reset. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.pin_redeem_result import PinRedeemResult

# TODO update the JSON string below
json = "{}"
# create an instance of PinRedeemResult from a JSON string
pin_redeem_result_instance = PinRedeemResult.from_json(json)
# print the JSON string representation of the object
print(PinRedeemResult.to_json())

# convert the object into a dict
pin_redeem_result_dict = pin_redeem_result_instance.to_dict()
# create an instance of PinRedeemResult from a dict
pin_redeem_result_from_dict = PinRedeemResult.from_dict(pin_redeem_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


