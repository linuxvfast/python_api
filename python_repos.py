# -*- coding:utf-8 -*-
import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
#获取URL连接信息存储到r中
r = requests.get(url)
#查看响应的状态码
print('Start Code:',r.status_code)

#api的响应结果为json格式的信息，使用json将信息转换为python字典
response_dict = r.json()
print('Total repositories:',response_dict['total_count'])

repo_dicts = response_dict['items']
print('Repositories returned:',len(repo_dicts))

#获取第一个字典的信息
repo_dict = repo_dicts[0]
print('\nKeys:',len(repo_dict))
#遍历字典的键值
for key in sorted(repo_dict.keys()):
    print(key)



