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
names,plot_dicts = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    # stars.append(repo_dict['stargazers_count'])
    # print(repo_dict['stargazers_count'])
    # print(repo_dict['description'])
    plot_dict = {
        'value':repo_dict['stargazers_count'],
        'label':str(repo_dict['description']),
        'xlink':repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)
# print(names)
# print(stars)
#生成条形图
my_style = LS('#333366',base_style=LCS)
#x_label_rotation=45 表示x轴旋转45度
# show_legend=False 表示隐藏图例
chart = pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('',plot_dicts)
chart.render_to_file('test_repos.svg')

#改进上面代码图标的样式
# my_config = pygal.Config()
# my_config.x_label_rotation = 45
# my_config.show_legend = False
# my_config.title_font_size = 24
# my_config.label_font_size = 14
# my_config.major_label_font_size = 18
# my_config.truncate_label = 15    #将项目名称缩短为15个字符
# my_config.show_y_guides = False   #隐藏水平线
# my_config.width = 1000

# show_image = pygal.Bar(my_config,style=my_style)
# chart.title = 'Python Projects'
# show_image.x_labels = [names['httpe'],names['django'],names['flask']]
# chart.x_labels = ['httpie','django','flask']
# plot_dicts = [
#     {'value':16101,'label':'Description of httpie.'},
#     {'value':15028,'label':'Description of django.'},
#     {'value':14798,'lavel':'Description of flask.'},
# ]
# chart.add('',plot_dicts)
# chart.render_to_file(u'python_repos.svg')
