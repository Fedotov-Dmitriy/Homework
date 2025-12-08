#include <stdio.h>

void swap(int* a, int* b)
{ 
    int temp = *a;
    *a = *b;
    *b = temp;
}

void gnomeSort(int arr[], int n)
{
    int index = 0;
    while (index < n) {
        if (index == 0) {
            index++;
        } else if (arr[index] >= arr[index - 1]) {
            index++; 
        } else {
            swap(&arr[index], &arr[index - 1]); 
            index--; 
        }
    }
}

int main(void)
{
    int arr[] = { 1, 7, 8, 2, 5, 4 };
    int arr2[] = { 1 };
    gnomeSort(arr2, 1);
    gnomeSort(arr, 6);
    for (int i = 0; i < 6; i++) {
        printf("%d", arr[i]);
    }
    printf("\n");
}