// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>

#include "dictionary.h"

int count = 0; // Counter for the number of words in the dictionary

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
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
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *dict_file = fopen(dictionary, "r");
    if (dict_file == NULL){
        printf("Can't open file");

        return false;
    }
    char word[LENGTH + 1];
    while (fscanf(dict_file, "%45", word) != EOF)
    {
        node *n = Malloc(sizeof(node));
        if (n==NULL)
        {

            printf("Cant assign memory to new node");
            return false;
        }

        strcpy(n->word, word);
        unsigned int index = hash(word);

        n->next = table[index];
        table[index] = n

        printf("Inserted %s at index %u\n", word, index);
        count++
    }
    fclose(dict_file);
    return true;
}


// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO

    return count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *temp = cursor;
            cursor = cursor->next;
            printf("Freeing %s\n", temp->word);
            free(temp);
        }
    }
    return true;
}
