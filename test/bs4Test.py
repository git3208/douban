#-*- codeing = utf-8 -*-
#@Time: 2020/5/22 16:12
#@Author: Hiwsi
#@File: bs4Test.py
#@Software: PyCharm
from bs4 import BeautifulSoup
import re
file = open("tt.html", "rb")
html =file.read()
bs=BeautifulSoup(html,"html.parser")
list=bs.findAll("a")
list=bs.findAll(re.compile("a"))
list=bs.findAll(class_="t0")
list=bs.findAll(text=["Python","你好"])
print(bs.title)
print(list)
