import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Invalid command-line usage")
        sys.exit(1)

    # TODO: Read database file into a variable
    rows = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2]) as text_file:
        text_reader = text_file.read()

    # TODO: Find longest match of each STR in DNA sequence

    for i in rows:

        # Create a dictionary to save the name, str and longest matches
        longest_matches = {"name": list(i.values())[0]}

        # Extract each str in csv file
        for str_dna in list(i.keys())[1:]:

            # Get the longest run of ech str
            longest_run = longest_match(text_reader, str_dna)

            # Save the str and its longest run in a temp dictionary
            sub_match = {str_dna: str(longest_run)}

            # Update the dict with the temp dict with the str and longest run
            longest_matches.update(sub_match)

        # Check if there is match and break, else continue looping through our file
        if longest_matches == i:
            print(i["name"])

            break
    # If no match
    else:
        print("No match")

    # TODO: Check database for matching profiles

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
