#include <cs50.h>
#include <stdio.h>
#include <string.h>

void winner(string person1, string person2);



int main(void)
{
    string person1 = get_string("Player 1: ");
    string person2 = get_string("Player 2: ");

    winner(person1, person2);   // Determining winner
}



void winner(string person1, string person2)
{
    int array[26] = {1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10};
    int score1 = 0, score2 = 0;

    // Calcuating score for player1
    for(int i = 0, lenght = strlen(person1); i < lenght; i++)
    {
        if(person1[i] >= 'a' && person1[i] <= 'z')
            score1 += array[person1[i] - 'a'];
        else if(person1[i] >= 'A' && person1[i] <= 'Z')
            score1 += array[person1[i] - 'A'];
    }

    // Calcuating score for player2
    for(int i = 0, lenght = strlen(person2); i < lenght; i++)
    {
        if(person2[i] >= 'a' && person2[i] <= 'z')
            score2 += array[person2[i] - 'a'];
        else if(person2[i] >= 'A' && person2[i] <= 'Z')
            score2 += array[person2[i] - 'A'];
    }

    // Comparing scores
    if(score1 > score2)
        printf("Player 1 wins!\n");
    else if(score1 < score2)
        printf("Player 2 wins!\n");
    else
        printf("Tie!\n");
}
