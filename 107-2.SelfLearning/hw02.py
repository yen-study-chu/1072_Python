# -*- coding: utf-8 -*-
"""
題目、請設計一個計算加班費的程式，
執行時在畫面中提示使用者從鍵盤輸入其年資與本月份加班時數，然後程
式在畫面中輸出該使用者本月份可領取的加班費金額。
         請注意：
         若年資小於3年，則加班費每小時為150元。
         若年資大於或等於3年，則加班費每小時為300元。

"""

years = int(input('請輸入年資?'))
m_plus = int(input('請輸入本月份加班時數?'))
amount = int()

if 0 <= years < 3:
    amount = m_plus * 150
elif years >= 3:
    amount = m_plus * 300
else:
    print("請重新輸入。")

print('本月份可領取加班費共',str(amount),'元')