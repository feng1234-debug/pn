#coding=utf-8

'''
open()操作的参数：
1.要操作的文件名称
2.以什么样的方式操作文件

w:只写模式【不可读，不存在就创建，存在就清空内容】
x:只写模式【不可读，不存在就创建，存在就报错】
a：增加模式【可读，不存在就创建，存在就只增加内容】

"+"表示可以同时读写某个文件，具体为：
r+:读写
w+:写读
x+:写读
a+：写读
'''

'''w---写文件'''
# f=open('file.json','w')
# temp={
#     "name":"feng",
#     "message":"hello"
# }
# f.writelines(temp)
# f.close()

#用序列化写
# import json
# json.dump(temp,open('file.json','w'))


# f=open('file1.json','w')
# f.write('feng')
# f.close()

# '''r---读'''
# f=open('file.json','r')
# print (f.readlines())
#
# '''追加'''
# f=open('file.json','a')
# f.write('fengfeng')
# f.close()

'''文件的上下文的处理'''

with open('file2','w') as f:
    f.write('feng')