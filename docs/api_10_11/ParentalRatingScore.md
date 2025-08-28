# ParentalRatingScore

A class representing an parental rating score.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **int** | Gets or sets the score. | [optional] 
**sub_score** | **int** | Gets or sets the sub score. | [optional] 

## Example

```python
from jellyfin.generated.api_10_11.models.parental_rating_score import ParentalRatingScore

# TODO update the JSON string below
json = "{}"
# create an instance of ParentalRatingScore from a JSON string
parental_rating_score_instance = ParentalRatingScore.from_json(json)
# print the JSON string representation of the object
print(ParentalRatingScore.to_json())

# convert the object into a dict
parental_rating_score_dict = parental_rating_score_instance.to_dict()
# create an instance of ParentalRatingScore from a dict
parental_rating_score_from_dict = ParentalRatingScore.from_dict(parental_rating_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


