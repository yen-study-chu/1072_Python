# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:41:07 2019

@author: user
"""

import requests
import json
import datetime
def getPrice(BaseUrl,inpair):
    BaseUrl = BaseUrl
    TradesUrl = "/trades"
    inpair = inpair
    x = int()
    isBuyer = str()
    ######
    
    rq = requests.get(BaseUrl + TradesUrl +"/"+inpair)
    #print(rq.text) #測試有無接收到資料
    #print(type(rq)) #同上
    Count = int(input("請輸入你要查的筆數："))
    
    rqj = json.loads(rq.text)
    #print(rqj)
    #print(type(rqj)) #在此發現 rqj 為 型態包了一個 data 
    data = rqj['data']
    #print(data) # 將 data 解開，儲存 data 的資料發現各筆為 list 的資料 
    #print(type(data))
    while x < Count:
        trades = data[x]        
        isBuyer = str(trades['isBuyer'])
        #沒加 str() 底下 if 無法判斷 ...
        if isBuyer == "False":
            isBuyer = "賣單"
        else:
            isBuyer = "買單"
        #
        trades_time = trades['timestamp'] 
            #取出 api 中的 timestamp 屬性
        trades_time = str(datetime.datetime.fromtimestamp(trades_time))
            #將 timestamp 時間戳 屬性 轉換為一般時間    
        trades_price = str(float(trades['price']))
        
        print("筆數："+ str(x+1) +"\n時間：" + trades_time + "\n價格："+ trades_price + "\n數量：" + trades['amount'] + "\n買/賣單："+ isBuyer + "\n")
        x += 1        
        
         