year = int(input('Year?'))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) :
    print("閏年。")
else:
    print("都不是。")