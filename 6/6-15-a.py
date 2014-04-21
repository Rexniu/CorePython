def date_convert(date_input):
    month = int(date_input.split('/')[0])
    day   = int(date_input.split('/')[1])
    year  = int('20' + date_input.split('/')[2])
    return (year, month, day)

import datetime
date_input = raw_input('Please input the begin date, MM / DD / YY ... ')
d1 = datetime.date(date_convert(date_input)[0], date_convert(date_input)[1], date_convert(date_input)[2])
date_input = raw_input('Please input the end date, MM / DD / YY ... ')
d2 = datetime.date(date_convert(date_input)[0], date_convert(date_input)[1], date_convert(date_input)[2])
print (d2 - d1).days
