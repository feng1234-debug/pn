#coding=utf-8

import requests

r=requests.get('http://www.baidu.com',timeout=6)


r=requests.get('https://www.12306.cn/index/',verify=False)
'''中文翻译成乱码需要转换一下'''
print(r.content.decode('utf-8'))