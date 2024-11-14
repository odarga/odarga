#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            int average = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0);
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtRed = average;
        }
    }

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for(int j = 0; j < width / 2; j++)
        {

            int tempRed;
            int tempGreen;
            int tempBlue;

            tempRed = image[i][j].rgbtRed;
            image[i][j].rgbtRed = image[i][width - j - 1].rgbtRed;
            image[i][width - j - 1].rgbtRed = tempRed;

            tempGreen = image[i][j].rgbtGreen;
            image[i][j].rgbtGreen = image[i][width - j - 1].rgbtGreen;
            image[i][width - j - 1].rgbtGreen = tempGreen;

            tempBlue = image[i][j].rgbtBlue;
            image[i][j].rgbtBlue = image[i][width - j - 1].rgbtBlue;
            image[i][width - j - 1].rgbtBlue = tempBlue;
        }
    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];

    for (int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            int count = 0;

            int tempRed = 0;
            int tempGreen = 0;
            int tempBlue = 0;

            int k = i - 1;
            int l = j - 1;
            int k_end = i + 1;
            int l_end = j + 1;

            if(i == 0)
                k = i;
            if(j == 0)
                l = j;
            if(i == height - 1)
                k_end = i;
            if(j == width - 1)
                l_end = j;


            while (k <= k_end)
            {
                while(l <= l_end)
                {
                    tempRed += image[k][l].rgbtRed;
                    tempGreen += image[k][l].rgbtGreen;
                    tempBlue += image[k][l].rgbtBlue;

                    l++;
                    count++;
                }

                k++;

                if(j == 0)
                    l = j;
                else
                    l = j - 1;

            }

            copy[i][j].rgbtRed = round(tempRed / count);
            copy[i][j].rgbtGreen = round(tempGreen / count);
            copy[i][j].rgbtBlue = round(tempBlue / count);
        }
    }
    for (int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
                image[i][j].rgbtRed = copy[i][j].rgbtRed;
                image[i][j].rgbtGreen = copy[i][j].rgbtGreen;
                image[i][j].rgbtBlue = copy[i][j].rgbtBlue;
        }
    }

    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];

    int Gx[3][3] = {{-1,0,1},{-2,0,2},{-1,0,1}};
    int Gy[3][3] = {{-1,-2,-1},{0,0,0},{1,2,1}};

    for (int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            int tempRedx = 0;
            int tempGreenx = 0;
            int tempBluex = 0;

            int tempRedy = 0;
            int tempGreeny = 0;
            int tempBluey = 0;

            int k = i - 1;
            int l = j - 1;
            int k_end = i + 1;
            int l_end = j + 1;

            if(i == 0)
                k = i;
            if(j == 0)
                l = j;
            if(i == height - 1)
                k_end = i;
            if(j == width - 1)
                l_end = j;


            while (k <= k_end)
            {
                while(l <= l_end)
                {
                    tempRedx += image[k][l].rgbtRed * Gx[k - i + 1][l - j + 1];
                    tempGreenx += image[k][l].rgbtGreen * Gx[k - i + 1][l - j + 1];
                    tempBluex += image[k][l].rgbtBlue * Gx[k - i + 1][l - j + 1];

                    tempRedy += image[k][l].rgbtRed * Gy[k - i + 1][l - j + 1];
                    tempGreeny += image[k][l].rgbtGreen * Gy[k - i + 1][l - j + 1];
                    tempBluey += image[k][l].rgbtBlue * Gy[k - i + 1][l - j + 1];

                    l++;
                }

                k++;

                if(j == 0)
                    l = j;
                else
                    l = j - 1;
            }

            copy[i][j].rgbtRed = round(sqrt(tempRedx * tempRedx + tempRedy * tempRedy));
            copy[i][j].rgbtGreen = round(sqrt(tempGreenx * tempGreenx + tempGreeny * tempBluey));
            copy[i][j].rgbtBlue = round(sqrt(tempBluex * tempBluex + tempBluey * tempBluey));

            if(copy[i][j].rgbtRed > 255)
                copy[i][j].rgbtRed = 255;

            if(copy[i][j].rgbtGreen > 255)
                copy[i][j].rgbtGreen = 255;

            if(copy[i][j].rgbtBlue > 255)
                copy[i][j].rgbtBlue = 255;
        }
    }
    for (int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
                image[i][j].rgbtRed = copy[i][j].rgbtRed;
                image[i][j].rgbtGreen = copy[i][j].rgbtGreen;
                image[i][j].rgbtBlue = copy[i][j].rgbtBlue;
        }
    }

    return;
}
