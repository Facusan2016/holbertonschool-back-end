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

    user_completed_tasks = [t for t in user_tasks if t['completed']]

    print(f'Employee {user_data["name"]} is done with ', end='')
    print(f'tasks({len(user_completed_tasks)}/{len(user_tasks)}):')

    for task in user_completed_tasks:
        print("\t " + task["title"])
