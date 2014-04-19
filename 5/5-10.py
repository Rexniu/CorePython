def change(f):
    print 'after change: %f' % ((f-32.)*(5./9.))

f = float(raw_input('Please input the degree fahrenheit:'))
change(f)
