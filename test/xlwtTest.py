#-*- codeing = utf-8 -*-
#@Time: 2020/5/26 14:02
#@Author: Hiwsi
#@File: xlwtTest.py
#@Software: PyCharm


import xlwt
wookbook=xlwt.Workbook(encoding="utf-8")
wooksheet=wookbook.add_sheet("sheet111")
for i in range(1,10):
    for j in range(1,i+1):
        wooksheet.write(i-1, j-1, "%d*%d "%(i,j))
        print("%d*%d "%(i,j),end="")
    print()

wookbook.save("t1.xls")