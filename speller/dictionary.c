// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

int count = 0; // Counter for the number of words in the dictionary

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Choose number of buckets in hash table
const unsigned int N = 10000; // number of buckets

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    char allupper_word[LENGTH + 1];
    for (int i = 0; word[i] && i < LENGTH; i++)
    {
        allupper_word[i] = toupper(word[i]);
    }
    allupper_word[strlen(word)] = '\0';

    unsigned int index = hash(allupper_word);
    node *cursor = table[index];

    while (cursor != NULL)
    {
        if (strcmp(cursor->word, allupper_word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned int hash = 0;
    while (*word)
    {
        hash = (hash << 2) ^ toupper(*word++);
    }
    return hash % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO: Open dictionary file
    FILE *dict_file = fopen(dictionary, "r");
    if (dict_file == NULL)
    {
        printf("Can't open file\n");
        return false;
    }
    char word[LENGTH + 1];

    // Read words from the file
    while (fscanf(dict_file, "%45s", word) != EOF)
    {
        // TODO: Allocate memory for new node
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            printf("Can't assign memory to new node\n");
            return false;
        }

        // Convert to uppercase
        int len = strlen(word);
        for (int i = 0; i < len; i++)
        {
            word[i] = toupper(word[i]);
        }
        strcpy(n->word, word);

        // Get hash index
        unsigned int index = hash(n->word);
        n->next = table[index];
        table[index] = n;

        count++;
    }
    fclose(dict_file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO: Return word count
    return count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO: Go through hash table
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *temp = cursor;
            cursor = cursor->next;
            free(temp);
        }
    }
    return true;
}
