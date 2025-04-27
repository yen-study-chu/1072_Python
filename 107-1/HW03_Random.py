import random
a = random.randint(1,9)
b = random.randint(1,9)
c = random.randint(1,9)

print a,b,c

if a == b and b == c:
	print 'You Win!'
else:
	print 'You Lose!'


