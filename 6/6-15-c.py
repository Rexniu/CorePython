def date_convert(date_input):
    month = int(date_input.split('/')[0])
    day   = int(date_input.split('/')[1])
    year  = int(date_input.split('/')[2])
    return (year, month, day)

import datetime
date_input = raw_input('Please input his birthday, MM / DD / YYYY ... ')

import time
next_year = int(time.strftime('%Y',time.localtime(time.time()))) + 1
next_birthday = datetime.date(next_year, date_convert(date_input)[1], date_convert(date_input)[2])
print (next_birthday - datetime.date.today()).days
