#include <stdint.h>
#include <stdio.h>
#include <math.h>
typedef union {
    double value;
    uint8_t bytes[8];
} Number;

static void parseDouble(Number number, double* outMantissa, int* outExponent)
{
    uint64_t bitPattern = 0;
    for (int i = 7; i >= 0; --i) {
        bitPattern = (bitPattern << 8) | number.bytes[i];
    }

    uint32_t signBit = (uint32_t)((bitPattern >> 63) & 1);
    uint32_t exponentBits = (uint32_t)((bitPattern >> 52) & 0x7FF);
    uint64_t fractionBits = bitPattern & 0xFFFFFFFFFFFFFULL;

    const int exponentBias = 1023;
    const double fractionDivisor = pow(2,52);

    int exponent = (int)exponentBits - exponentBias;
    double mantissa = 1.0 + (double)fractionBits / fractionDivisor;

    *outMantissa = signBit ? -mantissa : mantissa;
    *outExponent = exponent;

    if (exponentBits == 0 && fractionBits == 0) {
        *outMantissa = 0.0;
        *outExponent = 0;
    }
}

int main(void)
{
    Number number;

    printf("Enter a number: ");
    if (scanf("%lf", &number.value) != 1) {
        printf("Error reading input.\n");
        return 1;
    }

    int exponent = 0;
    double mantissa = 0.0;

    parseDouble(number, &mantissa, &exponent);
    printf("Result: %.15g*2^%d\n", mantissa, exponent);

    return 0;
}
