#!/usr/bin/python3
'''
Python script that fetches https://alx-intranet.hbtn.io/statu.s
'''
import urllib.request
import urllib.error

url = 'https://alx-intranet.hbtn.io/status'

try:
    with urllib.request.urlopen(url) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')

        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", utf8_content)
except urllib.error.URLError as e:
    print("Error:", e)
