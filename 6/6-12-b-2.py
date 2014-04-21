def rfindchr(string,char):
    a = string
    index = -1
    k = len(a)
    for i in a[::-1]:
       k = k - 1
       if i == char:
          index = k
          print index
          break
    if index == -1:print 'index = ',index

a = raw_input('Please input a string: ')
b = raw_input('Please input a character to be find in this sring :')
rfindchr(a,b)
