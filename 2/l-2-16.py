>>> filename = raw_input("Enter file name:")
Enter file name:test.txt
>>> fobj = open(filename,'r')
>>> for eachLine in fobj:
...   print eachLine,
... 
This is just for test
Python
open file
balabala.....
something else
just forget about it
and do something you should do!
>>> fobj.close()

