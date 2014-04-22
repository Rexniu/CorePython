list_a = [1,2,3,4]
list_b = ['a_value','b_value','c_value','d_value']

k = zip(list_a,list_b)
c = {}
for i in range(len(k)):
  c.update({k[i][0]:k[i][1]})

print c
