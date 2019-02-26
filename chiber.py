# -*- coding: utf-8 -*-
class Config:
    def __init__(self):
        self.name ="期限切れ通知"
        self.limit = "3"
        self.message = str(self.limit) + "ヶ月以内に終了します"

import csv, wx, datetime, subprocess
from dateutil.relativedelta import relativedelta

#設定ファイル読み出し
Conf_t = Config()
try:
    f_config = open("conf.txt", "r",encoding="utf-8")
    conf = f_config.readlines()
    for lines in range(len(conf)):
        conf[lines] = conf[lines].replace("\n","")
        conf[lines] = conf[lines].split('：',1)[-1]

    if type(conf[0]) is str: 
        if type(int(conf[1])) is int:
             if type(conf[2]) is str:
                Conf_t.name = conf[0]   
                Conf_t.limit = int(conf[1])
                Conf_t.message = conf[2]
          
except(FileNotFoundError):
    print("conf.txtファイルが見つかりません")
except(ValueError):
    print("期限の設定が数字ではありません")


app = wx.App()


# メッセージボックスを表示
today = datetime.date.today()

#CSV読み込み
f = open("list.csv", "r")
lst = list(csv.reader(f))
f.close()
warn_day = []

for row in range(len(lst)):
    if row == 0:
        #csvの1行目はカラム名なので飛ばす。
        continue

    if lst[row][2] == "T": #フラグ列がTであれば日付判定をする。
        obj_day = datetime.datetime.strptime(lst[row][1], '%Y%m%d')
        obj_day = obj_day.date()
        tod_day = today + relativedelta(months=int(Conf_t.limit))
        if tod_day >= obj_day: #この辺で日付計算する
            warn_day.append(lst[row][0] + "　期限:" + str(lst[row][1]) + '\n')

if warn_day:
    #配列が空か調べる。
    warn_out = ''.join(warn_day)
    hantei = wx.MessageBox(Conf_t.message+"\n" + warn_out + "\n設定ファイルを編集しますか？", Conf_t.name, wx.YES_NO | wx.ICON_EXCLAMATION | wx.NO_DEFAULT)
    print(hantei)
    if hantei == 2:
        ps = subprocess.Popen(['start','list.csv'], shell=True)
        ps = subprocess.Popen(['notepad','conf.txt'])



