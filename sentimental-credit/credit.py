import re


patterns  = [r'^\d{15}', r'^\d{16}', r'^\d{13}']

def check_input(number):
    if re.match(pattern, number):
        return True
    return False

