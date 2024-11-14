#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int invalid_key(string key);

void encryption(string plain_text, int key);



int main(int argc, string argv[])
{
    if(argc != 2)                                           // Checking if only 1 command-line argument
    {
        printf("Usage: ./caesar key\n");
        return 1;                                           // Error
    }

    if(invalid_key(argv[1]) == 1)                           // Checking key if has any nondecimal digit
    {
        printf("Err. Key includes nondecimal digit\n");
        return 1;                                           // Error
    }

    int key = atoi(argv[1]);

    string plain_text = get_string("plaintext:  ");

    encryption(plain_text, key);                            // Encryption

    return 0;
}



// Checking key if has any nondecimal digit
int invalid_key(string key)
{
    for(int i = 0, length = strlen(key); i < length; i++)
    {
        if(isdigit(key[i]) == 0)
            return 1;
    }

    return 0;
}

// Encryption
void encryption(string plain_text, int key)
{
    int k = key % 26;

    printf("ciphertext: ");

    for(int i = 0, length = strlen(plain_text); i < length; i++)
    {
        if(plain_text[i] >= 'a' && plain_text[i] <= 'z')
        {
            if((plain_text[i] + k) > 'z')
                printf("%c", 'a' + k - ('z' - plain_text[i]) - 1);
            else
                printf("%c",(plain_text[i] + k));
        }
        else if(plain_text[i] >= 'A' && plain_text[i] <= 'Z')
        {
            if((plain_text[i] + k) > 'Z')
                printf("%c", 'Z' + k - ('Z' - plain_text[i]) - 1);
            else
                printf("%c",(plain_text[i] + k));
        }
        else
            printf("%c",plain_text[i]);
    }
    printf("\n");
}

