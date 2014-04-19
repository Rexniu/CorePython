def conversion(a,b):
    return a*60 + b

time = raw_input('Please input the time in HH:MM format:')
t = time.split(':')
print conversion(int(t[0]),int(t[1]))
