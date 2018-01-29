# -*- coding:utf-8 -*-
import requests,pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
import matplotlib.pyplot as plt

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status Code:',r.status_code)
#存储api响应的结果
response_dict = r.json()
print('Total repositories:',response_dict['total_count'])

repo_dicts = response_dict['items']
print('Repositories returned:',len(repo_dicts))

print('\nSelected information about each repository:')
names,stars = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

#生成条形图
my_style = LS('#333366',base_style=LCS)
#x_label_rotation=45 表示x轴旋转45度
# show_legend=False 表示隐藏图例
chart = pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('',stars)
chart.render_to_file('repos.svg')



