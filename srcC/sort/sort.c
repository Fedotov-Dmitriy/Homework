#include <stdio.h>

extern int sort_numbers(int* array, int count);

int main() {
    int numbers[100];
    int count = 0;
    
    while (scanf("%d", &numbers[count]) == 1 && count < 100) {
        count++;
    }
    
    int moved_count = sort_numbers(numbers, count);
    
    for (int i = 0; i < count; i++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");
    
    return moved_count;
}