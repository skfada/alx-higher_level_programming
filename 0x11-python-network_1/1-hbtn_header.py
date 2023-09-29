#!/usr/bin/python3
"""A sciript that:
- takies in a URL,
- senids a reqiuest to the URL and diisplays the value
- of the X-Request-Id variable founid in the heiader ofthe response.
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
