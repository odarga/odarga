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

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int sepiaRed;
    int sepiaGreen;
    int sepiaBlue;

    for (int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            sepiaRed = round(image[i][j].rgbtRed * 0.393 + image[i][j].rgbtGreen * 0.769 + image[i][j].rgbtBlue * 0.189);
            sepiaGreen = round(image[i][j].rgbtRed * 0.349 + image[i][j].rgbtGreen * 0.686 + image[i][j].rgbtBlue * 0.168);
            sepiaBlue = round(image[i][j].rgbtRed * 0.272 + image[i][j].rgbtGreen * 0.534 + image[i][j].rgbtBlue * 0.131);

            if(sepiaRed > 255)
                sepiaRed = 255;

            if(sepiaGreen > 255)
                sepiaGreen = 255;

            if(sepiaBlue > 255)
                sepiaBlue = 255;

            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
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
