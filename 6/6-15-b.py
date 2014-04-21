def date_convert(date_input):
    month = int(date_input.split('/')[0])
    day   = int(date_input.split('/')[1])
    year  = int(date_input.split('/')[2])
    return (year, month, day)

import datetime
date_input = raw_input('Please input his birthday, MM / DD / YYYY ... ')
d1 = datetime.date(date_convert(date_input)[0], date_convert(date_input)[1], date_convert(date_input)[2])
print (datetime.date.today() - d1).days
