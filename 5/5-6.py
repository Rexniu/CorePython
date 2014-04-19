print 'Please input the expression,such as 1+23:'
expression = raw_input()

def verify(a):
    try:
        float(a)
        return True
    except ValueError:
        print 'You input an illegal expression."%s" is not a number.'% a
        return False

if len(expression.split('+'))==2:
    if(verify(expression.split('+')[0]))and(verify(expression.split('+')[1])):
        print '= %f' % (float(expression.split('+')[0]) + float(expression.split('+')[1]))
        pass
  
elif len(expression.split('*'))==2:
        if(verify(expression.split('*')[0]))and(verify(expression.split('*')[1])):
            print '= %f' % (float(expression.split('*')[0]) * float(expression.split('*')[1]))
            pass
	
elif len(expression.split('/'))==2:
    if(verify(expression.split('/')[0]))and(verify(expression.split('/')[1])):
        print '= %f' % (float(expression.split('/')[0]) / float(expression.split('/')[1]))
        pass
    
elif len(expression.split('-'))==2:
    if(verify(expression.split('-')[0]))and(verify(expression.split('-')[1])):
        print '= %f' % (float(expression.split('-')[0]) - float(expression.split('-')[1]))
        pass
    
elif len(expression.split('**'))==2:
    if(verify(expression.split('**')[0]))and(verify(expression.split('**')[1])):
        print '= %f' % (float(expression.split('**')[0]) ** float(expression.split('**')[1]))
        pass
else:
    pass
