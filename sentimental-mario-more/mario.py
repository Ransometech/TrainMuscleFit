from cs50 import get_int


def main():
    height = get_int(" Height: ")

    for i in range(height):
        print_row(i)


def print_row(height):
    for i in range(height);
        print ("#" * i)

main()
