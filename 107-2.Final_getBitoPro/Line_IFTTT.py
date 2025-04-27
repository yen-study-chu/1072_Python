# -*- coding: utf-8 -*-
"""
Created on Wed May 29 22:31:53 2019

@author: chunyen
"""
import time,requests,json,datetime

def Line(BaseUrl,inpair):
    
    BaseUrl = BaseUrl
    TradesUrl = "/trades"
    inpair = str.upper(inpair)
    rq = requests.get(BaseUrl + TradesUrl +"/"+inpair)
    #print(rq.text) #測試有無接收到資料
    #print(type(rq)) #同上
    x = int()
    isBuyer = str()
    rqj = json.loads(rq.text)
    #print(rqj)
    #print(type(rqj)) #在此發現 rqj 為 型態包了一個 data 
    data = rqj['data']
    #print(data) # 將 data 解開，儲存 data 的資料發現各筆為 list 的資料 
    #print(type(data))
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
    trades_amount = trades['amount']
    
    print("程式開始執行！")
    
    for i in range(30):
        iffurl = "http://maker.ifttt.com/trigger/BitoPro_getPrice/with/key/xxxxxxxxxxxxxx?"+"value1="+ inpair +"&value2="+ trades_amount +"&value3=" + trades_price
                                                                        #xxxxxxxxx 是輸入你的 IFTTT 通知碼的地方
        rs1 = requests.get(iffurl)
        print(rs1.text)
        time.sleep(30)
    