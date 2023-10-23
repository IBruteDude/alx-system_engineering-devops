#!/usr/bin/python3
""" makes requests to a user todos from the REST api """
import json
from sys import argv, stderr
from urllib.request import Request, urlopen


if __name__ == "__main__":
    id = int(argv[1])
    root = 'https://jsonplaceholder.typicode.com'

    name = json.loads(urlopen(root + f'/users?id={id}').read())[0]['username']
    todos = json.loads(urlopen(root + f'/users/{id}/todos').read())

    with open(f"{id}.json", "w", newline='') as jsondump:
        json.dump({f'{id}': [{
            'username': name,
            'completed': todo['completed'],
            'task': todo['title'],
        } for todo in todos]}, jsondump)
