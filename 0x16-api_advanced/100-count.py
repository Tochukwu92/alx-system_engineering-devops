#!/usr/bin/python3


'''Recursive function that querry reddit api'''


import requests
from collections import Counter


def rec_count_words(
        subreddit, word_list, word_count=Counter(), after=None):
    """

    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {'User-Agent': 'Mozilla/5.0'}

    params = {'limit': 10}

    if after:
        params['after'] = after

    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)

    dict_obj = response.json()

    posts = dict_obj['data']['children']

    for post in posts:
        title = post['data']['title']
        words = title.split()
        for word in words:
            normal_wd = word.lower().strip(".!,_?")
            if normal_wd in word_list:
                word_count[normal_wd] += 1

    after = dict_obj['data']['after']
    if after:
        return rec_count_words(subreddit, word_list, word_count, after)
    else:
        return word_count


def count_words(subreddit, word_list):
    '''

    '''
    word_list = [word.lower() for word in word_list]

    word_count = rec_count_words(subreddit, word_list)
    if not word_count:
        return

    sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_word_count:
        print(f"{word}: {count}")
