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

    users_data = requests.get(api_url + f'/users').json()
    users_tasks = requests.get(api_url + f'/todos').json()

    finalDict = {}

    for user in users_data:
        taskArr = []
        user_spcf_task = [x for x in users_tasks if x['userId'] == user['id']]

        for task in user_spcf_task:
            formattedDict = {
                'username': user['username'],
                'task': task['title'],
                'completed': task['completed'],
            }

            taskArr.append(formattedDict)

        finalDict[user['id']] = taskArr

    with open('todo_all_employees.json', 'w') as f:
        json.dump(finalDict, f)
