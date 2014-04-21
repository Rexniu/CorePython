scoreList=[]
while True:
    try:
        score = float(raw_input('Please input scores:'))
        scoreList.append(score)
    except:
        print "You did not input a correct score.Program stopped!!"
        break

print scoreList
i = 0
for k in scoreList:
    i = i + k
print 'The average is %4.2f'%(i/len(scoreList))
