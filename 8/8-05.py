def getfactors(number):
  factorList=[]
  for i in range(1,number+1):
    if number%i ==0:factorList.append(i)
  return factorList

number = raw_input('Please input your number: ')
print getfactors(int(number))
