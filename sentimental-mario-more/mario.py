from cs50 import get_int


def main():
    height = get_int(" Height: ")

    for i in range(height):
        print_row(i)


def print_row(height):
        height = height+1
        print ("#" * height, end="")

main()
