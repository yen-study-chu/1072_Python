# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:59:34 2019

@author: user
"""

import get_tickers,get_trades,Line_IFTTT

BaseUrl = "https://api.bitopro.com/v2"
print("1.tickers (查詢今日價格)")
print("2.get_recent_trades (近幾次交易比數)")
print("3.Push Price to Line  (最近一次價格發送 至 Line)")

action = str(input("請輸入數字選擇你想做的事："))
inpair = str(input("請輸入你選擇的交易對："))
# https://www.bitopro.com/fees  交易對數量
inpair = inpair
if action == '1':  
    get_tickers.tickers(BaseUrl,inpair)
elif action == '2':
    get_trades.getPrice(BaseUrl,inpair)
elif action == '3':
    Line_IFTTT.Line(BaseUrl,inpair)
else:
    print("重新輸入。")