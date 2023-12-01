#!/usr/bin/python3
'''
script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id
'''
import urllib.request
import sys

if len(sys.argv) != 2:
    print("Usage: python 1-hbtn_header.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(x_request_id)
        else:
            print("X-Request-Id header not found in the response.")
except urllib.error.URLError as e:
    print("Error:", e.reason)
