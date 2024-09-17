#print the Math table of a number for upto multiple of 20

num=int(input("Enter the number for the Math table:"))
for i in range(1, 21):
        print('%d * %02d = %03d'%(num,i,num*i))