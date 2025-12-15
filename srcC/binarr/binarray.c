#include <stdio.h>
int sum_of_binary_digits(int n) {
    int sum = 0;
    while (n > 0) {
        sum += n % 2;  
        n /= 2;  
    }
    return sum;
}

int main() {
    int n;
    printf("Введите количество элементов в массиве: ");
    scanf("%d", &n);

    int arr[n];
    printf("Введите элементы массива:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    int max_sum = -1;
    for (int i = 0; i < n; i++) {
        int sum = sum_of_binary_digits(arr[i]);
        if (sum > max_sum) {
            max_sum = sum;
        }
    }

    for (int i = 0; i < n; i++) {
        if (sum_of_binary_digits(arr[i]) == max_sum) {
            printf("Максимальное Число в двоичной системе  в массиве = %d ", arr[i]);
        }
    }
    printf("\n");

    return 0;
}
