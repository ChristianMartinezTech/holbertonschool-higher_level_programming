#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status """

from urllib import request

if __name__ == "__main__":
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("\t- type: " + str(type(html)))
        print("\t- content: " + str(html))
        print("\t- utf8 content: " + str(html.decode('utf-8')))
