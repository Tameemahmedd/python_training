import math
def even(num):
    return num%2==0
def odd(num):
    return num%2==1
def prime(num):
    prime=True
    for i in range (2,math.ceil(math.sqrt(num))+1):
        if(num%i==0):
            prime=False
            break

    return prime