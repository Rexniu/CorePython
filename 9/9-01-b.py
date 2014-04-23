fobj = open('1.txt')
for eachLine in fobj:
  switch = True
  for i in eachLine:
    if i =='#':switch = False
  if switch:print eachLine,
fobj.close()

