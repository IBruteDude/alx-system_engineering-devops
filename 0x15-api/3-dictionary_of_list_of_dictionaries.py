#!/usr/bin/python3
""" makes requests to a user todos from the REST api """
from json import load, dump, loads, dumps
from sys import argv, stderr
from urllib.request import Request, urlopen


if __name__ == "__main__":
    root = 'https://jsonplaceholder.typicode.com'
    users = loads(urlopen(f'{root}/users').read())

    jsondump = open(f"todo_all_employees.json", "w", newline='')
    dumpdict = {}
    for user in users:
        id = user['id']
        name = user['username']
        response = urlopen(f'{root}/users/{id}/todos')
        todos = loads(response.read())

        dumpdict[f'{id}'] = [{
            'username': name,
            'task': todo['title'],
            'completed': todo['completed'],
        } for todo in todos]
    dump(dumpdict, jsondump)
    jsondump.close()
