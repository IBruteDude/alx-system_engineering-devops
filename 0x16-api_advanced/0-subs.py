#!/usr/bin/python3
""" Module for the number of subsribers function """
from html import unescape
import json
import requests as rs


headers = {
    "User-Agent": "AlxAPI/0.0.1",
    "Authorization": "bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnls"
    "V0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJz"
    "dWIiOiJ1c2VyIiwiZXhwIjoxNzA5Njg3ODUxLjEzOTA0OCwiaWF0IjoxNzA5NjAxNDUxLjEz"
    "OTA0NywianRpIjoicDBJMFVoT1M2UW5qc2I2Y2dQZFVFd1BjQS1qSUZRIiwiY2lkIjoiR2Iw"
    "cVd1b0tQeElublBTbzdiRXduUSIsImxpZCI6InQyXzVnMHFzcWlpIiwiYWlkIjoidDJfNWcw"
    "cXNxaWkiLCJsY2EiOjE1NzkwMTExOTE1MzEsInNjcCI6ImVKeUtWdEpTaWdVRUFBRF9fd056"
    "QVNjIiwiZmxvIjo5fQ.R1UB_90NsMb5sH1ML-_-6kIn2WgKodiibpWwaT54CINrPYphoMVtf"
    "BqPoCei-aOikeZmQjgMX7C7CN9Go18zAzHmB_CpkbNND-3-b3zZhefDePfpX0E-_x_PVyxqu"
    "esSS2194PNJRQ_ss_nYI_t1mhWgMfF2YbeAWMkETkUmjk_n7HkFeJjLyha1Tni1lCep-ayt5"
    "RIz1-0zvor7xqABVlepzIu0yLMJM9BZDP6rj5t2QjPbn95N_I8lJchWFBQ6-3jzLm64yZQ86"
    "_HM6fEtFL1vBKeLI6aWH5YCYsJ_wOzBut2Zr1NQqJMII5xwtsq2HuNVyVfMgGO9yucwo4QY2w"
}


def number_of_subscribers(subreddit):
    """ get the number of subsribers from a valid subreddit """
    resp = rs.get(f'https://oauth.reddit.com/r/{subreddit}/about',
                  headers=headers)
    text = unescape(resp.text)
    try:
        data = json.loads(text)['data']
        sep = ',\n'
        resp_data = "{{\n{}\n}}".format(
            sep.join(
                [f'\t{repr(key)}: {repr(value)}'
                 for key, value in data.items()]))
        return data['subscribers']
    except json.decoder.JSONDecodeError as e:
        print(text)
    except KeyError as e:
        return 0


if __name__ == '__main__':
    print("{}".format(number_of_subscribers('programming')))
