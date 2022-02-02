#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status """

from urllib import request

if __name__ == "__main__":
    response = request.urlopen(argv[1])
    print('RESPONSE:', response)
    print('URL     :', response.geturl())

    headers = response.info()
    print('DATE    :', headers['date'])
    print(headers)