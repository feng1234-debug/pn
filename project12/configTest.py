#coding=utf-8

import configparser
import os
import mysql
def base_dir(filename=None):
    return os.path.join(os.path.dirname(__file__),filename)

def getLiux(Linux='Linux'):
    list1=[]
    config=configparser.ConfigParser()
    cp=config.read(base_dir('config.ini'))
    ip=config.get(Linux,'ip')
    name=config.get(Linux,'name')
    age=config.get(Linux,'age')
    list1.append(ip)
    list1.append(name)
    list1.append(age)
    return list1

print(getLiux())