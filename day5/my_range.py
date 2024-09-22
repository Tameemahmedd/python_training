#user defined range function

def my_range(*args):
    arg_count = len(args)
    if arg_count==1:
        i = 0
        while i < args[0]:
            yield i
            i += 1
    elif arg_count==2:
        i = args[0]
        while i < args[1]:
            yield i
            i += 1
    elif args[0]<args[1] and args[2]>0:
        i = args[0]
        while i < args[1]:
            yield i
            i += args[2]
    elif args[0]>args[1] and args[2]<0:
        i = args[0]
        while i > args[1]:
            yield i
            i += args[2]


for i in my_range(5):
    print(i, end=" ")
for i in my_range(5,15):
    print(i, end=" ")
for i in my_range(15, 2 , -2):
    print(i, end=" ")
for i in my_range(15, 2 , 2):
    print(i, end=" ")