#-*- codeing = utf-8 -*-
#@Time: 2020/5/19 11:17
#@Author: Hiwsi
#@File: urllibTest.py
#@Software: PyCharm

#模拟访问豆瓣网页
import urllib.request

url="http://www.douban.com"
# url="http://www.baidu.com"
url="https://www.xuexila.com/yc/c340279.html"
header={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
}
req=urllib.request.Request(url=url,headers=header)

response=urllib.request.urlopen(req)

print(response.read().decode("utf-8","ignore"))