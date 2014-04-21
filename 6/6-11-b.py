Input_IP = raw_input('Please input an IP address:')
IP = str.split(Input_IP,'.')
Data = 256**3*int(IP[0])+256**2*int(IP[1])+256*int(IP[2])+int(IP[3])
print 'the number is %d'%Data
