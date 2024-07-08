#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n=0;
    do
    {
        n = get_int("Size: ");
        printf("%d", n);
    }
    while (n < 1);

}
