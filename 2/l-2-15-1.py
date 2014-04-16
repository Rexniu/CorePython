SortList = [1,2,3]

for i in range(0,3):
  print 'Please input number',i+1
  SortList[i] = float(raw_input())

if SortList[0]<SortList[1]:
   i = SortList[0]
   SortList[0] = SortList[1]
   SortList[1] = i

if SortList[1]<SortList[2]:
   i = SortList[1]
   SortList[1] = SortList[2]
   SortList[2] = i

if SortList[0]<SortList[1]:
   i = SortList[0]
   SortList[0] = SortList[1]
   SortList[1] = i

print 'after sort:',SortList

