def showmenu():
    print '''
    (S)tone
    S(h)ears
    (C)loth
    (Q)uit
    '''
   
def computer_choice():
    import random
    return random.choice('shc')

def your_choice():
    input = raw_input('Please select your choice: ')
    return input.lower()
    # From www.cnblogs.com/balian/

def fight(your_input, computer_input):
    if your_input == computer_input: print 'Nobody Win.\n'
    elif your_input == 'c' and computer_input == 's': print 'You Win.\n'
    elif your_input == 's' and computer_input == 'h': print 'You Win.\n'
    elif your_input == 'h' and computer_input == 'c': print 'You Win.\n'
    else: print 'Sorry, Computer Win.\n'
   
CMDs = {'s': 'Stone', 'h': 'Shears', 'c': 'Cloth'}

run = True
while run:
    showmenu()
    your_input = your_choice()
    if your_input == 'q':
        print 'Game Over!'
        run = False
    else:
        computer_input = computer_choice()
        print 'Your have input %s.' % CMDs[your_input]
        print 'Computer have input %s.' % CMDs[computer_input]
        print 'the result is \n'
        fight(your_input, computer_input)
