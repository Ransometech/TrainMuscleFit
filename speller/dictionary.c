#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

int count = 0;

typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

const unsigned int N = 10000; // Increase number of buckets for better distribution

node *table[N];

unsigned int hash(const char *word)
{
    unsigned long hash = 5381;
    int c;
    while ((c = *word++))
    {
        hash = ((hash << 5) + hash) + toupper(c); // hash * 33 + c
    }
    return hash % N;
}

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

bool load(const char *dictionary)
{
    FILE *dict_file = fopen(dictionary, "r");
    if (dict_file == NULL)
    {
        printf("Can't open file\n");
        return false;
    }
    char word[LENGTH + 1];

    while (fscanf(dict_file, "%45s", word) != EOF)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            printf("Can't assign memory to new node\n");
            return false;
        }

        int len = strlen(word);
        for (int i = 0; i < len; i++)
        {
            n->word[i] = toupper(word[i]);
        }
        n->word[len] = '\0';

        unsigned int index = hash(n->word);
        n->next = table[index];
        table[index] = n;

        count++;
    }
    fclose(dict_file);
    return true;
}

unsigned int size(void)
{
    return count;
}

bool unload(void)
{
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
