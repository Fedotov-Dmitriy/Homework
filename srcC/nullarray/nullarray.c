
#include <stdio.h>
int main()
{
    int Array[] = {5, 0, 23, 0, -4, 8, 0, 100, 12, 0};
    int arrayLength = sizeof(Array) / sizeof(Array[0]);
    int zeroCount = 0;
    for (size_t i = 0; i < arrayLength; i++) {
        if (Array[i] == 0)
            zeroCount++;
    }

    printf("%d\n", zeroCount);

    return 0;
}