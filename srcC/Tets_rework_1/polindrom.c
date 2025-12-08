#include <stdbool.h>
#include <stdio.h>
#include <string.h>

bool isPalindrome(char* str) 
{
    int left = 0;
    int right = strlen(str) - 1;
    while (left < right) {
        while (str[left] == ' ') {
            left++;
        }
        while (str[right] == ' ') { 
            right--;
        }
        if (str[left] != str[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}

int main(void)
{
    char input[1024];
    bool res = false;
    printf("Введите строку: ");
    scanf("%[^\n]%*c", input);
    res = isPalindrome(input);
    if (res) {
        printf("Строка является полиндромом\n");
    } else {
        printf("Строка не является полиндромом\n");
    }
}