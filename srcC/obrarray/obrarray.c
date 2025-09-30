#include <stdio.h>

int main()
{
    int m, n;
    
    printf("Введите m и n: ");
    scanf("%d %d", &m, &n);
    
    int size = m + n;
    int x[1000];
    
    printf("Введите %d элементов массива: ", size);
    for (int i = 0; i < size; i++) {
        scanf("%d", &x[i]);
    }
    
    printf("Исходный массив: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", x[i]);
    }
    printf("\n");
    
    for (int i = 0; i < m; i++) {
        int temp = x[0];
        for (int j = 0; j < size - 1; j++) {
            x[j] = x[j + 1];
        }
        x[size - 1] = temp;
    }
    
    printf("Результат: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", x[i]);
    }
    printf("\n");
    
    return 0;
}