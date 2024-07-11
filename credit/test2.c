#include <cs50.h>
#include <stdio.h>

int checksum(long number);

int main(void)
{
    // Prompt the user for the credit card number
    long number;
    do
    {
        number = get_long("Number: ");
    }
    while (number < 1);

    // Print the checksum
    printf("%d\n", checksum(number));
}

int checksum(long number)
{
    int sum_digit = 0;
    int sum_other_digit = 0;
    int count = 0;

    while (number > 0)
    {
        int digit = number % 10;
        number /= 10;
        count++;

        // Check if the digit is in an odd position
        if (count % 2 == 0)
        {
            int multiplied_digit = 2 * digit;

            // If multiplied_digit is greater than 9, add its digits together
            if (multiplied_digit > 9)
            {
                sum_other_digit += (multiplied_digit / 10) + (multiplied_digit % 10);
            }
            else
            {
                sum_other_digit += multiplied_digit;
            }
        }
        else
        {
            sum_digit += digit;
        }
    }

    // Calculate and return the final checksum
    int final_checksum = sum_digit + sum_other_digit;
    return final_checksum;
}
