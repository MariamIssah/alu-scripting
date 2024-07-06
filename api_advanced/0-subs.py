#!/usr/bin/python3
"""
function that queries the 'Reddit API' and returns the number of subscribers
"""
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyBot/1.0"}  # Include a User-Agent to avoid 429 (Too Many Requests) error

    try:
        response = requests.get(url, headers=headers, timeout=10)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json().get("data", {})
            return data.get("subscribers", 0)
        elif response.status_code == 404:
            print(f"Subreddit '{subreddit}' not found.")
        else:
            print(f"Error: Status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

    return 0

# Example usage:
existing_subreddit = "python"
non_existing_subreddit = "nonexistentsubreddit"

print(f"Number of subscribers in '{existing_subreddit}': {number_of_subscribers(existing_subreddit)}")
print(f"Number of subscribers in '{non_existing_subreddit}': {number_of_subscribers(non_existing_subreddit)}")
