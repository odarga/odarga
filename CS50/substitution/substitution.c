#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int invalid_key(string key);

void encryption(string plain_text, string key);



int main(int argc, string argv[])
{
    if(argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;                                               // Error
    }

    if(invalid_key(argv[1]) == 1)                               // Checking the validty of key
        return 1;                                               // Error

    string plain_text = get_string("plaintext:  ");

    encryption(plain_text, argv[1]);                            // Encryption

    return 0;
}

// Checking the validty of key
int invalid_key(string key)
{
    int length = strlen(key);

    for(int i = 0; i < length; i++)
    {
        if(isalpha(key[i]) == 0)
        {
            printf("Err. Key must contain only letter\n");
            return 1;
        }
    }

    if(length != 26)
    {
        printf("Err. Key must contain 26 charachters\n");
        return 1;
    }

    for(int i = 0; i < length; i++)
    {
        for(int j = i+1; j < length; j++)
        {
            if(tolower(key[i]) == tolower(key[j]))
            {
                printf("Err. Key must contain each letter exactly once\n");
                return 1;
            }
        }
    }
    return 0;
}

// Encryption
void encryption(string plain_text, string key)
{
    printf("ciphertext: ");

    for(int i = 0, length = strlen(plain_text); i < length; i++)
    {
        if(isupper(plain_text[i]) != 0)
            printf("%c",toupper(key[plain_text[i] - 'A']));
        else if(islower(plain_text[i]) != 0)
            printf("%c",tolower(key[plain_text[i] - 'a']));
        else
            printf("%c",plain_text[i]);

    }

    printf("\n");
}
