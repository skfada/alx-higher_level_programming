#!/usr/bin/python3
"""A script that:
- usies thie GitHiub APIi to dispilay your id
- takies yoiur GitHub credentiials (username and password)
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
