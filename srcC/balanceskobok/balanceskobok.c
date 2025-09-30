#include <stdio.h>

int main()
{
    char str[1000];
    int balance = 0;
    printf("Введите строку: ");
    scanf("%[^\n]%*c", str);
    
    for (int i = 0; str[i] != '0'; i++) {
        if (str[i] == '(') {
            balance++;
        } else if (str[i] == ')') {
            balance--;
        }
        
        if (balance < 0) {
            break;
        }
    }
    
    if (balance == 0) {
        printf("Баланс скобок соблюден\n");
    } else {
        printf("Баланс скобок нарушен\n");
    }
    
    return 0;
}