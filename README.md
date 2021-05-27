# youtube_search

Python function for searching for youtube videos to avoid using their heavily rate-limited API

To avoid using the API, this uses the form on the youtube homepage and scrapes the resulting page.

## Example Usage

Example based on this fork with additional filters:

```python
from youtube_search import YoutubeSearch, YouTubeSearchOptions

# possible upload_date values:
#
# YouTubeSearchOptions.LAST_HOUR
# YouTubeSearchOptions.TODAY
# YouTubeSearchOptions.THIS_WEEK
# YouTubeSearchOptions.THIS_MONTH
# YouTubeSearchOptions.THIS_YEAR

results = YoutubeSearch(search_terms='my search term', upload_date=YouTubeSearchOptions.LAST_HOUR, max_results=10).to_dict()

for video in results:
    print(video['url_suffix']);
    print(video['title']);
    print(video['long_desc']);
    print(video['channel']);
    print(video['duration']);
    print(video['views']);
    print("=========");
```

For a basic search (and all of the current functionality), you can use the search tool as follows:

```pip install youtube-search```

```python
from youtube_search import YoutubeSearch

results = YoutubeSearch('search terms', max_results=10).to_json()

print(results)

# returns a json string

########################################

results = YoutubeSearch('search terms', max_results=10).to_dict()

print(results)
# returns a dictionary
```
