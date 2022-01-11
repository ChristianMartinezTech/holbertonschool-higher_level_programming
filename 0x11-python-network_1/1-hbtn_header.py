#!/usr/bin/python3
""" script that takes in a URL, sends an URL request
and displays the X-Request-Id value """

from urllib import request
from sys import argv

if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        headers = response.info()
        print(headers['X-Request-Id'])
