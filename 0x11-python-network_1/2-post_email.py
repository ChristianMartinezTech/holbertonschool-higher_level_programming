#!/usr/bin/python3
""" script that takes in a URL, sends an URL request
and displays the X-Request-Id value 
./2-post_email.py http://35.231.66.168:5000/post_email hr@holbertonschool.com
"""
from urllib omport parse
from urllib.request import Request, urlopen
from sys import argv

if __name__ == "__main__":

    header_email = {"email": argv[2]}
    encoded_data = parse

    with request.urlopen(argv[1]) as response:
        post_info = response.post(argv[2])
        print(post_info)
