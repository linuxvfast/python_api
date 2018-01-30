# -*- coding:utf-8 -*-
import requests
from operator import itemgetter
#获取hacker news上所有的ID号
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print('Status Code:',r.status_code)
submisson_ids = r.json()

#遍历前5个id号，获取id号对应的标题，连接，描述
submisson_dicts = []
for submisson_id in submisson_ids[:5]:
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submisson_id) + '.json')
    submisson_r = requests.get(url)
    print(submisson_r.status_code)
    response_dict = submisson_r.json()

    submisson_dict = {
        'title':response_dict['title'],
        'link':'http://mews.ycombinator.com/item?id=' + str(submisson_id),
        'comments':response_dict.get('descendants',0)
    }
    submisson_dicts.append(submisson_dict)

#对submisson_dicts的descendants列进行倒序排列
submisson_dicts = sorted(submisson_dicts,key=itemgetter('comments'),reverse=True)
for submisson_dict in submisson_dicts:
    print('\nTitle:',submisson_dict['title'])
    print('Discussion link:',submisson_dict['link'])
    print('Comments:',submisson_dict['comments'])
