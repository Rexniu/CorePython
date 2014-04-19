def rank(g):
    if 90<=g<=100:
        return 'A'
    elif 80<=g<90:
        return 'B'
    elif 70<=g<80:
        return 'C'
    elif 60<=g<70:
        return 'D'
    else:
        return 'F'



print 'Please input the score:'
g=float(raw_input())
print 'the stage is:',rank(g)
