#!/usr/bin/python3
""" makes requests to a user todos from the REST api """
from urllib.request import Request, urlopen
import json
from sys import argv, stderr


if __name__ == "__main__":
    id = int(argv[1])

    root = 'https://jsonplaceholder.typicode.com'

    response = urlopen(root + '/users')
    users = json.loads(response.read())
    response = urlopen(root + f'/users/{id}/todos')
    todos = json.loads(response.read())

    name = None
    for user in users:
        if user['id'] == id:
            name = user['name']
    if name is None:
        print(f"user {id} doesn't exist", file=stderr)
        exit(1)
    with open(f"{id}.json", "w", newline='') as jsondump:
        json.dump({f'{id}': [{
            'task': todo['title'],
            'completed': todo['completed'],
            'username': name
        } for todo in todos]}, jsondump)
