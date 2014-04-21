def list_display(list, N, F):
    num = len(list)/N
    if F == 0 and (len(list) - num * N) == 0:
        for i in range(N):
            for j in range(num):
                print list[i * num + j],
            print '\r'
    if F == 0 and (len(list) - num * N) > 0:
        for i in range(N-1):
            for j in range(num):
                print list[i * num + j],
            print '\r'
        for k in list[(N - 1) * num:]:
            print k,
        print '\r'       
   
           
list_string = raw_input('Please input the list: ... ')
num = raw_input('How many rows/columns in display: ... ')
state = raw_input('(H)orizontal or (V)ertical: ... ').lower()
CMDs = {'h' : 0, 'v' : 1}
list = []
a = list_string.split(',')
for i in a:
    list.append(int(i))
list_display(list, int(num), CMDs[state])
