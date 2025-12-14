#include "binary_to_deck.h"
#include <stdio.h>

int main(void)
{
    int d1;
    int d2;

    if (scanf("%d", &d1) != 1)
        return 1;
    if (scanf("%d", &d2) != 1)
        return 1;

    if (d1 < -128 || d1 > 127 || d2 < -128 || d2 > 127) {
        printf("Числа не в диапазон [-128; 127]\n");
        return 1;
    }

    int b1[] = { 0, 0, 0, 0, 0, 0, 0, 0 };
    int b2[] = { 0, 0, 0, 0, 0, 0, 0, 0 };
    int r[]  = { 0, 0, 0, 0, 0, 0, 0, 0 };

    ConvertDecToTwosBin(b1, 8, d1);
    ConvertDecToTwosBin(b2, 8, d2);
    int carryLine[] = { 0, 0, 0, 0, 0, 0, 0, 0 };
    int carry = 0;

    for (int i = 7; i >= 0; i--) {
        carryLine[i] = carry;
        if (b1[i] + b2[i] + carry >= 2)
            carry = 1;
        else
            carry = 0;
    }

    AddBinary(b1, b2, r);

    printf("carry: ");
    Print(carryLine);

    printf("  b1: ");
    Print(b1);

    printf("+ b2: ");
    Print(b2);

    printf("    ");
    for (int i = 0; i < 8; i++)
        printf("-");
    printf("\n");

    printf("   r: ");
    Print(r);

    printf("%d\n", ConvertTwosBin8ToDec(r));
    return 0;
}
