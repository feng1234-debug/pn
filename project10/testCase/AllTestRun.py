#coding=utf-8
'''批量执行所有测试用例'''
'''用html生成报表  将HtmlTestRunner.py文件放在python的lib目录下'''
import unittest
import os
import HTMLTestRunner
import time
'''
python2中需要导入一些模块,如果不加，写中文的时候会报错

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''

def allTests():
    suite=unittest.TestLoader().discover(
        start_dir=os.path.dirname(__file__),
        pattern='test_*.py',
        top_level_dir=None)
    return suite

def getNowTime():
    return time.strftime('%Y-%m-%d  %H_%M_%S',time.localtime(time.time()))

def run():
    #重新建个report文件，定位到report下面建一个html报告文件
    fp=os.path.join(os.path.dirname(__file__),'report',getNowTime()+'tsetReport.html')
    HTMLTestRunner.HTMLTestRunner(
        #需要打开文件并且写入
        stream=open(fp,'wb'),
        title='自动化测试报告',
        description='自动化报告详细说明').run(allTests())

if __name__=='__main__':
    run()