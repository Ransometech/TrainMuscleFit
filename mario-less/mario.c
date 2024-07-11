#include <cs50.h>
#include <stdio.h>
void print_row(int spaces, int bricks);
int main(void)
{
    //Prompt the user for the pyramid's height
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while(n<1);

    //Print a pyramid of that height
    for(int i=0; i<n; i++)
    {
      // Print row of bricks
      print_row(n-i, i+1);
    }

}
void print_row(int spaces, int bricks)
{
    // Print spaces
    for(int i=spaces; i>1; i--){
        printf(" ");
    }

    // Print bricks
    for(int j=0;j<bricks;j++)
    {
        printf("#");

    }
    printf("\n");
}
