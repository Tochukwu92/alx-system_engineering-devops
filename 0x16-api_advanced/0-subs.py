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

    data = response.json()

    result = data['data']['subscribers']
    return result
