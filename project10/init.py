#coding=utf-8
from selenium import webdriver
import unittest

class Init(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)
        cls.driver.get('http://www.baidu.com')

    @classmethod
    def tearDown(cls):
        cls.driver.quit()