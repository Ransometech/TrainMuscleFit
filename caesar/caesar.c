#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

// Function prototypes
bool is_digits(string s);


int main(int argc, string argv[])
{
    if (argc != 2 || !is_digits(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;

    }
    int key = arg[1];
    
    return 0;

}

bool is_digits(string key)
{
    for (int i = 0, len = strlen(key); i < len; i++)
    {
        if (!isdigit(key[i]))
        {
            return false;
        }
    }
    return true;
}
