#!/usr/bin/python3


import requests


def recurse(subreddit, hot_list=[], after=None):
    """

    """
    headers = {'User-Agent': 'Reddit Hot Articles Fetcher'}

    #  API request to get hot articles from the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    params = {'limit': 100, 'after': after}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False)

    #  Check if the subreddit is valid
    if response.status_code != 200:
        return None

    data = response.json().get('data')

    #  If there is no data, return None
    if not data:
        return None

    #  Append titles to the hot_list
    posts = data.get('children', [])
    for post in posts:
        hot_list.append(post['data']['title'])

    #  Check for pagination (if there's a next page)
    after = data.get('after')
    if after:
        #  Recursively call recurse with the next page
        return recurse(subreddit, hot_list, after)
    else:
        #  If no more pages, return the accumulated list
        return hot_list
