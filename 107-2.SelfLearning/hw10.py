# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 17:50:38 2019

@author: user
"""

a=[["Jack",40,5],["Mary",30,7],["Bob",35,9]]
def year(x):
    return x[2]
b = sorted(a,key=year,reverse=True)
print(b)