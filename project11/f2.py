#!/use/bin/env python
#coding:utf-8


import  requests
import  json



data={'first':'false','pn':2,'kd':'自动化测试工程师'}
headers={
	'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
	'Cookie':'_ga=GA1.2.1237290736.1534169036; user_trace_token=20180813220356-b7e42516-9f01-11e8-bb78-525400f775ce; LGUID=20180813220356-b7e428ad-9f01-11e8-bb78-525400f775ce; JSESSIONID=ABAAABAAAFCAAEG91327F649A09EEAD6003C392127E51B9; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1539431983,1539433248,1539529521,1539785285; LGSID=20181017220807-12832259-d216-11e8-bc54-525400f775ce; PRE_UTM=; PRE_HOST=www.google.com.hk; PRE_SITE=https%3A%2F%2Fwww.google.com.hk%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; _gid=GA1.2.1861304162.1539785285; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; SEARCH_ID=1066b8cc751f4e9b8eb6c73038d60584; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1539785292; LGRID=20181017220814-16ae80db-d216-11e8-bc54-525400f775ce',
	'Referer':'https://www.lagou.com/jobs/list_%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95?labelWords=&fromSearch=true&suginput=',
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
r=requests.post(
	url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false',
	data=data,
	headers=headers)
text=r.json()
print(json.dumps(text,indent=True,ensure_ascii=False))