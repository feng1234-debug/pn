#coding=utf-8

import logging
from selenium import webdriver
import unittest

def log(log_content):
    #定义文件
    logFile=logging.FileHandler('log.md','a',encoding='utf-8')
    #log格式
    fmt=logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s:%(message)s')
    logFile.setFormatter(fmt)

    #定义日志
    logger1 = logging.Logger('',level=logging.DEBUG)
    logger1.addHandler(logFile)
    logger1.info(log_content)
log('内容')