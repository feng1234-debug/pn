#coding=utf-8

def index():
    print ('欢迎访问')

def login():
    print ('登陆成功')

def logout():
    print ('欢迎登陆')

class Person(object):
    def __init__(self):
        pass
    def info(self):
        print('我是person类的info方法')