#!/usr/bin/python3
""" makes requests to a user todos from the REST api """
import json
from sys import argv, stderr
from urllib.request import Request, urlopen


if __name__ == "__main__":
    id = int(argv[1])
    root = 'https://jsonplaceholder.typicode.com'

    name = json.loads(urlopen(root + f'/users?id={id}').read())[0]['name']
    todos = json.loads(urlopen(root + f'/users/{id}/todos').read())

    completed = list(filter(lambda dic: dic['completed'], todos))

    print('Employee {} is done with tasks({}/{}):'.format(
        name, len(completed), len(todos)
    ))
    for todo in completed:
        print(f"\t {todo['title']}")
