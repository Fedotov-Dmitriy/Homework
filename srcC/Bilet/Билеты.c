#include <stdio.h>

int main() {
    int count[28] = {0}; 
    
    for (int a = 0; a <= 9; a++) {
        for (int b = 0; b <= 9; b++) {
            for (int c = 0; c <= 9; c++) {
                int s = a + b + c;
                count[s]++;
            }
        }
    }
    unsigned int kolichevstvo = 0;
    for (int s = 0; s <= 27; s++) {
        kolichevstvo += (unsigned int)count[s] * count[s];
    }

    printf("Количевство билетов = %u\n", kolichevstvo);
    return 0;
}
