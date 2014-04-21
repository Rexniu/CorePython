import string
import keyword

alphas = string.letters+'_'
nums = string.digits

print 'Welcome to the Identifier Checker v2.0'
print 'Testees must be at least 1 chars long.'

myInput = raw_input('Identifier to test:')

isKeyword = False
isIdentifier = False

if len(myInput)>=1:
    
    if myInput[0] not in alphas:
       print "invalid:first symbol must be alphabetic"
       isIdentifier = False
    else:
       for otherChar in myInput[1:]:

            if otherChar not in alphas + nums:
                print 'invalid:remaining symbols must be alphabetic'
                isIdentifier = False
                break
            else:
                isIdentifier = True

if myInput in keyword.kwlist:
    print "'%s' is a keyword of Python" % myInput
    isKeyword = True
if isIdentifier and(not isKeyword):print 'okay as an identifier'
