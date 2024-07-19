import re
from cs50 import get_int

patterns  = [r'^\d{15}', r'^\d{16}', r'^\d{13}']

def main():
    while True:
        number = get_int("Number: ")
        if check_input(number):
            break


def check_input(number):
    for i in patterns:
        if re.match(i, number):
            return True
    return False


main()
