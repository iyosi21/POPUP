# -*- coding: utf-8 -*-
import csv
import wx
import datetime
from dateutil.relativedelta import relativedelta

app = wx.App()

# メッセージボックスを表示
today = datetime.date.today()

#CSV読み込み
f = open("list.csv", "r")
lst = list(csv.reader(f))
warn_day = []

for row in range(len(lst)):
    #csvの1列目でヒットする値を探し、配列を作ります。
    obj_day = datetime.datetime.strptime(lst[row][1], '%Y%m%d')
    obj_day = obj_day.date()
    tod_day = today + relativedelta(months=3)
    if tod_day >= obj_day: #この辺で日付計算する
        warn_day.append(lst[row][0] + "　期限切れ:" + str(lst[row][1]) + '\n')

if warn_day != "":
    # メッセージボックスを表示
    warn_out = ''.join(warn_day)
    wx.MessageBox("以下が3ヶ月以内に期限切れです。\n" + warn_out, u'期限切れ通知', wx.ICON_EXCLAMATION)
