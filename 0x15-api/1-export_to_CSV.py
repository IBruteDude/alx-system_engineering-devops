#!/usr/bin/python3
""" makes requests to a user todos from the REST api """
from csv import reader, writer, QUOTE_ALL
import json
from sys import argv, stderr
from urllib.request import Request, urlopen


if __name__ == "__main__":
    id = int(argv[1])
    root = 'https://jsonplaceholder.typicode.com'

    name = json.loads(urlopen(root + f'/users?id={id}').read())[0]['username']
    todos = json.loads(urlopen(root + f'/users/{id}/todos').read())

    with open(f"{id}.csv", "w", newline='') as csvdump:
        csvwriter = writer(csvdump, quoting=QUOTE_ALL)
        for todo in todos:
            csvwriter.writerow([id, name, todo['completed'], todo['title']])
