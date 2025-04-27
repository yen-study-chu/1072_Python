#encoding=utf8
fin = open('/HW04_Text.txt',"r")
total_people = 0
average_years = 0
average_salary = 0

for x in fin:
    x = x.strip(" \n")
    x = x.split(",")
    total_people +=1
    average_years += float(x[1])
    average_salary += int(x[2])

average_years = average_years / total_people
average_salary = average_salary / total_people
print ("Total People:%d" % (total_people))  
#print "Average Years:%f" % (average_years)
#print "Average Salary:%d" % (average_salary)

fin.close()


