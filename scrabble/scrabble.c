#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Function prototype
int calculate_score(string word);

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int main(void)
{
    // Prompt the players for two words
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Calculate the score of each word
    int score1 = calculate_score(word1);
    int score2 = calculate_score(word2);

    // Print the winner
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("It's a tie!\n");
    }

}

int calculate_score(string word)
{
    int score = 0;
    int wlen = strlen(word);

    // Calculate score for each character
    for (int i = 0; i < wlen; i++)
    {
        if (isupper(word[i]))
        {
            score += POINTS[word[i] - 'A'];
        }
        else if (islower(word[i]))
        {
            score += POINTS[word[i] - 'a'];
        }
    }

    return score;
}
