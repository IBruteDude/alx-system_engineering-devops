#!/usr/bin/python3
""" makes requests to a user todos from the REST api """
from urllib.request import Request, urlopen
from sys import argv, stderr
import json


if __name__ == "__main__":
    id = int(argv[1])

    root = 'https://jsonplaceholder.typicode.com'

    response = urlopen(root + '/users')
    users = json.loads(response.read())
    response = urlopen(root + f'/users/{id}/todos')
    todos = json.loads(response.read())

    completed = list(filter(lambda dic: dic['completed'], todos))
    name = None
    for user in users:
        if user['id'] == id:
            name = user['name']
    if name is None:
        print(f"user {id} doesn't exist", file=stderr)
        exit(1)
    print('Employee {} is done with tasks({}/{}):'.format(
        name, len(completed), len(todos)
    ))
    for todo in completed:
        print(f"\t {todo['title']}")
