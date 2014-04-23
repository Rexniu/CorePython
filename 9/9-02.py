N = raw_input('Please input the line numbers: ')
F = raw_input('Please input the full location and file name: ')
fobj = open(F)
k = fobj.readlines()
for i in k[:int(N)]:
  print i,
fobj.close()
