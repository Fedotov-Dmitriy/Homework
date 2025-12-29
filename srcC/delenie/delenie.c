#include <stdio.h>

int main(void)
{
    long long a, b;
    scanf("%lld %lld", &a, &b);

    if (b == 0) {
        printf("Деление на 0 невозможно\n");
        return 0;
    }

    long long sign = 1;   

    if (a < 0) {
        a = 0 - a;        
        sign = 0 - sign;
    }
    if (b < 0) {
        b = 0 - b;        
        sign = 0 - sign;
    }

    long long q = 0;      
    while (a >= b) {
        a = a - b;
        q = q + 1;
    }

    q = q * sign;
    printf("%lld\n", q);
    return 0;
}
