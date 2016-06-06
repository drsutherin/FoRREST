/*
 * C program to find the value of sin(x) using the series
 * up to the given accuracy (without using user defined function)
 * also print sin(x) using library function.
 
 * Taken from: http://www.sanfoundry.com/c-program-value-sin-x/
 */
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
 
void main()
{
    int n, x1;
    float accuracy, term, denominator, x, sinx, sinval;
 
    printf("Enter the value of x (in degrees) \n");
    scanf("%f", &x);
    x1 = x;
    /*  Converting degrees to radians */
    x = x * (3.142 / 180.0);
    sinval = sin(x);
    printf("Enter the accuracy for the result \n");
    scanf("%f", &accuracy);
    term = x;
    sinx = term;
    n = 1;
    do
    {
        denominator = 2 * n * (2 * n + 1);
        term = -term * x * x / denominator;
        sinx = sinx + term;
        n = n + 1;
    } while (accuracy <= fabs(sinval - sinx));
    printf("Sum of the sine series = %f \n", sinx);
    printf("Using Library function sin(%d) = %f\n", x1, sin(x));
}
