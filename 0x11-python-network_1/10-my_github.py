#!/usr/bin/python3
'''
    Script that takes a GitHub user credentials (username and password),
    and uses the GitHub API to display his id
'''
import sys
import requests
from requests.auth import HTTPBasicAuth


def main():
    user = sys.argv[1]
    passwd = sys.argv[2]
    api_url = 'https://api.github.com/user'
    auth = HTTPBasicAuth(user, passwd)

    response = requests.get(api_url, auth=auth)
    data_json = response.json()
    print(data_json.get('id'))


if __name__ == "__main__":
    main()
