def double(x,y,z):
    if x >= y:
        if y >= z:
            print("過程：" + str(x) + " ** 2 " + " + " + str(y) + " ** 2 " + " = " + str(x**2+y**2))
            return x**2 + y**2
        else:
            print("過程：" + str(x) + " ** 2 " + " + " + str(z) + " ** 2 " + " = " + str(x**2+z**2))
            return x**2 + z**2
    else:
        if x >= z:
            print("過程：" + str(y) + " ** 2 " + " + " + str(x) + " ** 2 " + " = " + str(y**2+x**2))
            return y**2 + x**2
        else:
            print("過程：" + str(y) + " ** 2 " + " + " + str(z) + " ** 2 " + " = " + str(y**2+z**2))
            return y**2 + z**2       

a = int(input('x:'))
b = int(input('y:'))
c = int(input('z:'))
print(double(a,b,c))