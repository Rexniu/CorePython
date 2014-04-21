Input_number = abs(int(raw_input('Please input a number: ')))
x3 = x2 = x1 =x0 =0
x3 = Input_number/(256**3)
if x3>255:
    tmp = x3
    x3 = 255
else:
    tmp = x3
x2 = (Input_number-256**3*tmp)/(256**2)
x1 = (Input_number-256**3*tmp-256**2*x2)/(256**1)
x0 = Input_number - 256 ** 3 *tmp -256**2*x2 -256*x1

print '%d.%d.%d.%d'%(x3,x2,x1,x0)


