#!/usr/bin/python3
""" Module for the top ten function """
import requests as rs
import json
from pprint import pp
from html import unescape


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


def top_ten(subreddit):
    """ get the titles of the top ten subreddits """
    resp = rs.get(f'https://oauth.reddit.com/r/{subreddit}/hot',
                  headers=headers, params={'limit': 10})
    text = unescape(resp.text)
    try:
        data = json.loads(text)
        print(json.dumps(data))
        top10 = data["data"]["children"][:10]
        if len(top10) > 0:
            for item in top10:
                print(item["data"]["title"])
        else:
            print("None")
        return ""
    except json.decoder.JSONDecodeError as e:
        print("None")
    except KeyError as e:
        print("None")


if __name__ == '__main__':
    top_ten('programming')
