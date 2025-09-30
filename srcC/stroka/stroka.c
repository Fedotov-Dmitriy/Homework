#include <stdio.h>
#include <string.h>

int main()
{
    char S[1000];
    char S1[1000];
    
    printf("Введите главную строку S: ");
    scanf("%[^\n]%*c", S);
    
    printf("Введите подстроку S1: ");
    scanf("%[^\n]%*c", S1);
    
    int count = 0;
    int len_S = strlen(S);
    int len_S1 = strlen(S1);
    
    if (len_S1 > len_S) {
        printf("Результат: 0\n");
        return 0;
    }
    
    for (int i = 0; i <= len_S - len_S1; i++) {
        int found = 1;
        
        for (int j = 0; j < len_S1; j++) {
            if (S[i + j] != S1[j]) {
                found = 0;
                break;
            }
        }
        
        if (found == 1) {
            count++;
        }
    }
    
    printf("Результат: %d\n", count);
    
    return 0;
}