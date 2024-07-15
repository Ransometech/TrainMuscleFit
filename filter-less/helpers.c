#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
     // Convert each pixel to grayscale
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Get the pixel
            RGBTRIPLE *pixel = &image[i][j];

            // Calculate average color
            int average = round((pixel->rgbtRed + pixel->rgbtGreen + pixel->rgbtBlue) / 3.0);

            // Assign the average color to the pixel
            pixel->rgbtRed = average;
            pixel->rgbtGreen = average;
            pixel->rgbtBlue = average;
        }
    }

    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
     // Apply sepia filter to the image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Get the original colors
            RGBTRIPLE *pixel = &image[i][j];
            int originalRed = pixel->rgbtRed;
            int originalGreen = pixel->rgbtGreen;
            int originalBlue = pixel->rgbtBlue;

            // Calculate new sepia colors
            int sepiaRed = round(.393 * originalRed + .769 * originalGreen + .189 * originalBlue);
            int sepiaGreen = round(.349 * originalRed + .686 * originalGreen + .168 * originalBlue);
            int sepiaBlue = round(.272 * originalRed + .534 * originalGreen + .131 * originalBlue);

            // Assign sepia colors to pixel
             pixel->rgbtRed = (sepiaRed > 255) ? 255 : sepiaRed;
            pixel->rgbtGreen = (sepiaGreen > 255) ? 255 : sepiaGreen;
            pixel->rgbtBlue = (sepiaBlue > 255) ? 255 : sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Reflect the image horizontally
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            // Swap the pixels
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = temp;
        }
    }
    return;
}

#include <cs50.h>
#include <stdio.h>
#include "helpers.h"

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Create a temporary image to store the blurred values
    RGBTRIPLE temp[height][width];

    // Apply blur filter to the image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int redSum = 0, greenSum = 0, blueSum = 0;
            int count = 0;

            // Sum up the values of the surrounding pixels
            for (int di = -1; di <= 1; di++)
            {
                for (int dj = -1; dj <= 1; dj++)
                {
                    int newI = i + di;
                    int newJ = j + dj;

                    // Check if the surrounding pixel is within the image bounds
                    if (newI >= 0 && newI < height && newJ >= 0 && newJ < width)
                    {
                        redSum += image[newI][newJ].rgbtRed;
                        greenSum += image[newI][newJ].rgbtGreen;
                        blueSum += image[newI][newJ].rgbtBlue;
                        count++;
                    }
                }
            }

            // Calculate the average color value
            temp[i][j].rgbtRed = redSum / count;
            temp[i][j].rgbtGreen = greenSum / count;
            temp[i][j].rgbtBlue = blueSum / count;
        }
    }

    // Copy the blurred values back to the original image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = temp[i][j];
        }
    }
}

