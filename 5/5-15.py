def GCD(a,b):
    i = 0
    if (a%2==0)and(b%2==0):
        c = a/2
        d = b/2
        i = i+1
    else:
       c = a
       d = b
    while c!=d:
       if c>d:c=c-d
       elif c<d:d=d-c
       else:return c*(2**i)
    return c*(2**i)

def LCM(a,b):
    return a*b/GCD(a,b)

print GCD(4044,9088)
print LCM(4044,9088)
