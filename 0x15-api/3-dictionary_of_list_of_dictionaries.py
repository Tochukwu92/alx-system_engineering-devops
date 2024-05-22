#!/usr/bin/env python3

import json
import requests


def fetch_usr_data():
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    Data = {}

    for user in users:
        user_id = user["id"]

        todos = requests.get(url + "todos?userId={}".format(user_id)).json()
        Data[user_id] = []
        for todo in todos:
            task_info = {
                    "username": user.get("username"),
                    "task": todo.get("title"),
                    "completed": todo.get("completed")
            }
            Data[user_id].append(task_info)
    return Data


if __name__ == "__main__":
    data = fetch_usr_data()
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)
