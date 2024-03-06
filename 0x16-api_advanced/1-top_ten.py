#!/usr/bin/python3
""" Module for the top ten function """
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
