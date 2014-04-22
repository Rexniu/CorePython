def isprime(number):
  flag = True
  if number<=1:flag = False
  for i in range(2,number/2+1):
    if number%i == 0:flag = False
  return flag

number = raw_input('Please input your number: ')
print isprime(int(number))
