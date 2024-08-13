#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subscriber"""
import requests


def number_of_subscribers(subreddit):

    """
    returns the total number of subcribers for a given
    rdddit.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Mozilla/5.0'}


    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0
    try:

        data = response.json().get('data', {})

        return data.get('subscribers', 0)

    except ValueError:
        return 0
