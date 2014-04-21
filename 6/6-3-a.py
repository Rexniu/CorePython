aList = raw_input('Please input numbers,separated by space:')
bList = []
for i in aList.split(' '):
    bList.append(int(i))
bList.sort()
print bList[::-1]
