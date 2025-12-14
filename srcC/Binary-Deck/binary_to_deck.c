#include <stdio.h>
#include <stdlib.h>

void ConvertDecToTwosBin(int* bits, int bitCount, int value)
{
    if (value < 0) {
        value = 256 + value;
    }

    for (int i = bitCount - 1; i >= 0; i--) {
        bits[i] = value % 2;
        value /= 2;
    }
}

int ConvertTwosBin8ToDec(int* bits)
{
    int result = 0;

    for (int i = 0; i < 8; i++) {
        if (bits[7 - i] == 1) {
            result += (1ULL << i);
        }
    }

    if (bits[0] == 1) {
        return result - 256;
    }

    return result;
}

void AddBinary(int* leftBits, int* rightBits, int* sumBits)
{
    for (int i = 7; i >= 0; i--) {
        if (leftBits[i] + rightBits[i] + sumBits[i] < 2) {
            sumBits[i] = leftBits[i] + rightBits[i] + sumBits[i];
        } else if (i != 0) {
            sumBits[i - 1] = 1;
            sumBits[i] = (leftBits[i] + rightBits[i] + sumBits[i]) % 2;
        } else {
            sumBits[i] = (leftBits[i] + rightBits[i] + sumBits[i]) % 2;
        }
    }
}

void Print(int* bits)
{
    for (int i = 0; i < 8; i++) {
        printf("%d", bits[i]);
    }
    printf("\n");
}
