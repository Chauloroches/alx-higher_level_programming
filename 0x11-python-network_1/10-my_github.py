#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'
    headers = {'Accept': 'application/json'}

    response = requests.get(url, auth=(username, password), headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        print(user_data['id'])
    else:
        print("None")
