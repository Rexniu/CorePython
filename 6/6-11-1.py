def findchr(string,char):
    a = string
    k = index = -1
    for i in a:
        k = k+1
        if i ==char:
            index = k
            print index
    if index == -1:print 'index = ',index


a = raw_input('Please input a string: ')
b = raw_input('Please input a character to be find in this string:')
findchr(a,b)
