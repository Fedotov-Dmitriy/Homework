#include <stdio.h>

int main() {
    int sums[28] = {0};
    
    for (int i = 0; i <= 999; i++) {
        int digit1 = i / 100;
        int digit2 = (i / 10) % 10;
        int digit3 = i % 10;
        int sum = digit1 + digit2 + digit3;
        sums[sum]++;
    }
    
    int lucky_tickets = 0;
    for (int i = 0; i < 28; i++) {
        lucky_tickets += sums[i] * sums[i];
    }
    
    printf("Количество счастливых билетов: %d\n", lucky_tickets);
    
    return 0;
}