#??????
purePrice = float(raw_input('Please input the price:'))
print 'You should pay:'
print 'Subtotal: %10.2f' % purePrice
print 'Sales Tax:%10.2f' % round(purePrice*0.11,2)
print 'TOTAL:    %10.2f' % (purePrice + round(purePrice*0.11,2))
