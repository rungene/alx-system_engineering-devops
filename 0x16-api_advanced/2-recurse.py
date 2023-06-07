#!/usr/bin/python3
"""2-recurse"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit.
    Args:
        subreddit: name of subreddit to query
        hot_list: list to store the titles of hot_articles
        after: The id of the next page of results, or None
        if no results were found

    Return:
        A list containing list of the hot articles, or None
        if no results are founs
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    # setting a custom User-Agent.Avoids error - Too many request
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        params = {'after': after} if after else None
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        # Check if request was successful
        if response.status_code == 200:
            # Parse json
            data = response.json()

            if 'data' in data and 'children' in data['data']:
                children = data['data']['children']

                # Add the titles of the hot artiles to the list
                for post in children:
                    title_post = post['data']['title']
                    hot_list.append(title_post)
                # Check for more pages of the result
                if ('after' in data['data'] and
                   data['data']['after'] is not None):
                    next_after = data['data']['after']
                    return recurse(subreddit, hot_list, after=next_after)
                else:
                    # Return the list for hot articles
                    return hot_list
        else:
            return None
    except requests.exceptions.RequestException:
        return None
