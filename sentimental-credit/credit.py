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
        print("num", i,  number % 2,"_",  int(number /10),"_", number % 10)

        other_digit.append()
        number = int(number / 10)

main()
