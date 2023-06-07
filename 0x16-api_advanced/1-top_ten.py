#!/usr/bin/python3
"""1-top_ten"""
import requests


def top_ten(subreddit):
    """ queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    # setting a custom User-Agent.Avoids error - Too many request
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        data = response.json()

        if 'data' in data and 'children' in data['data']:
            child = data['data']['children']

            for post in child[:10]:
                title_post = post['data']['title']
                print(title_post)
    except request.exceptions.RequestException:
        print('None')
