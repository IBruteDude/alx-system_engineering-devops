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
