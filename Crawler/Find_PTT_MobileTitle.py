# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 21:41:25 2019

@author: Chunyen
"""

import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/MobileComm/index.html'
r = requests.get(url)
print('抓取資料原始檔完成。')

soup = BeautifulSoup(r.text,"html.parser") 
#parser 語法分析，這時 html 會被整理
print(soup)

title = soup.select("div.title a")
#將文章的標題取下來
print(title)

print('\n === 分區 ===')
for i in title:
    print(i.text) 
print('\n === 分區 ===')
print(soup.select('h3'))