def leap(y):
    if (y%4==0 and y%100!=0)or(y%400==0):
        print '%d is leap year!' % y
    else:
        print '%d is not leap year!' %y


y = float(raw_input('Please input the year:'))
leap(y)
