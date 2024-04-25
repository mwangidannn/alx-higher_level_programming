#!/usr/bin/python3
"""
This is a POST request to the passed URL with  email as a paras
"""
import urllib.request
from sys import argv


def main(argv):
    """
    This will Sends POST request the passed URL with  email as paras
    and displays the body of the response (decoded in utf-8)
    """
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf8')
    url = argv[1]
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        result = response.read()
        print(result.decode('utf8'))

if __name__ == "__main__":
    main(argv)
