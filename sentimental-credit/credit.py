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
        print(i % 10 + int(i/10))



main()
