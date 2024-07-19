import re


patterns  = [r'^\d{15}', r'^\d{16}', r'^\d{13}']

def main():
    while True:
        number = get_int("Number: ")
        if check_input(number):
            break


def check_input(number):
    if re.match(pattern, number):
        return True
    return False


