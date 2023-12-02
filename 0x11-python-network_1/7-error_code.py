#!/usr/bin/python3
'''
    cript that takes in a URL, sends a request to the URL and
    displays the body of the response
'''
import sys
import requests


def main():
    try:
        response = requests.get(sys.argv[1])
        response.raise_for_status()
        print(response.text)
    except requests.HTTPError:
        print('Error code:', response.status_code)


if __name__ == "__main__":
    main()
