#include <cs50.h>
#include <ctype.h>

#include <math.h>
#include <stdio.h>
#include <string.h>

// Function prototypes
int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // Prompt the user for some text
    string text = get_string("Text: ");

    // Count the number of letters, words, and sentences in the text
    int letters = count_letters(text);
    float words = count_words(text);
    int sentences = count_sentences(text);

    printf("The text contains %d letters.\n", letters);
    printf("The text contains %d sentences.\n", sentences);

    // Compute the Coleman-Liau index
    float L = (letters / words) * 100;
    float S = (sentence / words) * 100;

    // Print the grade level
}

int count_letters(string text)
{

    // Return the number of letters in text
    int count = 0;
    for (int i = 0, text_len = strlen(text); i <text_len; i++)
    {
        if (isalpha(text[i]))
        {
            count++;
        }
    }
    return count;
}

int count_words(string text)
{
    // Return the number of words in text
    int count = 0;
    for (int i = 0, text_len =strlen(text); i < text_len; i++)
   {
        if (text[i] == ' ')
        {
            count++;
        }
    }
    return count + 1;
}

int count_sentences(string text)
{
    // Return the number of sentences in text
   int count = 0;
    for (int i = 0, text_len  = strlen(text); i < text_len; i++)
   {
        if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            count++;
        }
    }
    return count;
}
