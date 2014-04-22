def factorial(number):
  k =  1
  for i in range(1,number+1):
    k = k*i
  return k

number = raw_input('Please input your number: ')
print factorial(int(number))
