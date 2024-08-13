#!/usr/bin/python3

"""Function to print the titl of first 10 hot post on a given reddit"""

import requests


def top_ten(subreddit):
    '''
    queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit: the subreddit/topic to list it's top 10
    '''

    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(
                                                subreddit)

    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    try:
        if response.status_code == 200:
            data = response.json().get('data', {})
            resultes = data.get('children', None)
            for result in resultes:
                print(result['data']['title'])
            else:
                print(None)
    except ValueError:
        print(None)
