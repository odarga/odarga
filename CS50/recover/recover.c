#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define BLOCK_SIZE 512

typedef uint8_t BYTE;



int main(int argc, char *argv[])
{
    int k = 0;

    // More than one argument in command line
    if(argc != 2)
    {
        printf("Usage: ./recover file\n");
        return 1;
    }

    char *infile = argv[1];

    // Open forensic image file
    FILE *input = fopen(infile, "r");

    // Unable to open forensic image file
    if(input == NULL)
    {
        printf("Couldn't open %s\n",infile);
        return 1;
    }

    // Allocating memory for output file
    char *outfile = malloc(BLOCK_SIZE);

    sprintf(outfile, "card.FAT");

    // Open FAT file
    FILE *output = fopen(outfile, "w");

    BYTE block[BLOCK_SIZE];

    int i = 0;

    // Reading and writings jpeg files
    while(fread(&block, BLOCK_SIZE, 1, input) != 0)
    {
        if(block[0] == 0xff && block[1] == 0xd8 && block[2] == 0xff && block[3] >= 0xe0)
        {
            fclose(output);

            sprintf(outfile, "%03d.jpg", k);

            k++;

            output = fopen(outfile, "w");
        }

        fwrite(&block, sizeof(block), 1, output);
    }

    fclose(input);
    fclose(output);

    // Free memory for output
    free(outfile);

    return 0;
}
