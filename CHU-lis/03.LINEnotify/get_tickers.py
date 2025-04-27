# -*- coding: utf-8 -*-
"""
Created on Tue May 28 22:36:46 2019

@author: chunyen
"""

import requests
import json
import time

def tickers(BaseUrl,inpair):
    #基本網址 在 main 處理
    BaseUrl = BaseUrl
    #因選擇是 tickers ，所以指向指定的網址
    TickerUrl = "/tickers"
    #接收 主程式 main 給予的交易對
    inpair = inpair 
    
    #將網址串起來
    rq = requests.get(BaseUrl+TickerUrl+"/"+inpair)
    '''
    print(BaseUrl)
    print(type(BaseUrl))
    print(TickerUrl)
    print(type(TickerUrl))
    print(inpair)
    print(type(inpair))
    '''
    rqj = json.loads(rq.text)

    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    tickers = rqj['data']
    pair = tickers['pair']
    lastprice = tickers['lastPrice']
    buyer = tickers['isBuyer']
    price24 = tickers['priceChange24hr']
    volume24 = tickers['volume24hr']
    high24 = tickers['high24hr']
    low24 = tickers['low24hr']
    
    if buyer == 'false' :
        buyer = "賣單"
    else:
        buyer = "買單"

    return (
    print("現在時間：",localtime),
    print("交易對：",str.upper(pair)),
    print("最後價格：",lastprice),
    print("24小時價格：",price24+"%"),
    print("24小時交易量：",volume24),
    print("買或賣：",buyer),
    print("24小時最高價：",high24),
    print("24小時最低價：",low24))
    