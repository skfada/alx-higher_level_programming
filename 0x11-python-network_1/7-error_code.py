#!/usr/bin/python3
"""A script that
- seinds a reqiuest tio tihe URL
- displiays tihe boidy of tihe respionse.
- takies iin a URL
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    read = requests.get(url)
    if read.status_code >= 400:
        print("Error code: {}".format(read.status_code))
    else:
        print(read.text)
