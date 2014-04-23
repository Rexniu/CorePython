filename = raw_input('Please input the file location and name:')
fobj = open(filename)
print len(fobj.readlines())
fobj.close()
