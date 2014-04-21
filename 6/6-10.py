input = raw_input('Please input a string: ')
output = ''
for i in input:
    if i == i.upper():
        output = output + i.lower()
    else:
        output = output + i.upper()
print output
