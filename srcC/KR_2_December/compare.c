#include <stdio.h>
#include <stdbool.h>
#include <string.h>

// возвращаем -1 если a < b, 0 если a == b, 1 если a > b.
int compare(const bool *a, size_t na,
                   const bool *b, size_t nb)
{
    //проходим ведущие нули
    size_t i = 0;
    while (i < na && !a[i]) i++;
    size_t j = 0;
    while (j < nb && !b[j]) j++;
    size_t len_a = na - i;
    size_t len_b = nb - j;
    //если длинна разная
    if (len_a < len_b) return -1;
    if (len_a > len_b) return 1;
    //если числа равны
    while (i < na && j < nb) {
        if (a[i] != b[j]) {
            return a[i] ? 1 : -1;
        }
        i++;
        j++;
    }

    return 0;
}

int main(void)
{
    char bufA[256], bufB[256];

    printf("Введите первое бинарное число: ");
    scanf("%255s", bufA);

    printf("Введите второе бинарное число: ");
    scanf("%255s", bufB);

    size_t na = strlen(bufA);
    size_t nb = strlen(bufB);

    bool a[256], b[256];
    for (size_t i = 0; i < na; i++)
        a[i] = (bufA[i] == '1');

    for (size_t i = 0; i < nb; i++)
        b[i] = (bufB[i] == '1');

    int cmp = compare(a, na, b, nb);

    if (cmp < 0)      printf("a < b\n");
    else if (cmp > 0) printf("a > b\n");
    else              printf("a == b\n");

    return 0;
}
