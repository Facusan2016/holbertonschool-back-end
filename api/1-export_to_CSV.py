#!/usr/bin/python3
"""
    Program to gather data from an API.
"""
import csv
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

    with open(f'{user_id}.csv', 'w', newline='') as f:

        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in user_tasks:
            writer.writerow([user_id,
                             user_data['name'],
                             task['completed'],
                             task['title']],
                             )
