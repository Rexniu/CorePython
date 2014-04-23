fobj = open('1.txt')
for eachLine in fobj:
  if eachLine[0]!='#':
    print eachLine,
fobj.close()

