def DivisibleJudge(a,b):
    if (a%b==0) or (b%a==0):
        return True

print 'Please input two numbers:'
a = float(raw_input())
b = float(raw_input())
if DivisibleJudge(a,b):
    print 'They are divisible!'
else:
    print 'They are not divisible!'

