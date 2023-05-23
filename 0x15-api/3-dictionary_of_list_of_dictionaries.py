#!/usr/bin/python3
"""
0-gather_data_from_an_API.py module
Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress."""

from json import dump
from requests import get

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/'
    response = get(url)

    json_users = response.json()
    my_dict = {}
    for user in json_users:
        user_name = user.get('name')
        user_id = user.get('id')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'
        response = get(url)
        json_obj = response.json()
        my_dict[user_id] = []
        filename = 'todo_all_employees.json'
        for obj in json_obj:
            my_dict[user_id].append({
                                    "task": obj.get('title'),
                                    "completed": obj.get('completed'),
                                    "username": user_name
                                    })
    with open(filename, "w") as json_file:
        dump(my_dict, json_file)
