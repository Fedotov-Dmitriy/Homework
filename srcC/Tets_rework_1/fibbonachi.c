#include <stdio.h>

int main(void) {
    const int LIMIT = 1000000;

    long long a = 1;   
    long long b = 2;   
    long long sum = 0;

    while (a <= LIMIT) {
        if (a % 2 == 0) {
            sum += a;
        }
        long long next = a + b;
        a = b;
        b = next;
    }

    printf("Sum = %lld\n", sum);
    return 0;
}
