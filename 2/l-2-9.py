i = 0
total = 0
ave = 0
a = [0,0,0,0,0]
for i in range(0,5):
  print 'Please input the number',i+1
  a[i]=float(raw_input())
  total = total + a[i]
print 'the average is ',total/5
