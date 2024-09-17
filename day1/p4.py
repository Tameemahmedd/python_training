#read a number from the user and print the lucky digit of the user where the lucky digit is found by finding the sum of digits of the given number and repeat the algorithm untill single digit number is arrived


def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def find_lucky_digit(n):
    while n >= 10:
        n = sum_of_digits(n)
    return n

number = int(input("Enter a number: "))
lucky_digit = find_lucky_digit(number)
print(f"The lucky digit is: {lucky_digit}")




