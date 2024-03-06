#!/usr/bin/python3
""" Module for the recursive requests function """
from html import unescape
import json
import requests as rs

headers = {
    "User-Agent": "AlxAPI/0.0.1",
    "Authorization": "bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnls"
    "V0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJz"
    "dWIiOiJ1c2VyIiwiZXhwIjoxNzA5Nzc2MzY1LjIyNDM4MSwiaWF0IjoxNzA5Njg5OTY1LjIy"
    "NDM4MSwianRpIjoid045cXB5WGdGVElEZTVGVFA0Zng2MGdJbDM2LUxnIiwiY2lkIjoiR2Iw"
    "cVd1b0tQeElublBTbzdiRXduUSIsImxpZCI6InQyXzVnMHFzcWlpIiwiYWlkIjoidDJfNWcw"
    "cXNxaWkiLCJsY2EiOjE1NzkwMTExOTE1MzEsInNjcCI6ImVKeUtWdEpTaWdVRUFBRF9fd056"
    "QVNjIiwiZmxvIjo5fQ.UXuh6D2zBJU4QCR9Lrj1Vxxyknc2PQpTRntaw39HaEtvhmjMafLGy"
    "ApqVQQYkTa9k5q3HujX9tnxYuCs7k1Hyt0nlZ5ypLU8kvv0F4kLQgRfGQVALxJYF35XaYwSq"
    "5Zaa3N6S63HKgiSPF-5E1aQrZWn0arIZ3XEoMnH4otrxSxDjsCo9AyJ50Qt7J8FtHMMWrWlX"
    "a99Yo8K-LS1JnBFjhIwsh5OLxhNPL5K7jSxghgFWQBHW3CKvz56feJMx1ep3xSULG5Hvqiji"
    "UfM_JukJbJGyBn9NoRjEBZ8ZJ7pdvCUHSf1WaRk05L0D58vG9FZYlZD4daxGnJabch2TmDB6w"
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
