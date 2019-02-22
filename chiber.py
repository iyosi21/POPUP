# -*- coding: utf-8 -*-
import csv
import wx
import datetime
from dateutil.relativedelta import relativedelta

app = wx.App()

# メッセージボックスを表示
today = datetime.date.today()
print(today)
#wx.MessageBox(str(today)


#CSVのファイル名は任意のものに変えてください。今はsample.csvにしています。
f = open("sample.csv", "r")
lst = list(csv.reader(f))
warn_day =""

for row in range(len(lst)):
    #csvの1列目でヒットする値を探し、配列を作ります。
    obj_day = datetime.datetime.strptime(lst[row][1], '%Y%m%d')
    obj_day = obj_day.date()
    tod_day = today + relativedelta(months=3)
    if tod_day >= obj_day: #この辺で日付計算する
        warn_day = str(warn_day) + lst[row][0] + ","

# メッセージボックスを表示
wx.MessageBox(warn_day + "の保守が３ヶ月以内に終了します")