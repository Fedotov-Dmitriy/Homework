#include <stdio.h>

int main() {
    double x, result;
    
    printf("Введите значение x: ");
    scanf("%lf", &x);
    
    double x2 = x * x;
    double temp = (x2 + x) * (x2 + 1);
    result = temp + 1;
    
    printf("x^4 + x^3 + x^2 + x + 1 = %.2f\n", result);

    return 0;
}