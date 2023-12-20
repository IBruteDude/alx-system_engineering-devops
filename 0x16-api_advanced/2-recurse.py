#!/usr/bin/python3
""" Module for the recursive requests function """
from html import unescape
import json
import requests as rs


headers = {
    "User-Agent": "AlxAPI/0.0.1",
    "Authorization": "bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnls"
    "V0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0."
    "eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzAzMTMxNDU1LjMxNDMzNSwiaWF0IjoxNzAzMDQ1"
    "MDU1LjMxNDMzNSwianRpIjoiVTJqWFlqazZfenBseGZwNlFEbW5PYWlhakZJc2F3Iiwi"
    "Y2lkIjoiR2IwcVd1b0tQeElublBTbzdiRXduUSIsImxpZCI6InQyXzVnMHFzcWlpIiwi"
    "YWlkIjoidDJfNWcwcXNxaWkiLCJsY2EiOjE1NzkwMTExOTE1MzEsInNjcCI6ImVKeUtW"
    "dEpTaWdVRUFBRF9fd056QVNjIiwiZmxvIjo5fQ.Tvj1i7RGqWYujYLZez-7R-QPPqhEo"
    "zjpu1NHuO7TyZUqWEpA-vTmvgASzWXhKiU0wj9zmJa_qTvygRKDh3tLmAxXcrX5-ZWkm"
    "C1wsiPqTXJeNOqlijdAsn0aVxPTcAQIJ1dM5Vfipv6BTClKpkTtsy06yqcW5hJJ2yBBg"
    "8deS2URvUIaZMGcnQ_wB0KjCR3EFm6brd-ypbAa9vC-N_hyp1wjogb_4fzl_vuvqBl6E"
    "NW_zWMJdOh14JGygjcanLYR1Vyo53u_XI452P-FkM36dqvfuWvB5beL3K02c-pMp1DO3"
    "xC3JZcv4-Sj351ezjb-SO5b8jV-SCZrwCDGCmJbEw"
}


def recurse(subreddit, hot_list=[], after=None):
    """ make a paginated recursive api call to get a list of hot articles """
    try:
        text = rs.get(f'https://oauth.reddit.com/r/{subreddit}/hot',
                      headers=headers,
                      params={'after': after} if after else {}).text
        data = json.loads(text)
        # json.dump(hot_list, open('resp.json', 'w'))
        if len(data["data"]["children"]) == 0:
            return hot_list
        else:
            hot_list += data["data"]["children"]
            return recurse(subreddit, hot_list, data["data"]["after"])
    except json.decoder.JSONDecodeError as e:
        print(text)



if __name__ == '__main__':
    print(len(recurse('programming')))
