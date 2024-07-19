import re
from cs50 import get_int

patterns  = [r'^\d{15}', r'^\d{16}', r'^\d{13}']

def main():
    while True:
        number = get_int("Number: ")
        if check_input(number):
            break
    checksum(number)


def check_input(number):
    for i in patterns:
        if re.match(i, str(number)):
            return True
    return False


def checksum(number):
    multiplied_digit = []
    other_digit = []
    sum_multiplied_digit =  0
    sum_other_digit = 0
    American_Express = [r'^34\d+$', r'^37\d+$']
    MasterCard = [r'^51\d+$', r'^52\d+$', r'^53\d+$', r'^53\d+$', r'^54\d+$', r'^55\d+$']
    Visa = r'^4\d+$'
    card = str(number)


    for i in str(number):
        #print("num", i,  number % 2,"_",  int(number /10),"_", number % 10)

        other_digit.append(number % 10)
        number = int(number / 10)
        multiplied_digit.append(2 *(number % 10))
        number = int(number / 10)
        print(multiplied_digit, "multiplied_digit")
        print(other_digit, "other_digit")
        if number == 0:
            break

    for i in multiplied_digit:
        sum_multiplied_digit += i % 10 + int(i/10)
    print(sum_multiplied_digit)

    for i in other_digit:
        sum_other_digit += i
    print(sum_other_digit)
    print(20%10, "last")
    if (sum_other_digit+sum_multiplied_digit)%10 != 0:

        print("INVALID")

    elif re.match(r'^5[1-5]\d+$', card):
        print("MASTERCARD")
    elif re.match(r'^4\d+$', card):
        print("VISA")
    else:
        print("AMEX")








main()
