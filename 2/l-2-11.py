def to_total():
  total = 0
  a = [1,2,3,4,5]
  for i in range(0,5):
    print "Please input number ",i+1
    a[i] = float(raw_input())
    total = total+a[i]
  print total
  
def to_average():
  total = 0
  a = [1,2,3,4,5]
  for i in range(0,5):
    print "Please input number ",i+1
    a[i] = float(raw_input())
    total = total+a[i]
  print total/5

print "input t to get the total of the 5 numbers"
print "input a to get the average of the 5 numbers"
print "input x to exit"

choice = raw_input("Your choice is:\n")
if choice == 't':
  to_total()
elif choice == 'a':
  to_average()
elif  choice == 'x':
  pass
else:
  print 'You inputed wrong select!!!'
