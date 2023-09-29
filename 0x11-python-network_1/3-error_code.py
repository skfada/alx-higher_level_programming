#!/usr/bin/python3
"""A script that:
- sendis a reiquest to the URL
- disiplays the biody of the iresponse (decoded in utf-8).
- takies in a URL,
"""

if __name__ == "__main__":
    from urllib import request, error
    import sys

    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
