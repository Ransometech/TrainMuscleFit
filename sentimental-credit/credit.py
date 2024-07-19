import re
from cs50 import get_int


def main():
    while True:
        number = get_int("Number: ")
        if number > 0:
            break
    # get card type
    checksum(number)


def checksum(number):
    multiplied_digit = []
    other_digit = []
    sum_multiplied_digit = 0
    sum_other_digit = 0
    card = str(number)

    for i in str(number):
        # print("num", i,  number % 2,"_",  int(number /10),"_", number % 10)

        # get each digit and other digit
        other_digit.append(number % 10)
        number = int(number / 10)
        multiplied_digit.append(2 * (number % 10))
        number = int(number / 10)
        print(multiplied_digit, "multiplied_digit")
        print(other_digit, "other_digit")
        if number == 0:
            break
    # sum each digit of multiplied digit
    for i in multiplied_digit:
        sum_multiplied_digit += i % 10 + int(i/10)
    print(sum_multiplied_digit)

    # sum each digit of other digit
    for i in other_digit:
        sum_other_digit += i
    print(sum_other_digit)
    print(20 % 10, "last")

    # check for invalid card
    if (sum_other_digit+sum_multiplied_digit) % 10 != 0:

        print("INVALID")

    # print each card type
    elif re.match(r'^5[1-5]\d+$', card):
        print("MASTERCARD")
    elif re.match(r'^4\d+$', card):
        print("VISA")
    else:
        print("AMEX")


main()
