#include <stdio.h>

int main() {
    float principal,rate, time,interest;

    // Input the values
    printf("Enter the principal amount: ");
    scanf("%f", &principal);

    printf("Enter the annual interest rate (in percentage): ");
    scanf("%f", &rate);

    printf("Enter the time (in years): ");
    scanf("%f", &time);

    // Calculate simple interest
    interest = (principal * rate * time) / 100;

    // Output the result
    printf("The simple interest is: %.2f\n", interest);

    return 0;
}
