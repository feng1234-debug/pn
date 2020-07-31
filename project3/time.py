#coding=utf-8
import time as t
#获取时间戳
print (int(t.time()))
#获取当前时间
#print(t.localtime(t.time()))
nowTime=t.strftime('%w-%m-%d %H:%M:%S',t.localtime())

t.sleep(2)
print(nowTime)
