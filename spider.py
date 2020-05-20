#-*- codeing = utf-8 -*-
#@Time: 2020/5/18 21:42
#@Author: Hiwsi
#@File: spider.py
#@Software: PyCharm

import bs4 #网页解析，获取数据
import re  #正则表达式，进行文字匹配
import urllib.request,urllib.error #指定url，获取网页数据
import xlwt #进行excel操作

def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 爬取网页
    datalist=getData(baseurl)
    savepath=".\\豆瓣电影Top250.xls"
    saveData(savepath)

def askUrl(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
    }
    request=urllib.request.Request(url,headers=header)
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        pass


def getData(baseurl):
    datalist=[]
    return datalist


#保存数据
def saveData(savepath):
    pass


if __name__ == '__main__':
    main()