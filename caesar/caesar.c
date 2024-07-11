#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

// Function prototypes
int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(int argc, string argv[])
{
    if (argc != 2 )
    {
        printf("Usage: ./caesar key\n");
        return 1;

    }
    if (!isdigit(argc[1]))
    {
        printf("Usage: ./caesar2 key\n");
        return 1;

    }
    return 0;

}

