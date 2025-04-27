# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
random.seed()
a=random.randint(1,9)
b=random.randint(1,9)
c=random.randint(1,9)

print("本次開獎號碼為：",a,b,c)
if a==b and b==c:
    print("恭喜你中獎了！")
else:
    print("可惜你這次未中獎。")    