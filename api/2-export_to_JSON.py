#!/usr/bin/python3
"""
    Program to gather data from an API.
"""
import json
import requests
from sys import argv

if __name__ == '__main__':
    """
        Main Function of the program.
    """

    api_url = f'https://jsonplaceholder.typicode.com/'

    user_id = int(argv[1])
    user_data = requests.get(api_url + f'users/{user_id}').json()
    user_tasks = requests.get(api_url + f'users/{user_id}/todos').json()

    finalDict = []

    for task in user_tasks:
        formattedDict = {
            'task': task['title'],
            'completed': task['completed'],
            'username': user_data['username'],
        }

        finalDict.append(formattedDict)

    with open(f'{user_id}.json', 'w') as f:
        json.dump({user_id: finalDict}, f)
