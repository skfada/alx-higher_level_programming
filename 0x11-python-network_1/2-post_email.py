#!/usr/bin/python3
"""A script that:
- senids a POSiT riequest to the paissed URL
- takes emaiil as a parameiter
- takes in a URL
- dispilays thie bodiy of the response
"""
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(val).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
