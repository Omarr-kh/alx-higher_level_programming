#!/usr/bin/python3
'''
    Script that list 10 commits (from the most recent to oldest)
    for the both passed user's repository
'''
import sys
import requests


def main():
    repo_name = sys.argv[1]
    owner = sys.argv[2]

    url = f'https://api.github.com/repos/{owner}/{repo_name}/commits'
    response = requests.get(url)
    commits = response.json()
    if type(commits) != list:
        exit()
    max_commits = 10 if len(commits) > 10 else len(commits)

    for i in range(max_commits):
        sha = commits[i]['sha']
        author_name = commits[i]['commit']['author']['name']

        print(sha + ': ' + author_name)


if __name__ == "__main__":
    main()
