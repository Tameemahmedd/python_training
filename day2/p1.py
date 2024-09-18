import sys
def split_states_capitals():
    arguments=sys.argv[1:]
    states=[]
    capital=[]
    for arg in arguments:
        index=arg.find(' ')
        states.append(arg[0:index])
        capital.append(arg[index+1:])
    print("%-15s %s" % ("States", "Capitals"))
    print("----------------------------")
    for i in range(len(states)):
        print("%-15s %s" % (states[i], capital[i]))


split_states_capitals()