/*
 * C program to generate Fibonacci Series. Fibonacci Series
 * is 0 1 1 2 3 5 8 13 21 ...
 
 * Taken from: http://www.sanfoundry.com/c-program-fibonacci-series/
 */
#include <stdio.h>
 
void main()
{
    int  fib1 = 0, fib2 = 1, fib3, limit, count = 0;
 
    printf("Enter the limit to generate the Fibonacci Series \n");
    scanf("%d", &limit);
    printf("Fibonacci Series is ...\n");
    printf("%d\n", fib1);
    printf("%d\n", fib2);
    count = 2;
    while (count < limit)
    {
        fib3 = fib1 + fib2;
        count++;
        printf("%d\n", fib3);
        fib1 = fib2;
        fib2 = fib3;
    }
}