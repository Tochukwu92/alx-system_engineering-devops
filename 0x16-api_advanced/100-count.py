#!/usr/bin/python3


"""Recursive function that querries Reddit API"""


import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """

    """
    #  Setting the User-Agent to prevent the request from being blocked
    headers = {'User-Agent': 'Reddit Keyword Counter'}

    #  Make the API request to get the hot posts in the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100, 'after': after}
    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)

    #  Check if the subreddit is valid
    if response.status_code != 200:
        return

    data = response.json().get('data')

    #  If there is no data, return
    if not data:
        return

    #  Extract the list of posts from the response
    posts = data.get('children')

    for post in posts:
        title = post['data']['title'].lower()

        #  Count the occurrences of each keyword in the title
        for word in word_list:
            count = title.split().count(word.lower())
            if count > 0:
                if word.lower() in word_count:
                    word_count[word.lower()] += count
                else:
                    word_count[word.lower()] = count

    #  Check if there is a next page (pagination)
    after = data.get('after')

    if after:
        #  Recursively call the function with the next page
        return count_words(subreddit, word_list, after, word_count)
    else:
        #  Sort the dictionary by value in desc order, then by key in asc order
        sorted_words = sorted(
                word_count.items(), key=lambda kv: (-kv[1], kv[0]))

        #  Print the results
        for word, count in sorted_words:
            print(f"{word}: {count}")
