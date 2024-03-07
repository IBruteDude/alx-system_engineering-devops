#!/usr/bin/python3
""" Module for the top ten function """
from html import unescape
import json
import requests as rs


headers = {
    "User-Agent": "AlxAPI/0.0.1",
    "Authorization": "bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnls"
    "V0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJz"
    "dWIiOiJ1c2VyIiwiZXhwIjoxNzA5OTI4NDgyLjU0NTUwNCwiaWF0IjoxNzA5ODQyMDgyLjU0"
    "NTUwNCwianRpIjoiOVBnOFBHbTI4U09WbGRRVnhzWjRpaEIzaFRZN2xRIiwiY2lkIjoiR2Iw"
    "cVd1b0tQeElublBTbzdiRXduUSIsImxpZCI6InQyXzVnMHFzcWlpIiwiYWlkIjoidDJfNWcw"
    "cXNxaWkiLCJsY2EiOjE1NzkwMTExOTE1MzEsInNjcCI6ImVKeUtWdEpTaWdVRUFBRF9fd056"
    "QVNjIiwiZmxvIjo5fQ.sbR2uWunRwbUGqAOlBMTO3xv4NOmVf01LWEitkOX_uXUWc0NFQ_73"
    "SqnXj_2oFW0tOk9EvnhLVoUApEJVR_kOr9P20ePju3xu79su2vrUZrmBvRwmuWN9guoYf6vv"
    "pvwLqcV1XuTysihrkKlxOA9hTgH0CkjB_V95FN_pA6MLMQ6HjH58chKQxABtv_HivoNZRpfN"
    "YYv1_RF3rBBD8zwizuh93_A2uvMwEb9V-zAvDY2DDuwuH8SrpJ6cbEe8ZlYIHXl_D4MFQy3K"
    "Do8zEeQ92GhOEhyryg6rSQKP1E9l28Nny5fEcx0XxP-4hY_UEBCbhtQo5htkJ4rMpKWJeLDLQ"
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
