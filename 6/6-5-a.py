a=raw_input("Please input a string: ")
j = 0
print a[j]+a[j+1],
while (j<len(a)-2):
    j = j+1
    print a[j-1]+a[j]+a[j+1],
j = len(a)
print a[j-2]+a[j-1]
