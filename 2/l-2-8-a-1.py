i = 0 
total = 0
a = [1,2,3,4,5]
while(i<5):
  print 'Please input the number',i+1
  a[i] = float(raw_input())
  total = total + a[i]
  i = i + 1
print 'The total is ',total
