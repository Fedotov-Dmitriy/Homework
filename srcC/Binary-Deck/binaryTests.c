#include "binary_to_deck.h"
#include <stdio.h>

void test2to10()
{
    int b17[]   = { 0, 0, 0, 1, 0, 0, 0, 1 }; // 17
    if (ConvertTwosBin8ToDec(b17) != 17) {
        printf("неверный перевод положительного числа в десятичную систему\n");
    }

    int bm43[]  = { 1, 1, 0, 1, 0, 1, 0, 1 }; // -43 (two's complement)
    if (ConvertTwosBin8ToDec(bm43) != -43) {
        printf("неверный перевод отрицательного числа в десятичную систему\n");
    }

    int b0[]    = { 0, 0, 0, 0, 0, 0, 0, 0 }; // 0
    if (ConvertTwosBin8ToDec(b0) != 0) {
        printf("неверный перевод нуля в десятичную систему\n");
    }

    int b127[]  = { 0, 1, 1, 1, 1, 1, 1, 1 }; // 127
    if (ConvertTwosBin8ToDec(b127) != 127) {
        printf("неверный перевод 127 в десятичную систему\n");
    }

    int bm128[] = { 1, 0, 0, 0, 0, 0, 0, 0 }; // -128
    if (ConvertTwosBin8ToDec(bm128) != -128) {
        printf("неверный перевод -128 в десятичную систему\n");
    }
}

void test10to2()
{
    int b17n[]   = { 0, 0, 0, 0, 0, 0, 0, 0 };
    int bm43n[]  = { 0, 0, 0, 0, 0, 0, 0, 0 };
    int b0n[]    = { 0, 0, 0, 0, 0, 0, 0, 0 };
    int b127n[]  = { 0, 0, 0, 0, 0, 0, 0, 0 };
    int bm128n[] = { 0, 0, 0, 0, 0, 0, 0, 0 };

    int b17[]    = { 0, 0, 0, 1, 0, 0, 0, 1 };
    int bm43[]   = { 1, 1, 0, 1, 0, 1, 0, 1 };
    int b0[]     = { 0, 0, 0, 0, 0, 0, 0, 0 };
    int b127[]   = { 0, 1, 1, 1, 1, 1, 1, 1 };
    int bm128[]  = { 1, 0, 0, 0, 0, 0, 0, 0 };

    ConvertDecToTwosBin(b17n,   8,  17);
    ConvertDecToTwosBin(bm43n,  8, -43);
    ConvertDecToTwosBin(b0n,    8,   0);
    ConvertDecToTwosBin(b127n,  8, 127);
    ConvertDecToTwosBin(bm128n, 8, -128);

    for (int i = 0; i < 8; i++) {
        if (b17[i] != b17n[i]) {
            printf("неверный перевод 17 в двоичную систему\n");
            break;
        }
    }

    for (int i = 0; i < 8; i++) {
        if (bm43[i] != bm43n[i]) {
            printf("неверный перевод -43 в двоичную систему\n");
            break;
        }
    }

    for (int i = 0; i < 8; i++) {
        if (b0[i] != b0n[i]) {
            printf("неверный перевод 0 в двоичную систему\n");
            break;
        }
    }

    for (int i = 0; i < 8; i++) {
        if (b127[i] != b127n[i]) {
            printf("неверный перевод 127 в двоичную систему\n");
            break;
        }
    }

    for (int i = 0; i < 8; i++) {
        if (bm128[i] != bm128n[i]) {
            printf("неверный перевод -128 в двоичную систему\n");
            break;
        }
    }
}

void testSumma()
{
    int b17[]  = { 0, 0, 0, 1, 0, 0, 0, 1 };
    int bm43[] = { 1, 1, 0, 1, 0, 1, 0, 1 };
    int r[]    = { 0, 0, 0, 0, 0, 0, 0, 0 };

    AddBinary(b17, bm43, r);

    int rr[] = { 1, 1, 1, 0, 0, 1, 1, 0 };

    for (int i = 0; i < 8; i++) {
        if (rr[i] != r[i]) {
            printf("неверное суммирование 17 + (-43)\n");
            break;
        }
    }
}

void testOverflow()
{
    // 127 + 1 = -128 (переполнение в 8 бит)
    int b127[] = { 0, 1, 1, 1, 1, 1, 1, 1 };
    int b1[]   = { 0, 0, 0, 0, 0, 0, 0, 1 };
    int r[]    = { 0, 0, 0, 0, 0, 0, 0, 0 };

    AddBinary(b127, b1, r);

    int exp[]  = { 1, 0, 0, 0, 0, 0, 0, 0 }; // -128

    for (int i = 0; i < 8; i++) {
        if (exp[i] != r[i]) {
            printf("неверное суммирование 127 + 1 (переполнение)\n");
            break;
        }
    }
}

int main(void)
{
    test10to2();
    test2to10();
    testSumma();
    testOverflow();
    printf("тесты завершены\n");
    return 0;
}

