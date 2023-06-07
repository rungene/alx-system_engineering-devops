#!/usr/bin/python3
"""0-subs"""
import requests


def number_of_subscribers(subreddit):
    """Recursive function queries the Reddit API and returns
    the number of subscribers (not active users, total subscribers)
    for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    # setting a custom User-Agent.Avoids error - Too many request
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']

    except request.exceptions.RequestException:
        pass

    return 0
