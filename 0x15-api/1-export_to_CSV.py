#!/usr/bin/python3


"""
fetch userid users todo task
"""


import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    params = {"userId": user_id}
    todos = requests.get(url + "todos", params=params).json()

    with open("{}.csv".format(user_id), mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for todo in todos:
            writer.writerow(
                    [user_id, username, todo.get(
                        "completed"), todo.get("title")])
