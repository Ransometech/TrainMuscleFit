from cs50 import get_int



def main():
    height = get_int(" Height: ")

    for i in range(height):
        print_row(height, i)


def print_row(height, height_row):
        height = height+1
        space =   height - height_row
        print (space * "#" * height_row + " " + "#" * height_row)

main()
