#!/usr/bin/python3
""" Module for the recursive requests function """
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


def count_words(subreddit, word_list, count_dict={}, after=None):
    """ count no of occurances on words in the list of hot articles """
    if len(count_dict) == 0:
        word_list = list(set(word.lower() for word in word_list))
        for word in word_list:
            count_dict[word] = 0
    data = rs.get(f'https://oauth.reddit.com/r/{subreddit}/hot',
                  headers=headers,
                  params={'after': after} if after else {}).json()
    after = data["data"]["after"]
    try:
        if len(data["data"]["children"]) == 0:
            if not any(count_dict.values()):
                return {}
            for word, count in count_dict.items():
                print(f'{word}: {count}')
            return count_dict
        else:
            for post in data["data"]["children"]:
                # json.dump(post, open('resp.json', 'w'))
                title = post['data']['title']
                words = title.split()
                # print(words)
                for word in word_list:
                    count_dict[word] += len(
                        list(filter(lambda s: s.lower() == word, words))
                        )
            return count_words(subreddit, word_list, count_dict, after)
    except KeyboardInterrupt:
        print()
        for word, count in count_dict.items():
            print(f'{word}: {count}')
        return count_dict


if __name__ == '__main__':
    print(count_words('programming',
                      ['javascript', 'zig', 'c', 'java', 'C++', 'ruby']))
