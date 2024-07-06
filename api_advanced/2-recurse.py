#!/usr/bin/python
"""
Reddit API module to recursively get all hot post titles of a subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Returns a list of titles of all hot posts for a subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of hot posts.
        after (str): The after parameter for pagination.

    Returns:
        list: A list of titles of all hot posts, or None if invalid.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'MyBot/1.0'}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data", {})
        hot_list += [post.get("data", {}).get("title", "None") for post in data.get("children", [])]
        after = data.get("after")
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    elif response.status_code == 404:
        return None
