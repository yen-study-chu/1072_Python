x = 1
y = 1

for x in range(1,10):
    y = 1
    for y in range(1,10):
        print('%d * %d = %d' %(x,y,x*y))
    x += 1    