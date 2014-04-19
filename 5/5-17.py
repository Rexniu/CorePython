import random
big_n = random.randint(1,101)

list = range(big_n)

for i in range(big_n):
    list[i] = random.randint(-1,2**31)

print big_n
print list
list.sort()
print list
