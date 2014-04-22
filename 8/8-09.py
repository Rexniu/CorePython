def Fibonacci(number):
  fs = [0,1]
  i = 1
  for i in range(number-1):
    a = fs[-1]+fs[-2]
    fs.append(a)
    i += 1
  print fs[1:]
  return fs[-1]

number = raw_input('Please input a number: ')
print Fibonacci(int(number))
