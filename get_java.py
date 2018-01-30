# -*- coding:utf-8 -*-
'''获取github中java项目的信息'''
import requests,pygal
from pygal.style import LightenStyle as LS,LightColorizedStyle as LCS

url = 'https://api.github.com/search/repositories?q=language:java&fort=star'
r = requests.get(url)
print('Ststus Code:',r.status_code)
response_dicts = r.json()

repo_dicts = response_dicts['items']
names,stars = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    # stars.append(repo_dict['stargazers_count'])
    plot_dict = {
        'value':repo_dict['stargazers_count'],
        'label':repo_dict['description'],
        'xlink':repo_dict['html_url']
    }
    stars.append(plot_dict)

my_style = LS('#333366',base_style=LCS)
chart = pygal.Bar(style=my_style,x_label_rotation=45,show_lengend=False)
chart.title = 'Jave Projects Count'
chart.x_labels = names
chart.add('',stars)
chart.render_to_file('get_java.svg')