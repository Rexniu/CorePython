def fixing(name):
  name_temp = name.split()
  return name_temp[-1]+','+name_temp[-2]

def verify(name):
  if "," in name:return True
  else:return False

total_number = int(raw_input('Enter total number of names:'))
name_list = []
error_times = 0
notice1 = 'Please enter name'
noticea = 'Wrong format..should be Last,First.'
notice2 = 'You have done this'
notice3 = ' time(s) already,Fixinng input..'
for i in range(total_number):
  name = raw_input(notice1+str(i)+':')
  if verify(name):
    name_list.append(name)
  else:
    error_times += 1
    print noticea
    print notice2 + str(error_times)+notice3
    name_list.append(fixing(name))

print '\n The sorted list(by last name is): '
name_list.sort()
for i in range(len(name_list)):print name_list[i]
