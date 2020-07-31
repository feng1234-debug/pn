#coding=utf-8
import json
import requests
'''
json对于任何一个语言来说都是可以兼容的
序列化：把python的数据类型转为str的类型过程
反序列化：str的类型转为python的数据结构
'''

# r=requests.post(url='https://www.fxiaoke.com/FHH/EM0HUL/Authorize/PersonalCloudLogin?_fs_token=',
#                 data={"phoneNumber":"13125083592","internationalAreaCode":"+86","rsaPassword":"Ct4u2O3EZm+z2QZdLI5qlSbG+dl7+B4z85Jq4Howh4ONx/eBXANc8/pB+rmf8cIXkgNOrQXpS1gO0sQyqcmYTxOGABhJcFCBzIyBuSOPg0/TJ1KLO+1fBP1F+CszhE5Q2Okp+L592RRocQ75ELf2zkIccMO0cCXvgy1jKOY7Zv8=","persistenceHint":"true","publicKey":"MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCROXqyCKxG8DrQKvrmdwiAHFJseaLHKsdzJ+61EpEGUawyLk5obn2Z2lyVVGjqT3KECk3DJtAD6Jux/m/gW2/lxspvhUO1YE1P8OZuUq5xhr/3AWuSSXCqLM2q6TEMnI2VE1BzlsRcxQVGVd4kGszzpyLXYS9ubFTTp1C2A+uZ1QIDAQAB"},
#                 headers={'Content-Type': 'application/json',
#                          'Referer': 'https: // www.fxiaoke.com / pc - login / build / login.html'})
# print(r.text)

# dict1={'name':'feng','age':'18'}
# #序列化：dict---str
# dict_str=json.dumps(dict1)
# print(dict_str,type(dict_str))
#
# #反序列化
# str_dict=json.loads(dict_str)
# print(str_dict,type(str_dict))

'''列表的序列化和反序列化的过程'''
# list1=['admin','feng','weike']
#
# #序列化
# list_str=json.dumps(list1)
# print(list_str,type(list_str))
#
#
# #反序列化
# str_list=json.loads(list_str)
# print(str_list,type(str_list))

'''
文件的序列化和反序列化
1.文件进行反序列化后，类型就是unicode
2.进行编码，把unicode类型转换为str类型
3.然后使用反序列化的，把str转为字典类型
'''
r=requests.get(url='http://172.18.198.34/views/main.html')
print(r.content.decode('utf-8'))
