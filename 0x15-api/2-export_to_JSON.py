#!/usr/bin/python3
"""
0-gather_data_from_an_API.py module
Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress."""

from json import dump
from requests import get
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = get(url)
    user_name = response.json().get('username')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    response = get(url)

    json_obj = response.json()
    my_dict = {user_id: []}
    filename = '{}.json'.format(user_id)
    for obj in json_obj:
        my_dict[user_id].append({
                                "task": obj.get('title'),
                                "completed": obj.get('completed'),
                                "username": user_name
                                })
    with open(filename, "w") as json_file:
        dump(my_dict, json_file)
