#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function prototypes
bool alpha_key(string key);
bool not_repeat(string key);

string ciphertext(string text, string key);

int main(int argc, string argv[])
{

    // Check for arguments
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    // Check if the key contains only alphabetic characters
    else if (!alpha_key(argv[1]))
    {
        printf("Key must only contain alphabetic characters\n");
        return 1;
    }

    // Check for duplicate characters
    else if (!not_repeat(argv[1]))
    {
        printf("Key must not contain repeated characters\n");
        return 1;
    }

    // Check if the key length is 26
    else if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters\n");
        return 1;
    }

    else
    {
        string plaintext = get_string("Plaintext: ");

        // Encrypt the plaintext
        ciphertext(plaintext, argv[1]);
    }
}

// Check if the key contains only alphabetic characters
bool alpha_key(string key)
{
    for (int i = 0, len = strlen(key); i < len; i++)
    {
        if (!isalpha(key[i]))
        {
            return false;
        }
    }
    return true;
}

// Check for duplicate characters
bool not_repeat(string key)
{
    for (int i = 0, len = strlen(key); i < len; i++)
    {
        for (int j = 1 + i; j < len; j++)
        {
            if (key[j] == key[i])
            {
                printf("%c %c", key[j], key[i]);

                 return false;
            }
        }
    }
    return true;
}

// Encrypt the text
string ciphertext(string text, string key)
{
    for (int i = 0, text_len = strlen(text); i < text_len; i++)
    {
        if isalpha (text[i])
        {
            if (isupper(text[i]))
            {
                text[i] = key[text[i] - 65];
            }

            else if (islower(text[i]))
            {
                text[i] = key[text[i] - 97];
                text[i] = tolower(text[i]);
            }
        }
    }
    // Print the ciphertext
    printf("ciphertext: %s\n", text);

    return 0;
}
