#!/usr/bin/python3
"""
    Program to gather data from an API.
"""
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

    completed_tasks = sum(1 for task in user_tasks if task['completed'])

    print(f'Employee {user_data["name"]} is done with', end='')
    print(f'tasks({completed_tasks}/{len(user_tasks)}):')

    for task in user_tasks:
        print(f'\t {task["title"]}')
