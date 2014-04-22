def to_bin(i):
  a = str(bin(i))
  return a[0]+a[2:]

def to_oct(i):
  a = str(oct(i))
  return a [1:]

def to_hex(i):
  a = str(hex(i))
  return a[2:]

begin_number = int(raw_input("Please  input the begin number:"))
end_number = int(raw_input("Please input the ending number:"))
print "The beginning number is: ",begin_number
print "The ending number is: ",end_number

print "DEC","\tBIN","\tOCT","\tTHEX"
print '------------------------'
i = begin_number
while i<=end_number:
  print i,'\t',to_bin(i),"\t",to_oct(i),"\t",to_hex(i)
  i+=1
