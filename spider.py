#-*- codeing = utf-8 -*-
#@Time: 2020/5/18 21:42
#@Author: Hiwsi
#@File: spider.py
#@Software: PyCharm

from bs4 import BeautifulSoup#网页解析，获取数据
import re  #正则表达式，进行文字匹配
import urllib.request,urllib.error #指定url，获取网页数据
import xlwt #进行excel操作
import sqlite3 #进行数据库保存操作

def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 爬取网页
    askUrl(baseurl)
    datalist=getData(baseurl)
    dbpath="movie.db"
    # savepath="豆瓣电影Top250.xls"
    # saveData(datalist,savepath)
    saveData2DB(datalist,dbpath)


#查找电影链接
findLink=re.compile(r'<a href="(.*?)">')
#查找图片链接
findImage=re.compile(r'<img.*src="(.*?)".*/>',re.S)#re.S让换行符包含在里面吗
#查找电影名称
findTitle=re.compile(r'<span class="title">(.*)</span>')
#查找影片评分
findRating=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#查找评价人数
findJudge=re.compile(r'<div class="star">.*<span>(\d*)人评价</span>',re.S)
#查找影片概况
findInq=re.compile(r'<span class="inq">(.*)</span>')
#查找影片相关内容
findBd=re.compile(r'<p class="">(.*?)</p>',re.S)
def askUrl(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
    }
    request=urllib.request.Request(url,headers=header)
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    # print(html)
    return html

def getData(baseurl):
    datalist=[]
    for i in range(0,10):
        url=baseurl+str(i*25) #一共有10页，每页25条数据
        html= askUrl(url)
        # print(html)
        #逐一解析数据
        soup=BeautifulSoup(html,"html.parser")
        for item in soup.findAll("div",class_="item"):
            # print(item)
            data=[]
            item=str(item)
            link=re.findall(findLink,item)[0]
            data.append(link)

            image=re.findall(findImage,item)[0]
            data.append(image)

            title=re.findall(findTitle,item)
            if len(title)==2:#可能有的电影有两个名字，有的只有一个
                ctitle=title[0]#中文名
                data.append(ctitle)
                otitle=title[1].replace("/","")#外文名,替换掉/
                data.append(otitle)
            else:
                data.append(title[0])
                data.append(" ") #空格替换为外文名

            rating = re.findall(findRating, item)[0]
            data.append(rating)

            judge = re.findall(findJudge, item)[0]
            data.append(judge)

            inq = re.findall(findInq, item)
            if len(inq)==0:
                data.append("无")
            else:
                data.append(inq[0])

            bd = re.findall(findBd, item)[0]
            bd=re.sub('<br(\s+)?/>(\s+)?',' ',bd)
            bd=re.sub('/',' ',bd)
            bd=bd.strip()
            data.append(bd)

            datalist.append(data)
    # for item in datalist:
    #     print(item)
    return datalist


#保存数据
def saveData(datalist,savepath):
    book = xlwt.Workbook(encoding="utf-8",)
    sheet = book.add_sheet("豆瓣电影Top250",cell_overwrite_ok=True)
    col=("排名","电影链接","图片链接","电影中文名称","电影外文名称","影片评分","评价人数","影片概况","影片相关内容")
    for i in range(0,9):
        sheet.write(0,i,col[i])
    for i in range(0,len(datalist)):
        for j in range(0,8):
            sheet.write(i+1,0,i+1)#排名
            sheet.write(i+1,j+1,datalist[i][j])#内容
        print("写入第%d行"%(i+1))
    print("写入完成")
    book.save(savepath)


def saveData2DB(datalist,dbpath):
    init_db(dbpath)
    conn=sqlite3.connect(dbpath)
    cur=conn.cursor()
    for data in datalist:
        for index in range(len(data)):
            data[index]='"'+data[index]+'"'
        sql='''
            insert into movie250(info_link, pic_link, cname, oname, rate, judge, about, info)
            values(%s)
        '''%",".join(data)#join用法，将列表以逗号为分隔分开
        cur.execute(sql)
    cur.close()
    conn.commit()
    conn.close()

def init_db(dbpath):
    sql='''
        create table movie250
        (
            id integer primary key autoincrement,
            info_link text,
            pic_link text,
            cname varchar,
            oname varchar,
            rate int,
            judge int,
            about text,
            info text
        )
    '''
    conn = sqlite3.connect(dbpath)#创建链接数据库
    cursor=conn.cursor()#进行游标操作
    cursor.execute(sql)#执行数据库语句
    conn.commit()#提交操作
    conn.close()#关闭数据库


if __name__ == '__main__':
    main()

    print("执行完成")