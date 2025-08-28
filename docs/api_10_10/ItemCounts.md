# ItemCounts

Class LibrarySummary.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**movie_count** | **int** | Gets or sets the movie count. | [optional] 
**series_count** | **int** | Gets or sets the series count. | [optional] 
**episode_count** | **int** | Gets or sets the episode count. | [optional] 
**artist_count** | **int** | Gets or sets the artist count. | [optional] 
**program_count** | **int** | Gets or sets the program count. | [optional] 
**trailer_count** | **int** | Gets or sets the trailer count. | [optional] 
**song_count** | **int** | Gets or sets the song count. | [optional] 
**album_count** | **int** | Gets or sets the album count. | [optional] 
**music_video_count** | **int** | Gets or sets the music video count. | [optional] 
**box_set_count** | **int** | Gets or sets the box set count. | [optional] 
**book_count** | **int** | Gets or sets the book count. | [optional] 
**item_count** | **int** | Gets or sets the item count. | [optional] 

## Example

```python
from jellyfin.generated.api_10_10.models.item_counts import ItemCounts

# TODO update the JSON string below
json = "{}"
# create an instance of ItemCounts from a JSON string
item_counts_instance = ItemCounts.from_json(json)
# print the JSON string representation of the object
print(ItemCounts.to_json())

# convert the object into a dict
item_counts_dict = item_counts_instance.to_dict()
# create an instance of ItemCounts from a dict
item_counts_from_dict = ItemCounts.from_dict(item_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


