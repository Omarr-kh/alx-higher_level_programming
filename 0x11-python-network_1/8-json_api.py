#!/usr/bin/python3
'''
    script that takes in a letter and sends a POST request to 
    http://0.0.0.0:5000/search_user with the letter as a parameter.
'''
import sys
import requests


def main():
    data = {"q": sys.argv[1] if len(sys.argv) > 1 else ""}
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)

    try:
        data_json = response.json()
        if 'id' in data_json and 'name' in dict_json:
            print('[{}] {}'.format(data_json['id'], data_json['name']))
        else:
            print('No result')
    except Exception:
        print('Not a valid JSON')


if __name__ == "__main__":
    main()
