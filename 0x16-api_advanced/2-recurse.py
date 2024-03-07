#!/usr/bin/python3
""" Module for the recursive requests function """
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


def recurse(subreddit, hot_list=[], after=None):
    """ make a paginated recursive api call to get a list of hot articles """
    try:
        text = rs.get(f'https://oauth.reddit.com/r/{subreddit}/hot',
                      headers=headers,
                      params={'after': after} if after else {}).text
        data = json.loads(text)
        # json.dump(hot_list, open('resp.json', 'w'))

        if data["data"]["children"] is None:
            return None

        if len(data["data"]["children"]) == 0:
            return len(hot_list)
        else:
            hot_list += data["data"]["children"]
            return recurse(subreddit, hot_list, data["data"]["after"])
    except json.decoder.JSONDecodeError as e:
        # print(e)
        print(text)


if __name__ == '__main__':
    print(recurse('this_is_a_fake_subreddit'))
