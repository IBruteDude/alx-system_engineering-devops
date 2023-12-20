#!/usr/bin/python3
""" Module for the number of subsribers function """
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
    print("{:d}".format(number_of_subscribers('programming')))
