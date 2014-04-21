def myPop(list):
    return list[0:len(list)-1]
   
   
list_string = raw_input('Please input the list: ... ')
list = []
a = list_string.split(',')
for i in a:
        list.append(int(i))
print myPop(list)
