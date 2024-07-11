#include <cs50.h>
#include <stdio.h>
int main(void)
{
    // Ask a user for their name and greet them
    string userName = get_string("What is your name?: ");

    printf("hello, %s\n", userName);
}

