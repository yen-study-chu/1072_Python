#攝氏轉華氏
def ctof(numbers):
    f = float(numbers)
    f = (f * (9/5)) + 32
    return f
#華氏轉攝氏
def ftoc(numbers):
    c = float(numbers)
    c = (5/9) * (c-32)
    return c

kind = str(input('你輸入的是攝氏還是華氏(C/F) : '))
numbers =  float(input('請輸入溫度 : '))
if kind == 'C' or kind == 'c':
    print(ctof(numbers))
elif kind =='F' or kind == 'f':
    print(ftoc(numbers))
else:
    print('輸入有誤。')    