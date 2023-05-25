#!/usr/bin/python3
"""
1-export_to_CSV module
python script to export data in the CSV format.
"""
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
    filename = '{}.csv'.format(user_id)
    with open(filename, mode='w') as f:
        for obj in json_obj:
            f.write('"{}","{}","{}","{}"\n'
                    .format(user_id, user_name,
                            obj.get('completed'), obj.get('title')))
