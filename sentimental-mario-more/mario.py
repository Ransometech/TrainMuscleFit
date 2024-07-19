from cs50 import get_int

height = get_int(" Height: ")


def main():

    for i in range(height):
        print_row(i)


def print_row(height_row):
        height = height+1
        space =   height - height_row
        print ("#" * height_row + " " + "#" * height_row)

main()
