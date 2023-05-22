#!/usr/bin/python3
"""
0-gather_data_from_an_API.py module
Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress."""

from requests import get
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = get(url)
    user_name = response.json().get('name')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    response = get(url)

    json_obj = response.json()
    objects = []
    count_obj = 0
    for obj in json_obj:
        if obj.get('completed'):
            objects.append(obj)
            count_obj += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(user_name, count_obj, len(json_obj)))
    for obj in objects:
        print('\t {}'.format(obj.get('title')))
