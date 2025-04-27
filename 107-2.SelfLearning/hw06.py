# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def transform(number):
    turn = (number / 255)*100
    return turn

a = int(input("請輸入能力值："))
b = transform(a)
print("轉換後能力值：=",round(b))