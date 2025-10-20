#include <stdio.h>

int main(void){
    int mass[] = {0,1,2,3,4,8,5,11}; // инициализируйте массив 
    int minPosition, tmp;
    for (int i = 0; i < (sizeof(mass) / sizeof(mass[0])); i++)
{
    minPosition = i;
    for (int j = i + 1; j < (sizeof(mass) / sizeof(mass[0])); j++)
        if (mass[minPosition] > mass[j])
            minPosition = j;
    tmp = mass[minPosition];
    mass[minPosition] = mass[i];
    mass[i] = tmp;
}
for (int i = 0; i < (sizeof(mass) / sizeof(mass[0])); i++)
        printf("%d ", mass[i]);
}