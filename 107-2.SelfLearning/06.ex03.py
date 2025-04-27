x1 = int(input('請輸入第一個戶頭裡面的錢：'))
x2 = int(input('請輸入第二個戶頭裡面的錢：'))
y = int(input('請輸入要轉的錢：'))

if x1<y:
    x2+=x1
    x1 = 0
    print(x1,x2)
else:    
    print(x1-y,x2+y)