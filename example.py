#!/usr/bin/env python3
 
from youtube_search import YoutubeSearch, YouTubeSearchOptions

results = YoutubeSearch(search_terms='my search term', upload_date=YouTubeSearchOptions.LAST_HOUR, max_results=10).to_dict()

for video in results:
    print(video['url_suffix']);
    print(video['title']);
    print(video['long_desc']);
    print(video['channel']);
    print(video['duration']);
    print(video['views']);
    print("=========");

