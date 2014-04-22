def isprime(number):
  flag = True
  if number<=1:flag = False
  for i in range(2,number/2+1):
    if number%i == 0:flag = False
  return flag

def getfactors(number):
  factorList=[]
  for i in range(1,number+1):
    if number%i ==0 and isprime(i):
      factorList.append(i)
  return factorList

def getPrimeFactors(number):
  temp = getfactors(number)
  k = 1
  for i in temp:k=k*i
  if k==number:return temp
  else:
    j = number/k
    return temp + getPrimeFactors(j)


number =int(raw_input('Please input your number: '))
if isprime(number):print 'You have already input a prime nnumber!'
else:
  factors = getPrimeFactors(int(number))
  factors.sort()
  print factors

