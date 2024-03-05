#!/usr/bin/python3
""" Module for the top ten function """
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


def top_ten(subreddit):
    """ get the titles of the top ten subreddits """
    resp = rs.get(f'https://oauth.reddit.com/r/{subreddit}/hot',
                  headers=headers, params={'limit': 10})
    text = unescape(resp.text)
    data = json.loads(text)
    # print(json.dumps(data))
    top10 = data["data"]["children"][:10]
    if len(top10) > 0:
        for item in top10:
            print(item["data"]["title"])
    else:
        print("None")
    return ""


if __name__ == '__main__':
    top_ten('programming')
