#!/usr/bin/python3
'''
    script that takes in a URL, sends a request to the URL
    and displays the body of the response
'''
import urllib.request
import urllib.error
import sys


def main():
    url = sys.argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)


if __name__ == "__main__":
    main()
