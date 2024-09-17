#print second smallest digit in a number
def smallest_digit1(n):

#    digits=[int(digit)for digit in str(n)]
#    digits.sort()
#    return digits[1]
    smallest_digit=9
    second_smallest_digit=9
    temp=n
    while temp!=0:
        rem=temp%10
        temp=temp//10
        if rem<smallest_digit:
            second_smallest_digit=smallest_digit
            smallest_digit=rem
        elif rem<second_smallest_digit:
            second_smallest_digit=rem
    return second_smallest_digit


number=int(input("Enter a number:"))
print(smallest_digit1(number))