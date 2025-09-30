#include <stdio.h>

int main() {
    int a, b;
    int chastnoe = 0;
    int znak = 1;
    
    printf("Vvedite a: ");
    scanf("%d", &a);
    printf("Vvedite b: ");
    scanf("%d", &b);
    
    if (b == 0) {
        printf("Oshibka! Na nol delit nelzya!\n");
        return 1;
    }
    
    if ((a < 0 && b > 0) || (a > 0 && b < 0)) {
        znak = -1;
    }
    
    if (a < 0) {
        a = -a;
    }
    if (b < 0) {
        b = -b;
    }
    
    while (a >= b) {
        a = a - b;
        chastnoe = chastnoe + 1;
    }
    
    chastnoe = chastnoe * znak;
    
    printf("Nepolnoe chastnoe: %d\n", chastnoe);
    printf("Ostatok: %d\n", a * znak);
    
    return 0;
}