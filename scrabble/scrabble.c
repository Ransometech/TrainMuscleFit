#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int calculate_score(string word);
int POINTs[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int main(void)
{
    // Prompt the Players for two words
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");
    printf("%d", word1['B']);

     // Compute the score of each word

      // Print the winner



}

int calculate_score(string word)
{
    int score = 0;

    for (int i=0, wlen = strlen(word); i<wlen; i++)
    {
        if (isupper(word[i]))
        {
            score = POINTs[word[i]-'A'];
        }

    }
    return 3;

}
