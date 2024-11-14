#include <cs50.h>
#include <stdio.h>

int height();

void blanks(int height, int i);
void hashes(int i);




int main(void)
{
    int h = height();               // Getting Height Of Pyramide

    for(int i = 0; i < h; i++)     // Creating Rows
    {
        blanks(h, i);               // Printing Blanks
        hashes(i);                  // Printing Hashes
        printf("\n");               // New Row
    }
}




// Getting Height Of Pyramide
int height()
{
    int height = 0;

    while(height < 1)
        height = get_int("Height of the Pyramide (Between 1-8): ");

    return height;
}

// Printing Blanks
void blanks(int height, int i)
{
    for(int j = 1; j < height - i; j++)
        printf(" ");
}

// Printing Hashes
void hashes(int i)
{
    for(int j = 0; j <= i; j++)
        printf("#");
}
