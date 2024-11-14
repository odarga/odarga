// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N * LENGTH + 1];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    node *ptr = table[hash(word)];

    while(ptr->next != NULL)
    {
        if(strcasecmp(word, ptr->word) == 0)
        {
            return true;
        }
        ptr = ptr->next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    return ((toupper(word[0]) - 'A') + 1) * strlen(word);
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    for(int i = 0; i < N * LENGTH + 1 ; i ++)
    {
        table[i] = malloc(sizeof(node));
        table[i]->next = NULL;
    }

    FILE *file = fopen(dictionary, "r");

    if(file == NULL)
    {
        return false;
    }

    int index = 0;
    char word[LENGTH + 1];
    char c;

    node *new_word = malloc(sizeof(node));

    while(fread(&c, sizeof(char), 1, file))
    {
        if(c == '\n')
        {
            new_word->word[index] = '\0';
            new_word->next = table[hash(new_word->word)];
            table[hash(new_word->word)] = new_word;
            new_word = malloc(sizeof(node));
            index = 0;
        }
        else{
            new_word->word[index] = c;
            index++;
        }
    }
    free(new_word);
    fclose(file);

    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    int count = 0;

    for(int i = 0; i < N * LENGTH + 1; i++)
    {
        node *ptr = table[i];

        while(ptr->next != NULL){
            count++;

            ptr = ptr->next;
        }
    }

    if (count == 0)
    {
        return 0;
    }
    else{
        return count;
    }
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for(int i = 0; i < N * LENGTH + 1; i++)
    {
        node *ptr = table[i];

        if(ptr == NULL)
        {
            return false;
        }

        while(ptr->next != NULL)
        {
            node *next = ptr->next;
            free(ptr);
            ptr = next;
        }
    }
    return true;
}
