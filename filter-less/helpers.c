#include "helpers.h"

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
            int average = (pixel->rgbtRed + pixel->rgbtGreen + pixel->rgbtBlue) / 3;

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
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
