a = raw_input("Please input a string A: ")
b = raw_input("Please input a string B: ")

trigger = True
if len(a)!=len(b):
    trigger = False
else:
    for i in range(len(a)):
        if a[i]!= b[i]:trigger = False
if trigger: print 'String A matches string B!'
else:print 'String A does not match string B!'
