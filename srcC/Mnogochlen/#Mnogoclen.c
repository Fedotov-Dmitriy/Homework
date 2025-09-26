#include <stdio.h>
int  main(){
    int x; 
    int y;
    scanf("%d", &x);
    y = (x*x+x)*(x*x+1)+1;
    printf("%d\n",y );
    return 0;
}