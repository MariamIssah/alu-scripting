#!/usr/bin/python3
"""
Reddit API module to recursively get all hot post titles of a subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively returns a list of titles of all hot posts for a subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of hot posts.
        after (str): The after parameter for pagination.

    Returns:
        list: A list of titles of all hot posts, or None if invalid.
    """
    if not isinstance(subreddit, str):
        return None

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/126.0.0.0 Safari/537.36"
        )
    }
    params = {'after': after}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return None

        data = response.json().get("data", {})
        children = data.get("children", [])
        if not children and not hot_list:
            return None

        for post in children:
            hot_list.append(post.get("data", {}).get("title", "None"))

        after = data.get("after", None)
        if after is None:
            return hot_list

        return recurse(subreddit, hot_list, after)
    except requests.RequestException:
        return None
