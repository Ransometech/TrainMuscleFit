#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Accept a single command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Open the memory card
    FILE *card = fopen(argv[1], "r");

    // Create a buffer for a block of data
    uint8_t buffer[512];

    FILE *new_img = NULL;
    int count = 0;
    // While there's still data left to read from the memory card
    while (fread(buffer, 1, 512, card) == 512)
    {
        // Check if the block indicates the start of a new JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // Close the previous JPEG
            if (new_img != NULL)
            {
                fclose(new_img);
            }

            // Create a JPEG file
            char jpeg_file[8];
            sprintf(jpeg_file, "%03i.jpg", count);
            new_img = fopen(jpeg_file, "w");
            if (new_img == NULL)
            {
                printf("Could not create file.\n");
                return 1;
            }
            count++;
        }

        // Write to the JPEG file if it has been opened
        if (new_img != NULL)
        {
            fwrite(buffer, 1, 512, new_img);
        }
    }

    // Close any remaining files
    if (new_img != NULL)
    {
        fclose(new_img);
    }
    fclose(card);

    return 0;
}
