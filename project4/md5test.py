#coding=utf-8
from urllib import parse
import hashlib
'''
对请求参数做ascill码的排序
做url encode编码：age=18&city=hubei&name=feng&work=tester
做md5--sign---4e29633fa9cad3f7f77f10f3d1e2c604
dict1={}
'''

# dict1={'name':'feng','age':'18','city':'hubei','work':'tester',}
# dict1=dict(sorted(dict1.items(),key=lambda item:item[0]))
#

# datas=parse.urlencode(dict1)
# print(datas)
#
# md5=hashlib.md5()
# md5.update(datas.encode('utf-8'))
# print(md5.hexdigest())

def getMd5(**kwargs):
    dict1=dict(sorted(kwargs.items(),key=lambda item:item[0]))
    datas = parse.urlencode(dict1)
    md5 = hashlib.md5()
    md5.update(datas.encode('utf-8'))
    return md5.hexdigest()
print(getMd5(name='feng',age='18'))