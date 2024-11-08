
#include <stdio.h>

int main() {
    int age;
    float income;

    // Prompt user to input age
    printf("Enter your age: ");
    scanf("%d", &age);

    // Prompt user to input annual income
    printf("Enter your annual income (in Sh): ");
    scanf("%f", &income);

    // Check if customer meets loan requirements
    if (age >= 21,&&income >= 21000) {
        printf("Congratulations! you qualify for a loan.\n");
    } else {
        printf("Sorry,you request we can't process it now try again later .\n");
    }

    return 0;
}
