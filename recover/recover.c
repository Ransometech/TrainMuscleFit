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

    FILE *img = NULL;
    int file_count = 0;
    
    // While there's still data left to read from the memory card
    while (fread(buffer, 1, 512, card) == 512)
    {
        // Close the previous JPEG if it exists
        if (img != NULL)
        {
            fclose(img);
        }

        // Create a new JPEG file
        char filename[8];
        sprintf(filename, "%03i.jpg", file_count);
        img = fopen(filename, "w");
        if (img == NULL)
        {
            printf("Could not create file.\n");
            return 1;
        }
        file_count++;
    }

        // Write to the JPEG file if it has been opened
        if (img != NULL)
        {
            fwrite(buffer, 1, 512, img);
        }
    }

    // Close any remaining open files
    if (img != NULL)
    {
        fclose(img);
    }
    fclose(card);


        }


    }
}
