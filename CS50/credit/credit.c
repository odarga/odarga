#include <cs50.h>
#include <stdio.h>

int digit_check(long number);
int digit_validity_check(int digit);
void validity_check(long number, int digit);



int main(void)
{
    int digit;

    int x;

    long number;

    number = get_long("Number: ");

    digit = digit_check(number);                // Finding total digits in number
    if(digit_validity_check(digit) == 1)        // Checking digit validity
        validity_check(number, digit);          // Checking number validity
    else
        printf("INVALID\n");
}



// Finding total digits in number
int digit_check(long number)
{
    long i = 1;
    int digit = 0;

    while(true)
    {
        if(number / i == 0)
            break;
        digit++;
        i = i * 10;
    }
    return digit;
}

// Checking if number of digits are valid (13/15/16)
int digit_validity_check(int digit)
{
    if(digit == 13 || digit == 15 || digit == 16)
        return 1;
    else
        return 0;
}

// Luhn's Algorithm and determining card type
void validity_check(long number, int digit)
{
    int total = 0;
    long k=10;

    // Luhn's Algorithm
    for(int i=1; i <= digit; i++)
    {
        if(((number / k) % 10) * 2 < 10)
            total += ((number / k) % 10) * 2;
        else
        {
            total += (((number / k) % 10) * 2) / 10 + (((number / k) % 10) * 2) % 10;
        }

        k = k * 100;
        i = i+1;
    }

    k = 1;

    for(int i=1; i <= digit; i++)
    {
        total += ((number / k) % 10);
        k = k * 100;
        i = i+1;
    }

    if(total % 10 != 0)
    {
        printf("INVALID\n");
    }

    // Determining card type
    else
    {
        if(digit == 13 && number / 1000000000000 == 4)
            printf("VISA\n");
        else if(digit == 16 && number / 1000000000000000 == 4)
            printf("VISA\n");
        else if(digit == 16 && number / 1000000000000000 == 5 && ((number / 100000000000000) % 10 > 0 || (number / 100000000000000) % 10 <= 5))
            printf("MASTERCARD\n");
        else if(digit == 15 && number / 100000000000000 == 3 && ((number / 10000000000000) % 10 == 4 || (number / 10000000000000) % 10 == 7))
            printf("AMEX\n");
        else
            printf("INVALID\n");
    }
}
