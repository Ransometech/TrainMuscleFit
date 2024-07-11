#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


// Function prototypes
bool is_digits(string s);
string ciphertext(string text, int key);



int main(int argc, string argv[])
{
    if (argc != 2 || !is_digits(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;

    }
    int key = atoi(argv[1]);
    string plaintext = get_string("Plaintext: ");

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
string ciphertext(string text, int key)
{
    for (int i=0, text_len = strlen(text); i <text_len; i++){

        if (isupper(text[i]))
        {
            text[i] = text[i] + 5
        }


    }

    return 0;

}
