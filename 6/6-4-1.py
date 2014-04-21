scoreList = []
flag = True
while flag:
    score =raw_input('Please input scores("."to quit!):')
    if score !='.':
       scoreList.append(float(score))
    else:
         flag = False

print scoreList
i = 0
for k in scoreList:
    i = i + k
print "The average is %4.2f" % (i/len(scoreList))
