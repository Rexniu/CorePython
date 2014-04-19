def a_b(a,b):
    ta = False
    tb = False
    if(a%b)==0:ta = True
    if(b%a)==0:tb = True
    return (ta or tb)


print 'Please input two numbers:'
a = float(raw_input())
b = float(raw_input())
if a_b(a,b):
    print 'They are divisible!'
else:
    print 'They are not divisible!'

