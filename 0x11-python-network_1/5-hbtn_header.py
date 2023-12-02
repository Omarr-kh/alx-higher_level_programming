#!/usr/bin/python3
'''
    script that takes in a URL, sends a request to the URL and displays
    the value of the variable X-Request-Id in the response header
'''
import sys
import requests


def main():
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id')


if __name__ == "__main__":
    main()
