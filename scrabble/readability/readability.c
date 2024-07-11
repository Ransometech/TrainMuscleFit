#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // Prompt the user for some text
    string text = get_string("Text: ");

    // Count the number of letters, words, and sentences in the text
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    printf("The text contains %d letters.\n", letters);
    printf("The text contains %d words.\n", words);
    // Compute the Coleman-Liau index

    // Print the grade level
}

int count_letters(string text)
{

    int count = 0;
    for (int i=0, text_len = strlen(text); i<text_len; i++)
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
    for (int i=0, text_len=strlen(text); i<text_len; i++)
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
    return 1;
}
