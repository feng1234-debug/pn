#coding=utf-8
import requests
import csv
import ddt
import unittest


'''通过接口测试的技术获取拉钩网平台的资料'''
url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=False'


def getHeaders():
    headers={'Content-Type':'application/json;charset=UTF-8',
             'User-Agent':'"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0"',
             'Cookie':'"RECOMMEND_TIP=true; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1595247844,1595247877,1595248603,1595248625; _ga=GA1.2.625729902.1592547780; user_trace_token=20200619142300-eceec3bb-aadd-4f58-8e6c-b5191cd9cbb2; LGUID=20200619142300-80804bef-d9f1-4353-be96-59cd57f94fb5; index_location_city=%E5%85%A8%E5%9B%BD; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22172cb3ec376a76-08cedb8966f951-14636e4a-2073600-172cb3ec377be6%22%2C%22%24device_id%22%3A%22172cb3ec376a76-08cedb8966f951-14636e4a-2073600-172cb3ec377be6%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Firefox%22%2C%22%24browser_version%22%3A%2235.0%22%7D%7D; LG_LOGIN_USER_ID=13b28ea4d82f3abe5849a3cb1185f592904bbd39f3f0c6d8ef2f4efb9c3014bd; LG_HAS_LOGIN=1; _gid=GA1.2.383417396.1595239275; SEARCH_ID=f70b040a3dfe4554a27583b9d490c9dd; LGSID=20200720203645-33acfcc1-bcf4-4868-8dc5-60730db93103; PRE_UTM=m_cf_cpc_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.0f00000uEDLSpLgiC6pP0HLzVncqfYLxJDS3HyKdjzMezcsK8Hrfjts-sZ1R0MwyWeqYSU32XpAAQ3VFLLOxWzAABE24cwKJSuqOlzix4Rjij%5F9eCDQxyqO0sYMyh8VW5Vfzrr-OxjzxVM06sev3HaRuDBPsNpu6smmNb300b%5FihqpyAIM1DBBroUD%5FO%5FYmhNt5G0c%5Fx9rI%5FNLjZo2z26KW1CW85.7b%5FNR2Ar5Od663rj6tJQrGvKD77h24SU5WudF6ksswGuh9J4qt7jHzk8sHfGmYt%5FrE-9kstVerQKz33X8M-eXKBqM764mTT5Qx-4U81W%5FdLtVviEGzF4T5M33xg4mIqXZ1L3xUg9qIvZ1tTr1x9vUn5MY3IMo9vUt5M8se5gjlSpknpgwRgkF4X5QIJyAp7WWklIhqf.U1Yk0ZDqs2v4VnL31xWi%5Fejh0ZKGm1Ys0Zfq1xWi%5Fejhs2v4V0KGUHYznWR0u1dsT1n0Iybqmh7GuZN%5FUfKspyfqP0KWpyfqrjf0UgfqnH0krNtknjDLg1DsnWPxnW0dnNtknH0dnNt1PW0k0AVG5H00TMfqrj00mhbqnHRdg1Ddr7tznjwxnWDL0AdW5HDsnj7xnH6dPjm1PjDYP7tkg1DsPHmvPWD1g1Dsn-ts0Z7spyfqn0Kkmv-b5H00ThIYmyTqn0K9mWYsg100ugFM5Hc0TZ0qn0K8IM0qna3snj0snj0sn0KVIZ0qn0KbuAqs5H00ThCqn0KbugmqTAn0uMfqn0KspjYs0Aq15H00mMTqPsK8IjYs0ZPl5fK9TdqGuAnqTZnVuLGCXZb0pywW5R9rf6KYmgFMugfqPWPxn7tkPHn0IZN15HbLnWm4nHRdPHfkrjm3PjfsnH00ThNkIjYkPHbdnWfLrj6vrHfL0ZPGujY4PjDsuAmYnj0snjc1nHDs0AP1UHYswW97wH6sfR7jf1nLPDuD0A7W5HD0TA3qn0KkUgfqn0KkUgnqn0KlIjYs0AdWgvuzUvYqn7tsg1Kxn7tsg100uA78IyF-gLK%5Fmy4GuZnqn7tsg1Kxn7t1P1b3PjTvg100TA7Ygvu%5FmyTqn0Kbmv-b5H00ugwGujYVnfK9TLKWm1Ys0ZNspy4Wm1Ys0Z7VuWYs0AuWIgfqn0KGTvP%5F5H00XMK%5FIgnqn0K9uAu%5FmyTqnfK%5Fuhnqn0KbmvPb5fKYTh7buHYLPW0znjc0mhwGujYzwDRYrHuanYNDwWT4PWnLfHRzP1RYrRf3rjTdfbcYn0KEm1Yk0AFY5H00Uv7YI1Ys0AqY5H00ULFsIjYsc10Wc10Wnansc108nj0snj0sc10Wc10WQinsQW0snj0snankQW0snj0sn0KkgLmqna3vn-tsQW0sg108njKxna3kr7tsQWD4g108nWD0mMPxTZFEuA-b5H00mLFW5HRkrHc4%26ck%3D3034.2.9999.238.276.340.400.129%26shh%3Dwww.baidu.com%26sht%3Dmonline%5F3%5Fdg%26us%3D1.0.1.0.3.3472.0%26ie%3Dutf-8%26f%3D8%26tn%3Dmonline%5F3%5Fdg%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%25E7%25BD%2591%25E9%25A1%25B5%25E7%2589%2588%26oq%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%25E7%25BD%2591%25E9%25A1%25B5%25E7%2589%2588%26rqlang%3Dcn%26bs%3D%25E6%258B%2589%25E5%258B%25BE%25E6%258B%259B%25E8%2581%2598%26bc%3D110101; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm%5Fsource%3Dm%5Fcf%5Fcpc%5Fbaidu%5Fpc%26m%5Fkw%3Dbaidu%5Fcpc%5Fbj%5Fd438fb%5Fd2162e%5F%25E7%25BD%2591%25E9%25A1%25B5%25E7%2589%2588%25E6%258B%2589%25E5%258B%25BE%26bd%5Fvid%3D11346011929005318419; JSESSIONID=ABAAAECABIEACCA8A0999CA8E9D8536F7E54DBB65C6CA1F; WEBTJ-ID=20200720180113-1736bab9600960-08cb941ca44d3a-14636e4a-2073600-1736bab9601b6f; TG-TRACK-CODE=index_search; X_HTTP_TOKEN=fafa969f52b95cff836842595199b222209ad59c6b; X_MIDDLE_TOKEN=92675f0611fb57b3767b7b396bf215b8; _gat=1; LGRID=20200720203718-5fb9e09e-4d0f-4d0a-9343-018e3b76ea41; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1595248636"',
             'Referer':'"https://www.lagou.com/jobs/list_%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=&fromSearch=true&suginput="'
             }
    return headers

def f():
    list1=[]
    t=[i for i in range(1,31)]
    list1.append(t)
f()



# @ddt.ddt
# class LaGou(unittest.TestCase):
#     @ddt.data((1,),(2,),(3,),(4,),(5,),)
#     @ddt.unpack
#     def test_Lagou(self,page=2):
#         positions=[]
#         r = requests.post(
#             url=url,
#             headers=getHeaders(),
#             data={'first': False, 'pn': page, 'kd': '自动化测试工程师'})
#         self.assertEqual(r.json()['success'],True)
#         print(r.json()['content']['positionResult']['result'][0]['city'])
#
# if __name__=='__main__':
#     unittest.main(verbosity=2)