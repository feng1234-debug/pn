#coding=utf-8
import unittest
from project10.init import *

def add(a,b):
    return a-b

class BaiduLink(Init):
    @unittest.skip('该功能已经取消，忽略该用例的执行')
    def test_baidu_news(self):
        print(self.driver.title,type(self.driver.title))
        self.assertEqual(self.driver.title,'百度一，你就知道')

    def test_baidu_login(self):
        so=self.driver.find_element_by_id('kw')
        self.assertTrue(so.is_enabled())

    def test_baidu_title(self):
        self.assertIn('百度',self.driver.title)

if __name__=='__main__':
    suite=unittest.TestSuite()
    # 用例确定先后执行顺序，也可以用序号 001 002让他按照顺序进行执行  也可以按照测试类来执行
    # suite.addTest(BaiduTest('test_baidu_news'))
    # suite.addTest(BaiduTest('test_baidu_news'))
    unittest.TextTestRunner(verbosity=2).run(suite)