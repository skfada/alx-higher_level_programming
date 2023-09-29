#!/usr/bin/python3
"""
Displays the X-Request-Id header variable of a request
to a given URL
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    reader = requests.get(url)
    print(reader.headers.get("X-Request-Id"))
