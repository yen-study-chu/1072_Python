def is_leap(year):
    if(year >= 1900 and year <= 10**5):
        if (year % 4 == 0):
            if(year % 400 == 0):
                leap = True
            else:
                if (year % 100 == 0):
                    leap = False
                else:
                    leap = True
        else:
            leap = False
            # Write your logic here
    else:
        leap = False
    return leap


year = int(input())
print(is_leap(year))
