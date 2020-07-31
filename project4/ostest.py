#coding=utf-8

import os
#创建文件mkdir
#os.mkdir('c:/log')
#os.rmdir('c:/log')

#对文件或者目录重命名
#os.rename('c:/log','c:/newlog')

#对目录的处理  上级目录就重复，再重复
# print('当前文件的目录',os.path.dirname(__file__))
#print('当前文件的上级目录',os.path.dirname(os.path.dirname(__file__)))


#实现对login文件内容的读取
# base_dir=os.path.dirname(os.path.dirname(__file__))
# f=open(os.path.dirname(base_dir,'project4/qq'),'r')
# print(f.read())

#请求参数是不确定的，可能有一个，可能有N个

