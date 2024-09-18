def calc(first_num:int, second_num:int)->int:
    sum=first_num+second_num
    difference=first_num-second_num
    product=first_num*second_num
    quotient=first_num//second_num
    return sum, difference, product, quotient


t1=calc(35,7)
print(t1)
s, d, p, q=calc(10,5)
print(s,d,p,q)#destructuring
