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

    // Encrypt the plaintext
    ciphertext(plaintext, key);
}

// Check if a string contains only digits
bool is_key(string key)
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

// Encrypt the text
string ciphertext(string text, int key)
{
    for (int i = 0, text_len = strlen(text); i < text_len; i++)
    {
        if isalpha (text[i])
        {
            if (isupper(text[i]))
            {
                text[i] = ((text[i] - 65 + key) % 26) + 65;
            }

            else if (islower(text[i]))
            {
                text[i] = ((text[i] - 97 + key) % 26) + 97;
            }
        }
    }
    // Print the ciphertext
    printf("ciphertext: %s\n", text);

    return 0;
}
