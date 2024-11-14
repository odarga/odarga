#include <cs50.h>
#include <stdio.h>

int change_ammount();
int coin_numbers(int change);



int main(void)
{
    int c = change_ammount();       // Getting change ammount
    int n = coin_numbers(c);        // Finding coin numbers
    printf("%d\n", n);
}



// Getting change ammount
int change_ammount()
{
    int change = 0;

    do{
        change = get_int("Change owed: ");
    }
    while(change <= 0);

    return change;
}

// Determining number of coins
int coin_numbers(int change)
{
    int number = 0;

    while(change >= 25)
    {
        change = change -25;
        number++;
    }
    while(change >= 10)
    {
        change = change -10;
        number++;
    }
    while(change >= 5)
    {
        change = change -5;
        number++;
    }
    while(change >= 1)
    {
        change = change -1;
        number++;
    }

    return number;
}
