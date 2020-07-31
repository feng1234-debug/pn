#coding=utf-8
'''面向对象中多态的讲解'''
'''鸭子模型  多态   同样的消息被不同的对象接收'''
from selenium import *

class Framework(object):
    def __init__(self,frame):
        self.frame=frame

class Web(Framework):
    def __init__(self,frame='selenium'):
        Framework.__init__(self,frame=frame)


class App(Framework):
    def __init__(self,frame='Appnium'):
        Framework.__init__(self,frame=frame)

class CloudTesting(object):
    def testing(self,frame):
        if isinstance(frame,Web):
            print('web端的自动化测试')
        elif isinstance(frame,App):
            print('移动自动化测试框架')
        elif isinstance(frame,Framework):
            print('全栈测试')

if __name__=='__main__':
    cloud=CloudTesting()
    app=App()
    web=Web()
    cloud.testing(web)


'''工厂设计模式的应用与讲解'''

class Factory(object):
    def createFrame(self,frame):
        if frame=='web':
            return Web()
        elif frame=='app':
            return App()

class Frame(object):
    def __str__(self):
        return 'frame'

class Web(Frame):
    def __str__(self):
        return 'web'

class App(Frame):
    def __str__(self):
        return 'app'

if __name__=='__main__':
    factory=Factory()
    print(factory.createFrame('web'))