def verify(a):
    b = '0123456789'
    if len(a)==2 and a[0] in b and a[1] in b:return True
    else:return False

def change(a):
    b = int(a)
    N25 = b/25
    N10 = (b-25*N25)/10
    N5 = (b-25*N25-10*N10)/5
    N1 = b-25*N25-10*N10-5*N5

    print '%i Cents can be changed to:' % b
    print '25 Cents:%i' % N25
    print '10 Cents:%i' % N10
    print '5 Cents:%i' % N5
    print '1 Cents:%i' % N1

a = raw_input('Please input the number in U.S cents:')
if verify(a):change(a)
else:print "Invalid input,Please try angin!!"
