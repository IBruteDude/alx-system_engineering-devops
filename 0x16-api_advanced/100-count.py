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


def count_words(subreddit, word_list, count_dict={}, after=None):
    """ count no of occurances on words in the list of hot articles """
    if len(count_dict) == 0:
        word_list = list(set(word.lower() for word in word_list))
        for word in word_list:
            count_dict[word] = 0
    text = rs.get(f'https://oauth.reddit.com/r/{subreddit}/hot',
                  headers=headers,
                  params={'after': after} if after else {}).text
    data = json.loads(text)
    print(data)
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
