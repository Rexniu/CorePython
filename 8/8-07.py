def getfactors(number):
  factorList = []
  for i in range(1,number/2+1):
    if number%i==0:factorList.append(i)
  return factorList

def isperfect(number):
  if sum(getfactors(number))==number:return True
  else:return False

number = raw_input('Please input your number: ')
print number,getfactors(int(number)),isperfect(int(number))
