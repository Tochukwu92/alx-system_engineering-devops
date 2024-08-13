#!/usr/bin/python3

"""Function that return title of all articles of a given subreddit"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    function that queries the Reddit API and returns a
    list containing the titles of all hot articles for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {'User-Agent': 'Mozilla/5.0'}

    params = {'limit': 100}

    if after:
        params['after'] = after

    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)

    Data = response.json()

    posts = Data['data']['children']

    for post in posts:  # loop through the posts list

        hot_list.append(post['data']['title'])

    after = Data['data']['after']

    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
