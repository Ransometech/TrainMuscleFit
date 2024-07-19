from cs50 import get_int


def main():

    # Prompt the user for the pyramid's height
    while True:
        height = get_int(" Height: ")
        if height > 0 and height <= 8:
            break

    # Print a pyramid of that height
    for i in range(height):
        print_row(height, i)


def print_row(height, height_row):
    height_row = height_row + 1
    space_len = height - height_row
    space = " " * space_len

    # Print a row of bricks for the left and right pyramid
    print(space + "#" * height_row + "  " + "#" * height_row)


main()
