#????
def strip(str):
    str_b = str[1:-1]
    return str_b

a = raw_input("Please input a string,begin and ending with sapce: ")
if a[0]==' 'and a[len(a)-1]==' ':
    print strip(a)
else:print 'This string should begin and end with space.'
