# Accept a number from the user and check if it is a perfect square
import math
num=int(input('Enter a number to check for perfect square:'))
root=math.sqrt(num)
if(math.floor(root)*root==num):
    print("Perfect Square")
else:
    print("Not a perfect square")