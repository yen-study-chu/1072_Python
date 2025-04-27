print("=== 輸入值為 1000 以內，不得為負。 ===")
x = int(input('你的購買金額：'))
y = 1000 - x
answer = ""

# 有 500,100,50,10,5,1
if x<=1000 and x>0:
    a = y // 500 
    b = y % 500 // 100
    c = y % 100 // 50 
    d = y % 50 // 10
    e = y % 10 // 5
    f = y % 5 // 1
    if a >= 1:
        answer += "500, "+ str(a) + "; "
    if b >= 1:
        answer += "100, "+ str(b) + "; "
    if c >= 1:
        answer += "50, "+ str(c) + "; "
    if d >= 1:
        answer += "10, "+ str(d) + "; "
    if e >= 1:
        answer += "5, " + str(e) + "; "
    if f >= 1:
        answer += "1, " + str(f) +"; "
    
    answer = answer[:-2]
    #消除下一位如果沒有 則不會顯示 ;_ 
    print(answer)
else:
    print("不再範圍內。")

